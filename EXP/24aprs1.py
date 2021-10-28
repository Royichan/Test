class botique:
    def __init__(self,*args):
        self.bid=args[0]
        self.bname=args[1]
        self.btype=args[2]
        self.brate=args[3]
        self.bpoints=args[4]

class onlinebotique:
    def __init__(self,bdict):
        self.bdict=bdict
    
    def getb(self,low,up,extra,stype):
        rl=[]
        if stype.lower() in self.bdict.keys():
            blist=[]
            blist=self.bdict[stype.lower()]
            for q in blist:
                if q.btype.lower()==stype.lower():
                    if q.bpoints>=low and q.bpoints<=up:
                        q.brate=q.brate+extra
                        rl.append(q)
                    else:
                        rl.append(q)
        if len(rl)==0:
            return None
        else:
            rl.sort(reverse=True,key=lambda p:p.bpoints)
            return rl

if __name__=="__main__":
    bd=[]
    n=int(input())
    for k in range(n):
        i=int(input())
        n=input()
        t=input().lower()
        r=float(input())
        p=int(input())
        bd.append(botique(i,n,t,p,r))
    l=float(input())
    u=float(input())
    x=int(input())
    y=input()
    bdict={}
    for k in bd:
        if k.btype in bdict.keys():
            bdict[k.btype].append(k)
        else:
            bdict[k.btype]=[]
            bdict[k.btype].append(k)
    gb=onlinebotique(bdict)
    db=gb.getb(l,u,x,y)
    if db==None:
        print("No boutique found")
    else:
        for j in db:
            print(j.bid,j.bname,j.brate)