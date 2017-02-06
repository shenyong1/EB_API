# -*- coding: utf-8 -*-
from Config.EB_API_Config import *
from nose.config import flag
from string import lower
from random import choice
import string
import random

def GetNumber(length=8,chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])


def CommonMoudle(Path,data):
    if Path==data:
        return True
    else:
        return False
      
def Del_All(ownerId): 
    sql1= "delete from iPms.RoomType where ownerId=%s"%ownerId
    sql2= "delete from iPmsBiz.Rooms where ownerId=%s"%ownerId
    sql3= "select * from iPms.RoomType where ownerId=%s"%ownerId
    sql4= "select * from iPmsBiz.Rooms where Ownerid=%s"%ownerId
          
    curs = conn.cursor()
    Del_RoomType = curs.execute(sql1)
    Del_Rooms    = curs.execute(sql2)
    Now_RoomType = curs.execute(sql3)
    Now_Rooms    = curs.execute(sql4)
    conn.close()
    
    print "Del RoomType:%s"%Del_RoomType
    print "Del Rooms:%s"   %Del_Rooms
    print "Now RoomType:%s"%Now_RoomType
    print "Now Rooms:%s"   %Now_Rooms
    
def BatchAdd_RoomType(**self):
        payload = [{
                    "RoomTypeName":   self['RoomTypeName1'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber1_1']
            },
            {
                "RoomNumber": self['RoomNumber1_2']
            },
            {
                "RoomNumber": self['RoomNumber1_3']
            },
            {
                "RoomNumber": self['RoomNumber1_4']
            },
            {
                "RoomNumber": self['RoomNumber1_5']
            },
            {
                "RoomNumber": self['RoomNumber1_6']
            },
            {
                "RoomNumber": self['RoomNumber1_7']
            },
            {
                "RoomNumber": self['RoomNumber1_8']
            },
            {
                "RoomNumber": self['RoomNumber1_9']
            },
            {
                "RoomNumber": self['RoomNumber1_10']
            }
                              
                              ]
                   },
                {
                    "RoomTypeName":   self['RoomTypeName2'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber2_1']
            },
            {
                "RoomNumber": self['RoomNumber2_2']
            },
            {
                "RoomNumber": self['RoomNumber2_3']
            },
            {
                "RoomNumber": self['RoomNumber2_4']
            },
            {
                "RoomNumber": self['RoomNumber2_5']
            },
            {
                "RoomNumber": self['RoomNumber2_6']
            },
            {
                "RoomNumber": self['RoomNumber2_7']
            },
            {
                "RoomNumber": self['RoomNumber2_8']
            },
            {
                "RoomNumber": self['RoomNumber2_9']
            },
            {
                "RoomNumber": self['RoomNumber2_10']
            }
                            
        ]
        }]
        
                   
        r = requests.request('POST', self['url'], headers=Headers ,data=json.dumps(payload))

        BatchAdd_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(BatchAdd_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(BatchAdd_RoomType_data['resultCode'] ,200)
        Message=BatchAdd_RoomType_data['Message']

         
        if businessCode & resultCode ==True:
            print "BatchAdd_RoomType is Pass. Message:%s Date:%s"%(Message,today)
#             for type in range(0,7):
#                  print type               
#                 for number in range(0,10):
#                      print number
#                     RoomTypeId_S=('BatchAdd_RoomType_data'+'[data][%s]'+'[Rooms]'+'[%s][RoomTypeId]')%(type,number)
#                     print RoomTypeId_S
#                     RoomTypeId = json.loads(RoomTypeId_S)
#                     print   RoomTypeId  
            RoomTypeId1=BatchAdd_RoomType_data['data'][0]['Rooms'][0]['RoomTypeId']
            RoomNumber1=BatchAdd_RoomType_data['data'][0]['Rooms'][0]['RoomNumber']
            print BatchAdd_RoomType_data


        else:
            print "BatchAdd_RoomType is Failed. Message:%s Date:%s"%(Message,today)
            BatchAdd_RoomType={'Result':False}
            return BatchAdd_RoomType     

    
  
    

if __name__ == "__main__":
#     Order_Detail=All_Store(storeid=Headers['ownerid'],url=PO_Search_url)
# 
#     Name(url=PO_Search_url, 
#          storeid=Headers['ownerid'],
#          iphone="None",
#          name='房客',
#          OrgId='None',
#          order='None',
#          status='None')
#     
#     Time(url=PO_Search_url,
#          storeid=Headers['ownerid'],
#          roomTypeId='None',
#          dateTimeType='0',
#          queryDateTimeBegin='2016-12-12',
#          queryDateTimeEnd='2016-12-13'
#          )

    RoomTypeName = random.sample(xrange(90000000), 100)
    RoomNumber   = random.sample(xrange(80000000), 100)
    print RoomTypeName
    print RoomNumber
    
    Del_All(ownerId='434265567985665')
    
    RoomType=BatchAdd_RoomType(CaseNumber='TCS_001',
                          url=Search_RoomType_url,
                          OTARoomTypeName='Test',
                          OTARoomTypeId='Z23582JSC',
                          RoomTypeName1=RoomTypeName[1],
                          RoomNumber1_1=RoomNumber[1],
                          RoomNumber1_2=RoomNumber[2],
                          RoomNumber1_3=RoomNumber[3],
                          RoomNumber1_4=RoomNumber[4],
                          RoomNumber1_5=RoomNumber[5],                          
                          RoomNumber1_6=RoomNumber[6],                          
                          RoomNumber1_7=RoomNumber[7],                          
                          RoomNumber1_8=RoomNumber[8],                          
                          RoomNumber1_9=RoomNumber[9],                          
                          RoomNumber1_10=RoomNumber[10],                                                    
                          RoomTypeName2=RoomTypeName[2],
                          RoomNumber2_1=RoomNumber[11],
                          RoomNumber2_2=RoomNumber[12],
                          RoomNumber2_3=RoomNumber[13],                          
                          RoomNumber2_4=RoomNumber[14],                            
                          RoomNumber2_5=RoomNumber[15],                            
                          RoomNumber2_6=RoomNumber[16],                            
                          RoomNumber2_7=RoomNumber[17],                            
                          RoomNumber2_8=RoomNumber[18],                            
                          RoomNumber2_9=RoomNumber[19],                            
                          RoomNumber2_10=RoomNumber[20],                            
                          weekdayPrice='300')
    

    

    
    