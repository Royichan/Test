class Volcano:
    def __init__(self,*args):
        self.vname=args[0]
        self.county=args[1]
        self.year=args[2]

class Eruption:
    def __init__(self,vlist):
        self.vlist=vlist
    
    def findvol(self,scounty):
        vl=[]
        for i in self.vlist:
            if i.county.lower()==scounty.lower():
                vl.append(i)
        if len(vl)!=0:
            return vl
        else:
            return None
    
    def findstat(self,svname):
        for i in self.vlist:
            if i.vname.lower()==svname.lower():
                if (2021-i.year)>=25:
                    return "low probability"
                elif (2021-i.year)<=50 and (2021-i.year)>25:
                    return "high probability"
                elif i.year==2021:
                    return "active"
                else:
                    return "inactive"
            else:
                return None

if __name__=="__main__":
    vl=[]
    n=int(input())
    for i in range(n):
        vname=input()
        county=input()
        year=int(input())
        rl.append(Volcano(vname,county,year))
    svname=input()
    scounty=input()
    er=Eruption(vl)
    res1=er.findvol(scounty)
    res2=er.findstat(svname)
    if res1!=None:
        for i in res1:
            print(i.vname)
            print(i.county)
            print(i.year)
    else:
        print("no volcano found")
    if res2!=None:
        print(res2)
    else:
        print("No matching records found with in the records")