class product:
    def __init__(self,*args):
        self.pname=args[0]
        self.ptype=args[1]
        self.pprice=args[2]
        self.pqty=args[3]
 
class store:
     def __init__(self,plist):
         self.plist=plist

    def purchase(self,spname,spqty):
        for i in self.plist:
            if (i.pname.lower()!=spname.lower()) and i.pqty!=0:
                return None
            else if i.pname.lower()==spname.lower() and spqty>i.pqty:
                    q=i.pqty
                    i.pqty=0
                    return (q*pprice)
            else if i.pname.lower()==spname.lower() and spqty<i.qpty:
                    q=i.pqty
                    i.pqty=i.pqty-spqty
                    return (spqty*pprice)

if __name__=="__main__":
    pl=[]
    n=int(input())
    for i in range(n):
        name=input()
        ttype=input()
        price=int(input())
        qty=int(input())
        pl.append(product(name,ttype,price,qty))
    spname=input()
    sqty=input()
    st=store(pl)
    bill=at.purchase(spname,sqty)
    if bill==None:
        print("No product found")
    else:
        print(bill)
    for i in pl:
        print(i.pname,i,pqty)