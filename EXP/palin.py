n=input()
d={}
for i in n:
    if i not in d:
        d[i]=n.count(i)
c=0
for i in d:
    if d[i]%2!=0:
        c=c+1
if c>1:
    print("palindrome not possible")
else:
    d=list(d.items())
    d.sort(key=lambda x: x[0])
    d=dict(d)
    res=""
    flag=''
    for i in d.keys():
        if d[i]%2==0:
            res=res+(i*int(d[i]/2))
        else:
            flag=i
    for i in range(d[flag]):
        res=res+flag
    r=""
    r=r+(res+res[:len(res)-d[flag]][::-1])
    print("palindrome : ",r)