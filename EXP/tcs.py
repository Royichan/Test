class paint:
    def __init__(self, paintingID, paintingName, paintingType, paintingPrice):
        self.paintingID=paintingID
        self.paintingName=paintingName
        self.paintingType=paintingType
        self.paintingPrice=paintingPrice

class showroom:
    def totalprice(self,k,l):
        for i in k:
            print(i.paintingPrice)                     


def main():
    n=int(input())
    p = []
    for i in range(0,n):
        p.append(paint(int(input()), input(), input(), int(input())))
    
    for i in p:
        print(i.paintingID)
        print(i.paintingName)
        print(i.paintingType)
        print(i.paintingPrice)
    
    s = showroom()
    s.totalprice(p,n)
    print("This is the final print statement.")

if "__name__" == main():
   main()
       
