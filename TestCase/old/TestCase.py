from Common.TestFuntion import *

class UseTest():
    def __init__(self, name):
        self.name = name

    def Setup(self):
        print "Test Start"


    def Test(self):
        RoomID=Add_RoomType(RoomType_API_url,Room['RoomTypeName'],Room['RoomNumber'])
        result = RoomID[4]
        if (result != True):
            return result
        
        Add_RoomType(RoomType_API_url,RoomID[0],RoomID[1])

        
        result = Add_RoomType(RoomType_API_url,RoomID[0],Room['NewRoomTypeName'])
        if (result != True):
            return result
        



    def CleanUp(self):
        print "Test End"




if __name__ == "__main__":
    #########
    # Unit tests
    #########
    #testName = 'TCUI_USE_01'
    test = UseTest('TCS_001')
    #logging.info("Executing %s", testName)
    

    test.Test()