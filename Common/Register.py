# -*- coding: utf-8 -*-
from Config.EB_API_Config import *
from nose.config import flag
from string import lower
from random import choice
import string
import random

def CommonMoudle(Path,data):
    if Path==data:
        return True
    else:
        return False
      

    
def Register(**self):
        Num=random.sample(xrange(90000000), 100)
        
        payload = {
        "PartnerId": Num[1],
        "PartnerName": "ding",
        "Mobile": "15500000551",
        "AuthToken":Num[2],
        "AcctId":Num[3],
        "BDID":"123",
        "OpenEntry":"aaaa",
        "HotelInfo": {
            "HotelName": "123451",
            "Contact": "ding",
            "HotelId": Num[4],
            "Address": "铜川路",
            "Tel": "51492147",
            "Brand": "汉庭",
            "Longitude": 217.46,
            "Latitude": 31.147,
            "City": "上海",
            "RoomTypes": [
                {
                   "weekdayPrice": 100.0,
                   "weekendPrice": 90.0,
                   "OtaRoomTypeId": Num[5],
                    "OtaRoomTypeName": "大床房",
                    "RoomTypeName": "大床房",
                    "RoomNumbers":[]
                }
            ]
        }
    }

                 
        r = requests.request('POST', self['url'], headers=Headers ,data=json.dumps(payload))
        T=r.elapsed.microseconds/1000


        Register_data = json.loads(r.text)
        businessCode=CommonMoudle(Register_data['businessCode'] ,200)
        resultCode=CommonMoudle(Register_data['resultCode'] ,200)
                                                         
        if businessCode & resultCode ==True and T<300:
            print "Register is Pass.Time:%s ms"%(T)  
 
#             RoomType={'RoomTypeName':RoomTypeName,
#                'RoomNumber':RoomNumber,
#                'RoomTypeId':RoomTypeId,
#                'RoomID':RoomID,
#                'Result':True}
#             return RoomType

        else:
            print "Register is Failed.Time:%s ms"%(T)
#             RoomType={'Result':False}
#             return RoomType

    

if __name__ == "__main__":

#     RoomTypeName = random.sample(xrange(90000000), 100)
#     RoomNumber   = random.sample(xrange(80000000), 100)
#     print RoomTypeName
#     print RoomNumber
    for num in range(1,1001):
        if num !=1000:
            print "num:%s"%(num)
            Register(url=Register_API_url)
        else:
            print "ok"
        
        
        
        
        
        
        