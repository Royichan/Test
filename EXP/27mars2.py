class person:
    def __init__(self,*args):
        self.name=args[0]
        self.height=args[1]
        self.weight=args[2]
        self.bmi=0
        self.bmistatus=""
    
    def calbmi(self):
        self.bmi=round(self.weight/self.height**2)

class society:
    def __init__(self,status,plist):
        self.status=status
        self.plist=plist
        print(self.plist[0].name)
    
    def cbs(self,pname):
        pc=0
        for i in self.plist:
            if i.name.lower()==pname.lower():
                print("ok")
                i.calbmi()
                for d in self.status.keys():
                    if i.bmi<=self.status[d][1] and i.bmi>=self.status[d][0]:
                        i.bmistatus=d
                        pc=pc+1
        if pc==0:
            return False
        else:
            return True

    def rip(self,sbmi):
        rl=[]
        for i in self.plist:
            i.calbmi()
            if i.bmi<sbmi:
                rl.append(i)
        return rl

if __name__=="__main__":
    l=[]
    n=int(input())
    for i in range(n):
        name=input()
        height=int(input())
        weight=int(input())
        pe=person(name,height,weight)
        l.append(pe)
    d={}
    k=int(input())
    for j in range(k):
        s=input()
        o=int(input())
        u=int(input())
        if o<u:
            d[s]=(o,u)
        else:
            d[s]=(u,o)
    pname=input()
    sbmi=int(input())
    so=society(d,l)
    res1=so.cbs(pname)
    res2=so.rip(sbmi)
    if res1==False:
        print("No Person Exists")
    else:
        for i in l:
            if i.name==pname and i.bmi!=0:
                print(i.bmi,i.bmistatus)
    if len(l)==0:
        print("No Invalid")
    else:
        for j in res2:
            print(j.name,j.bmi)