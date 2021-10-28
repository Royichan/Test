class document:
    def  __init__(self,*args):
        self.did=args[0]
        self.dname=args[1]
        self.ddetail=args[2]

class darchive:
    def __init__(self,*args):
        self.aid=args[0]
        self.dlist=args[1]

    def finddate(self):
        rel=[]
        for i in self.slist:
            if "/" in i.ddetail:
                s=i.ddetails.strip().split(",")
                for j in s:
                    if "/" in j:
                        rel.append((i.did,j))
        return rel

    def doccount(self,stype):
        count=0
        for i in self.dlist:
            if stype==i.dname.split(".")[1]:
                count=count+1
        return count

if __name__=="__main__":
    dl=[]
    n= int(input())
    for i in range(n):
        iid=int(input())
        name=input()
        detail=input()
        dl.append(document(iid,name,detail))
    stype=input()
    do=document('1',dl)
    res1=do.finddate()
    res2=do.doccount(stype)
    for i in res1:
        print(i[0],i[1])
    if res2==0:
        print("no doc")
    else:
        print("Document Count = ",res2)