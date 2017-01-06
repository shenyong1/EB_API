from Common.RoomType import *

class UseTest():
    def __init__(self, CaseNumber):
        self.CaseNumber = CaseNumber

    def Setup(self):
        print "Test Start"



    def Test(self,CaseNumber):
        RoomTypeName=GetNumber(8)
        RoomTypeName1=GetNumber(8)
        RoomTypeName2=GetNumber(8)  
        RoomNumber=GetNumber(10)
        RoomNumber1=GetNumber(10)
        RoomNumber2=GetNumber(10)
        RoomNumber3=GetNumber(10)
        RoomNumber4=GetNumber(10)
        NewRoomTypeName=GetNumber(9)
  
        RoomType=BatchAdd_RoomType(CaseNumber=self.CaseNumber,
                          url=Search_RoomType_url,
                          RoomTypeName1=RoomTypeName1,
                          OTARoomTypeName='Test',
                          OTARoomTypeId='Z23582JSC',
                          RoomNumber1_1=RoomNumber1,
                          RoomNumber1_2=RoomNumber2,
                          RoomTypeName2=RoomTypeName2,
                          RoomNumber2_1=RoomNumber3,
                          RoomNumber2_2=RoomNumber4,
                          weekdayPrice='300')
        Result = RoomType['Result']
        if (Result != True):
            return Result
       
                
    def CleanUp(self):
        print "Test End"


if __name__ == "__main__":
    test = UseTest('TCS004')
    test.Test(CaseNumber='TCS004')
    
    