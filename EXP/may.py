class doctor:
    def __init__(self,id, name, dept, fee, sun):
        self.id=id
        self.name=name
        self.dept=dept
        self.fee=fee
        self.sun=sun

class hospital:
    list=[]
    def getdoc(self,qdept,doclist):
        for i in doclist:
            if i.dept==qdept and i.sun==qsun:
                list.append(i)
        return list

    def selectdoc(self,fee,doclist):
        for i in doclist:
            if i.fee>qfee and sun=="not available":
                self.doclist.remove(i)
                return True
        else:
            return False



if __name__=="__main__":
    doclist=[]
    for i in range(0,5):
        id=int(input())
        name=input().lower()
        dept=input().lower()
        fee=int(input())
        sun=input().lower()
        d=doctor(id,name,dept,fee,sun)
        doclist.append(d)
    qsun=input().lower()
    qdept=input().lower()
    qfee=int(input())
    hos=hospital()
    res1=hos.getdoc(qdept,doclist)
    res2=hos.selectdoc(qfee,doclist)
    if res1==[]:
        print("Doc not found")
    else:
        for k in res1:
            print(k.id)
            print(k.name)
    if res2:
        for k in doclist:
            print(k.id)
            print(k.name)
    else:
        print("original list")
        for k in doclist:
            print(k.id)
            print(k.name)