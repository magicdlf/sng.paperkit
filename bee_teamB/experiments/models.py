import csv,json,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
PAPER=Path(__file__).resolve().parents[1]
p=PAPER
DURATIONS=[3,5,12,21]
SURVIVAL=[.97,.99,.999,.985,.955]
INITIAL=[3000,4500,10000,15000,6000]

def simulate(model):
    state=INITIAL[:];rows=[]
    for day in range(61):
        wet=20<=day<30
        activity=.45 if wet and model>=2 else 1
        rows.append([day,*state,activity*state[4],activity*state[4]*100])
        if day==60:break
        survival=SURVIVAL[:];transfers=[1/d for d in DURATIONS];eggs=1500
        if wet and model==3:
            survival[4]=.94;transfers[3]*=.7;eggs*=.85
        alive=[n*s for n,s in zip(state,survival)]
        moved=[alive[i]*transfers[i] for i in range(4)]
        nxt=[alive[0]-moved[0]+eggs]+[alive[i]-moved[i]+moved[i-1] for i in range(1,4)]+[alive[4]+moved[3]]
        assert all(math.isfinite(n) and n>=0 for n in nxt)
        assert abs(sum(nxt)-sum(alive)-eggs)<1e-7
        state=nxt
    return rows

font='/System/Library/Fonts/Supplemental/Arial.ttf';Fnt=lambda n:ImageFont.truetype(font,n)
colors=['#8b80bf','#4d9c9a','#d0a144','#447db1','#e07c45']
def chart(title,subtitle,curves,labels,name):
 im=Image.new('RGB',(1100,650),'white');d=ImageDraw.Draw(im);l,r,t,b=115,1040,120,500
 maxv=max(max(v) for v in curves);ymax=math.ceil(maxv/5000)*5000
 X=lambda x:l+(r-l)*x/60;Y=lambda y:b-(b-t)*y/ymax
 d.text((l,22),title,font=Fnt(28),fill='#25344b');d.text((l,66),subtitle,font=Fnt(18),fill='#66758a')
 d.rectangle((X(20),t,X(30),b),fill='#edf1f6')
 for i in range(5):
  y=ymax*i/4;d.line((l,Y(y),r,Y(y)),fill='#e1e7ee');d.text((25,Y(y)-11),f'{y:,.0f}',font=Fnt(18),fill='#66758a')
 d.line((l,t,l,b,r,b),fill='#66758a',width=2)
 for day in range(0,61,10):d.text((X(day)-10,b+14),str(day),font=Fnt(18),fill='#66758a')
 for j,values in enumerate(curves):d.line([(X(i),Y(v)) for i,v in enumerate(values)],fill=colors[j],width=3)
 # Deliberately incomplete legends; teacher key identifies what is missing.
 for j,label in enumerate(labels):
  xx=130+j*210;d.line((xx,604,xx+32,604),fill=colors[j],width=3);d.text((xx+40,591),label,font=Fnt(18),fill='#25344b')
 d.text((545,545),'Day',font=Fnt(20),fill='#25344b');d.text((l,95),'Bees',font=Fnt(17),fill='#66758a')
 im.save(p/'assets'/name)

outputs={}
for model in [1,2,3]:
    rows=simulate(model);outputs[str(model)]=rows
    with (PAPER/'experiments'/f'model-{model}.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['day','eggs','larvae','pupae','hive_bees','foragers','active_foragers','visits_per_day']);w.writerows(rows)
    chart(f'Model {model}: colony composition','Daily population by stage',[[row[j] for row in rows] for j in range(1,6)],['Eggs','Larvae','Pupae','Hive bees'],f'model-{model}-stages.png')
    chart(f'Model {model}: pollination capacity','Population and available workforce',[[row[5] for row in rows],[row[6] for row in rows]],['Foragers','Active foragers'],f'model-{model}-workforce.png')
    visits=sum(row[7] for row in rows[20:30])/10
    print(model,round(rows[-1][4]+rows[-1][5]),round(visits),math.ceil(2000000/visits))
(PAPER/'experiments/models.json').write_text(json.dumps(outputs))
assert outputs['1'][0]==outputs['2'][0]==outputs['3'][0]
assert all(a[1:6]==b[1:6] for a,b in zip(outputs['1'],outputs['2']))
