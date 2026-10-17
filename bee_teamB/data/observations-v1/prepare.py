import csv,json,hashlib,collections
from pathlib import Path
P=Path(__file__).resolve().parent
source=json.loads((P/'source.json').read_text())
f=P/'raw/pop.csv'
if not f.exists():raise SystemExit('Missing raw/pop.csv: download original CSV from the source page first.')
raw=f.read_bytes();expected=next(x for x in source['files'] if x['path']=='pop.csv')['digest']
if hashlib.sha256(raw).hexdigest()!=expected:raise SystemExit('SHA256 differs from recorded Dryad version. Inspect provenance before continuing.')
rows=[{k.strip():v for k,v in row.items()} for row in csv.DictReader(raw.decode('utf-8-sig').splitlines())]
required=['Colony.ID','demography','Eggs','Larvae','Pupae','Adults','Total']
if not rows or any(k not in rows[0] for k in required):raise SystemExit('Actual columns differ from source documentation: inspect the original file.')
groups=collections.defaultdict(list);missing=[];totals=[];keys=set()
for i,row in enumerate(rows,2):
 key=(row['Colony.ID'],row['demography'])
 if key in keys:raise SystemExit('Duplicate colony/date: inspect before splitting.')
 keys.add(key);groups[row['Colony.ID']].append(row)
 vals={}
 for k in required[2:]:
  try:vals[k]=float(row[k])
  except ValueError:missing.append({'line':i,'column':k,'value':row[k]})
 if len(vals)==5:
  delta=vals['Total']-sum(vals[k] for k in ['Eggs','Larvae','Pupae','Adults'])
  if abs(delta)>1:totals.append({'line':i,'difference':delta})
out=P/'prepared';out.mkdir(exist_ok=True)
for number,(colony,data) in enumerate(sorted(groups.items()),1):
 with (out/('colony-%02d.csv'%number)).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(data)
report={'rows':len(rows),'colonies':{k:len(v) for k,v in groups.items()},'missing_or_nonnumeric':missing,'total_discrepancies':totals,'date_policy':'Raw strings preserved; date format not yet interpreted.'}
(P/'quality.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
