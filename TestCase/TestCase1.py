from Common.TestFuntion import *
import logging


class TestCase1():

    def setUp(self):
        RoomID=Add_RoomType(Add_RoomType_url,Room['RoomTypeName'],Room['RoomNumber'])
        result = RoomID[4]
        if (result != True):
#             logging.error("%s", status[result])
            return result
#         logging.info("%s Setup Phase Done", self.name)
        return result

    def Testfunc1(self):
        result = Search_All_RoomType(Search_All_RoomType_url,self.RoomID[0],self.RoomID[1])
        if (result != True):
#             logging.error("%s", status[result])
            return result
#         result = Search_All_RoomType(Search_All_RoomType_url,self.RoomID[0],self.RoomID[1])
#         if (result != True):
#             logging.error("%s", status[result])
#             return result
#         logging.info("%s Test Phase Done", self.name)
        return result


    def tearDown(self):
        result = Del_RoomType(Del_RoomType_url, self.RoomID[2])
        if (result != True):
#             logging.error("%s", status[result])
            return result
#         logging.info("%s CleanUp Phase Done", self.name)
        return result