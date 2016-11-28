from Common.TestFuntion import *

class UseTest():
    def __init__(self, name):
        self.name = name

    def Setup(self):
        RoomID=Add_RoomType(Add_RoomType_url,Room['RoomTypeName'],Room['RoomNumber'])
        result = RoomID[4]
        if (result != True):
#             logging.error("%s", status[result])
            return result
        logging.info("%s Setup Phase Done", self.name)
        return result

    def Test(self):
        result = Search_All_RoomType(Search_All_RoomType_url,self.RoomID[0],self.RoomID[1])
        if (result != True):
#             logging.error("%s", status[result])
            return result
#         result = Search_All_RoomType(Search_All_RoomType_url,self.RoomID[0],self.RoomID[1])
#         if (result != True):
#             logging.error("%s", status[result])
#             return result
        logging.info("%s Test Phase Done", self.name)
        return result

    def CleanUp(self):
        result = Del_RoomType(Del_RoomType_url, RoomID[2])
        if (result != True):
#             logging.error("%s", status[result])
            return result
        logging.info("%s CleanUp Phase Done", self.name)
        return result



if __name__ == "__main__":
    #########
    # Unit tests
    #########
    #testName = 'TCUI_USE_01'
    test = UseTest('TCUI_USE_01')
    #logging.info("Executing %s", testName)
    
    test.Setup()
    print "ok"