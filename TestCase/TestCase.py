from Common.RoomType import *

class UseTest():
    def __init__(self, name):
        self.name = name

    def Setup(self):
        print "Test Start"



    def Test(self):
        RoomTypeName=GetNumber(8)
        RoomNumber=GetNumber(10)
        NewRoomTypeName=GetNumber(9)
  
        RoomType=Add_RoomType(url=RoomType_API_url,RoomTypeName=RoomTypeName,RoomNumber=RoomNumber,weekdayPrice='300')

        Result = RoomType['Result']
        if (Result != True):
            return Result
        
        Status=RoomType_Status(url=RoomType_Status_url,
                        RoomTypeId=RoomType['RoomTypeId'])

        
        Result = Status['Result']
        if (Result != True):
            return Result
        
        Modify=Modify_RoomType(url=RoomType_API_url,
                        RoomTypeName=Room['NewRoomTypeName'],
                        RoomTypeId=RoomType['RoomTypeId'],
                        weekdayPrice=999,
                        RoomNumber=RoomType['RoomNumber'],
                        RoomID=RoomType['RoomID'],
                        IsActive=False)
        
        Result = Modify['Result']
        if (Result != True):
            return Result
        
        
    def CleanUp(self):
        print "Test End"


if __name__ == "__main__":
    test = UseTest('TCS_001')
    test.Test()
    
    