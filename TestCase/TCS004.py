from Common.RoomType import *

class UseTest():
    def __init__(self, CaseNumber):
        self.CaseNumber = CaseNumber

    def Setup(self):
        print "Test Start"



    def Test(self,CaseNumber):
        RoomTypeName = random.sample(xrange(90000000), 100)
        RoomNumber   = random.sample(xrange(80000000), 100)
  
        RoomType=BatchAdd_RoomType(CaseNumber=self.CaseNumber,
                          url=Search_RoomType_url,
                          RoomTypeName1=RoomTypeName[1],
                          OTARoomTypeName='Test',
                          OTARoomTypeId='Z23582JSC',
                          RoomNumber1_1=RoomNumber[1],
                          RoomNumber1_2=RoomNumber[2],
                          RoomTypeName2=RoomTypeName[2],
                          RoomNumber2_1=RoomNumber[3],
                          RoomNumber2_2=RoomNumber[4],
                          weekdayPrice='300')
        Result = RoomType['Result']
        if (Result != True):
            return Result
       
                
    def CleanUp(self):
        print "Test End"


if __name__ == "__main__":
    test = UseTest('TCS004')
    test.Test(CaseNumber='TCS004')
    
    