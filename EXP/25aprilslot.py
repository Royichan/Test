class property:
    def __init__(self,*args):
        self.ptype=args[0]
        self.pvalue=args[1]
        self.maxbid=args[2]

class tender:
    def __init__(self,*args):
        self.bname=args[0]
        self.ptype=args[1]
        self.bid=args=[2]

def bidp(plist,tlist):
    rl=[]
    tlist.sort(key=lambda x:x.bid)
    for p in plist:
        for t in tlist:
            if t.ptype.lower()==p.ptype().lower():
                if t.bid>=p.pvalue and t.bid<=p.maxbid:
                    plist.remove(p)
                    rl.append(t.bname)
    if rl!=[]:
        return rl
    else:
        return None

if __name__=="__main__":
    plist=[]
    pn=int(input())
    for i in range(pn):
        ptype=input()
        pvalue=int(input())
        maxbid=int(input())
        plist.append(property(ptype,pvalue,maxbid))
    tlist=[]
    tn=int(input())
    for i in range(tn):
        bname=input()
        ptype=input()
        bid=int(input())
        tlist.append(tender(bname,ptype,bid))
    res1=bidp(plist,tlist)
    if res1==None:
        print(No property found)
    else:
        for i in res1:
            print(i)
    for i in plist:
        print(i.ptype)