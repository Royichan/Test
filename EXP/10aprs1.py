class One:
    def _init_(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

class Two:
    def _init_(self,lis):
        self.lis=lis
        #self.extra=extra
        
    def first(self):
        res=[]
        for i in self.lis:
            if len(res) ==0:
                res.append(i)
            elif i.a < res[0].a:
                res.pop()
                res.append(i)
        return res
    
    def second(self):
        newlist = sorted(self.lis, key=lambda x: x.c)
        return newlist
    
n=int(input())
arr=[]
for i in range(n):
    a=input()
    b=int(input())
    c=int(input())
    d=input()
    
    arr.append(One(a,b,c,d))
#extra=input()
ob=Two(arr)
out1=ob.first()
out2=ob.second()

if len(out1) >0:
    for j in out1:
        print(j.a)
        print(j.b)
        print(j.c)
        print(j.d)

else:
    print("No Data Found")

if len(out2) >0:
    for j in out2:
        print(j.c)
else:
    print("No Data Found")