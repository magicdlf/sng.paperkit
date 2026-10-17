from pathlib import Path
import csv,datetime,collections,json,math,statistics
from PIL import Image,ImageDraw,ImageFont
root=Path('/Users/magicdlf/claude/HiMCMPaper');paper=root/'workshop/papers/bee-stages-02-data';out=paper/'data/observations-v1';assets=paper/'assets'
rows=[]
for original in csv.DictReader((root/'workshop/data/pop.csv').open()):
 r={k.strip():v for k,v in original.items()};r['date']=datetime.datetime.strptime(r['demography'],'%m/%d/%y').date()
 for k in ['Adults','Pupae','Larvae','Eggs','Total']:r[k]=float(r[k]);assert math.isfinite(r[k]) and r[k]>=0
 assert abs(r['Total']-sum(r[k] for k in ['Adults','Pupae','Larvae','Eggs']))<=1
 rows.append(r)
g=collections.defaultdict(list)
for r in rows:g[r['Colony.ID']].append(r)
for rr in g.values():rr.sort(key=lambda r:r['date'])
start=min(r['date'] for r in rows);end=max(r['date'] for r in rows);days=(end-start).days
complete=[k for k,v in g.items() if len(v)==25]
report={'rows':len(rows),'colonies':len(g),'start':str(start),'end':str(end),'complete_series_colonies':complete,'coverage':{},'midpoint_flags':[]}
for k,rr in g.items():
 report['coverage'][k]={'n':len(rr),'first':str(rr[0]['date']),'last':str(rr[-1]['date']),'adult_start':rr[0]['Adults'],'adult_end':rr[-1]['Adults'],'adult_peak':max(r['Adults'] for r in rr)}
 for a,b,c in zip(rr,rr[1:],rr[2:]):
  fraction=(b['date']-a['date']).days/(c['date']-a['date']).days
  residuals={v:b[v]-(a[v]+fraction*(c[v]-a[v])) for v in ['Eggs','Larvae','Pupae','Adults']}
  if all(abs(v)<=1 for v in residuals.values()):report['midpoint_flags'].append({'colony':k,'date':str(b['date']),'residuals':residuals})
font='/System/Library/Fonts/Supplemental/Arial.ttf';ft=lambda n:ImageFont.truetype(font,n)
colors={'Eggs':'#8064b2','Larvae':'#2e9389','Pupae':'#c18a23','Adults':'#3679b6'}
ticks=[datetime.date(2022,6,1),datetime.date(2022,9,1),datetime.date(2022,12,1),datetime.date(2023,3,1),datetime.date(2023,5,1)]
def panel(d,rect,rr,stage,title,ymax):
 x,y,w,h=rect;l=x+70;r=x+w-20;t=y+42;b=y+h-45
 X=lambda day:l+(r-l)*(day-start).days/days;Y=lambda val:b-(b-t)*val/ymax
 d.text((x+12,y+4),title,font=ft(22),fill='#22334b')
 for i in range(4):
  val=ymax*i/3;yy=Y(val);d.line((l,yy,r,yy),fill='#e1e6ed');d.text((x+5,yy-10),f'{val/1000:.0f}k',font=ft(17),fill='#5d6d80')
 d.line((l,t,l,b,r,b),fill='#8592a3',width=1)
 for day in ticks:d.text((X(day)-24,b+11),day.strftime('%b'),font=ft(17),fill='#5d6d80')
 pts=[(X(row['date']),Y(row[stage])) for row in rr]
 d.line(pts,fill=colors[stage],width=2)
 for px,py in pts:d.ellipse((px-4,py-4,px+4,py+4),fill=colors[stage])
 return X,Y
im=Image.new('RGB',(1500,1080),'white');d=ImageDraw.Draw(im)
d.text((32,20),'Adult counts: nine colonies, one shared scale',font=ft(31),fill='#22334b')
d.text((32,67),'Original CSV values | points are dated records; lines only connect them | blank tails mean no record',font=ft(21),fill='#5d6d80')
for index,k in enumerate(sorted(g,key=int)):
 panel(d,(20+index%3*495,115+index//3*300,480,285),g[k],'Adults',f'Colony {k}  |  n={len(g[k])}',30000)
d.text((35,1030),'Calendar axis: June 2022 through May 2023. No missing date is replaced by zero.',font=ft(20),fill='#5d6d80')
im.save(assets/'observed-adults-nine-colonies.png')
im=Image.new('RGB',(1500,900),'white');d=ImageDraw.Draw(im)
d.text((35,20),'Colony 6: adults and immature stages do not move together',font=ft(30),fill='#22334b')
d.text((35,65),'Original CSV values | each panel has its own count scale | no fitted or simulated curves',font=ft(21),fill='#5d6d80')
for index,stage in enumerate(['Eggs','Larvae','Pupae','Adults']):
 ymax={'Eggs':6000,'Larvae':6000,'Pupae':6000,'Adults':15000}[stage]
 panel(d,(20+index%2*740,112+index//2*340,725,325),g['6'],stage,stage,ymax)
d.text((35,832),'31 Oct 2022: Eggs = Larvae = Pupae = 0; Adults = 10,894. Zero entries need measurement-context checks.',font=ft(20),fill='#5d6d80')
im.save(assets/'observed-colony6-four-stages.png')
# Compare averages over the same five colonies, avoiding a changing membership.
report['fixed_five_means']={}
for date in sorted(set(r['date'] for r in rows)):
 rr=[r for r in rows if r['date']==date and r['Colony.ID'] in complete]
 if len(rr)==5:report['fixed_five_means'][str(date)]={k:sum(r[k] for r in rr)/5 for k in ['Eggs','Larvae','Pupae','Adults']}
(out/'analysis.json').write_text(json.dumps(report,indent=2)+'\n')
print('midpoint flags',len(report['midpoint_flags']),report['midpoint_flags'][:8])
print('verified records',len(rows),'range',start,end)
page='''# What the downloaded observations show

Source: Chen et al., Dryad DOI 10.5061/dryad.5tb2rbpg5. The original pop.csv contains 185 dated records from nine colonies, from 30 May 2022 to 15 May 2023. Fractional counts are retained because the stage quantities are estimates. These figures use that CSV, not a published model figure.

![Adult counts for all nine colonies, with the same date and count scales.](assets/observed-adults-nine-colonies.png){#fig:observed-adults width=100%}

Colony trajectories differ. Colony 9 rises from 12,932 to 25,171 adults across its full record, while Colony 5 falls from 5,156 to 3,647. Four series end earlier than the others; their disappearance from the table does not establish why recording stopped. Do not replace these missing tails by zero or treat changing-membership averages as a seasonal trajectory.

![Egg, larval, pupal and adult counts for Colony 6. Scales differ across panels.](assets/observed-colony6-four-stages.png){#fig:observed-stages width=100%}

Colony 6 illustrates a difference between adult abundance and recruitment-stage abundance. On 31 October 2022, all three immature stages are recorded as zero, while 10,894 adults remain. On 15 May 2023 the table records immature stages again and 11,807 adults. A zero stage count therefore does not by itself establish irreversible colony loss; measurement and management context must be checked.

Using the same five colonies throughout (5, 6, 7, 8, 9), mean larvae rise from 921 on 16 January to 2,911 on 27 February 2023; mean adults rise from 6,037 to 8,873. This describes a shared-subset change, not evidence that food or weather caused it. The subset excludes incomplete records and is not necessarily representative of all nine colonies.

The sampling is mostly about two weeks apart and does not directly measure daily deaths, births or transition probabilities. Some adjacent values also match linear interpolation unusually closely; consult the original processing and field records before treating every row as an independent measurement. Keep these limitations visible when fitting a stage model.
'''
(paper/'sections/00-data-handover.md').write_text(page)
