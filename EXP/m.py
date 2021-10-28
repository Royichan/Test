class Doctor:
    def __init__(self,doctorId, doctorName, deptName, consultFee,sundayAvailable):
        self.doctorId = doctorId
        self.doctorName =doctorName
        self.deptName = deptName
        self.consultFee = consultFee
        self.sundayAvailable= sundayAvailable

class Hospital:
    def __init__(self, doctorList):
        self.doctorList = doctorList
        
    def getDoctorList(self,dptName):#2
        lst =[]
        for item in doctorList:
           if item.deptName.lower()==dptName.lower() and item.sundayAvailable.lower() == "available":
                lst.append(item)
        return lst
            
        
        
    def selectDoctor(self,fees):
        for item in doctorList:#3
            if item.sundayAvailable.lower()=="not available" and item.consultFee>fees:
                doctorList.remove(item)
                return True
        return False
        
        
doctorList =[]
for i in range(5):
    doctorId = eval(input())
    doctorName= input()
    deptName = input()
    consultFee= eval(input())
    sundayAvailable= input()
    x = Doctor(doctorId,doctorName,deptName,consultFee,sundayAvailable)
    doctorList.append(x)

y = Hospital(doctorList) #1
dptName= input()
fees = eval(input())

lst = y.getDoctorList(dptName)

if len(lst)==0:
    print("Doctor Not Found")
else:
    for item in lst:
        print(item.doctorId)
        print(item.doctorName)

if y.selectDoctor(fees):#4
    temp= []
    orderedList =[]
    for item in doctorList:
        temp.append(item.consultFee)
        temp.sort()
    for item in temp:
        for doc in doctorList:
            if item==doc.consultFee:
                orderedList.append(doc)
                doctorList.remove(doc)

    for item in orderedList:
        print(item.doctorId)
        print(item.doctorName)
        print(item.consultFee)
                
else:
    print("Returning the original List:")
    for item in doctorList:
        print(item.doctorId)
        print(item.doctorName)