import json,csv,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DURATIONS=[3,5,12,21]
SURVIVAL=[.97,.99,.999,.985,.955]
INITIAL=[3000,4500,10000,15000,6000]

def run(rain=True):
    state=INITIAL[:]; rows=[]
    for day in range(61):
        wet=rain and 20<=day<30
        activity=.45 if wet else 1.0
        rows.append([day,*state,activity*state[4],activity*state[4]*100])
        if day==60:break
        survival=SURVIVAL[:]
        if wet:survival[4]=.94
        transfers=[1/d for d in DURATIONS]
        if wet:transfers[3]*=.7
        alive=[state[i]*survival[i] for i in range(5)]
        moved=[alive[i]*transfers[i] for i in range(4)]
        eggs=1500*(.85 if wet else 1)
        nxt=[alive[0]-moved[0]+eggs,alive[1]-moved[1]+moved[0],alive[2]-moved[2]+moved[1],alive[3]-moved[3]+moved[2],alive[4]+moved[3]]
        assert all(math.isfinite(n) and n>=0 for n in nxt)
        assert abs(sum(nxt)-sum(alive)-eggs)<1e-7
        state=nxt
    return rows

def main():
    outputs={name:run(rain) for name,rain in [('sunny',False),('rainy',True)]}
    for name,rows in outputs.items():
        with (ROOT/(name+'.csv')).open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['day','eggs','larvae','pupae','hive_bees','foragers','active_foragers','visits_per_day']);w.writerows(rows)
    (ROOT/'outputs.json').write_text(json.dumps(outputs))
    return outputs
if __name__=='__main__':main()
