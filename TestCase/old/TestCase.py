from Common.TestFuntion import *

class UseTest():
    def __init__(self, name):
        self.name = name

    def Setup(self):
        print "Test Start"


    def Test(self):
        RoomID=Add_RoomType(Add_RoomType_url,Room['RoomTypeName'],Room['RoomNumber'])
        result = RoomID[4]
        if (result != True):
            return result
        
        result = Search_All_RoomType(Search_All_RoomType_url,RoomID[0],RoomID[1])
        if (result != True):
            return result
        
        result = Del_RoomType(Del_RoomType_url, RoomID[2])
        if (result != True):
            return result


    def CleanUp(self):
        print "Test End"




if __name__ == "__main__":
    #########
    # Unit tests
    #########
    #testName = 'TCUI_USE_01'
    test = UseTest('TCUI_USE_01')
    #logging.info("Executing %s", testName)
    

    test.Test()

    print "ok"