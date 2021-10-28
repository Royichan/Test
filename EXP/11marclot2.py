class table:
    def __init__(self,*args):
        self.tno=args[0]
        self.wname=args[1]
        self.status=args[2]
    
    def waitertable(self,tlist):
        dw={}
        for i in tlist:
            if i.wname not in dw:
                dw[wname]=1
            else:
                dw[wname]=dw[wname]+1
        
        return dw

    def tablewaiter(self,tlist,stno):
        for i in tlist:
            if i.tno==stno:
                return i.wname
            else:
                return None
if __name__=="__main__":
    n=int(input())
    tl=[]
    for j in range(n):
        tno=int(input())
        wname=input()
        status=input()
        tl.append(table(tno,wname,status))
    stno=int(input())
    t=table()
    d=t.waitertable(tlist)
    for a in d:
        print(a,"-",d[a])
    y=t.tablewaiter(tlist,stno)
    if y==None:
        print("No Table")
    else:
        print(y)