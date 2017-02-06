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
            RoomTypeId2=BatchAdd_RoomType_data['data'][1]['Rooms'][0]['RoomTypeId']
            RoomNumber1=BatchAdd_RoomType_data['data'][0]['Rooms'][0]['RoomNumber']
            RoomNumber2=BatchAdd_RoomType_data['data'][0]['Rooms'][1]['RoomNumber']
            RoomNumber3=BatchAdd_RoomType_data['data'][0]['Rooms'][2]['RoomNumber']            
            RoomNumber4=BatchAdd_RoomType_data['data'][0]['Rooms'][3]['RoomNumber']
            RoomNumber5=BatchAdd_RoomType_data['data'][0]['Rooms'][4]['RoomNumber']
            RoomNumber6=BatchAdd_RoomType_data['data'][0]['Rooms'][5]['RoomNumber']
            RoomNumber7=BatchAdd_RoomType_data['data'][0]['Rooms'][6]['RoomNumber']
            RoomNumber8=BatchAdd_RoomType_data['data'][0]['Rooms'][7]['RoomNumber']
            RoomNumber9=BatchAdd_RoomType_data['data'][0]['Rooms'][8]['RoomNumber']
            RoomNumber10=BatchAdd_RoomType_data['data'][0]['Rooms'][9]['RoomNumber']
            
            RoomNumber11=BatchAdd_RoomType_data['data'][1]['Rooms'][0]['RoomNumber']
            RoomNumber12=BatchAdd_RoomType_data['data'][1]['Rooms'][1]['RoomNumber']
            RoomNumber13=BatchAdd_RoomType_data['data'][1]['Rooms'][2]['RoomNumber']            
            RoomNumber14=BatchAdd_RoomType_data['data'][1]['Rooms'][3]['RoomNumber']
            RoomNumber15=BatchAdd_RoomType_data['data'][1]['Rooms'][4]['RoomNumber']
            RoomNumber16=BatchAdd_RoomType_data['data'][1]['Rooms'][5]['RoomNumber']
            RoomNumber17=BatchAdd_RoomType_data['data'][1]['Rooms'][6]['RoomNumber']
            RoomNumber18=BatchAdd_RoomType_data['data'][1]['Rooms'][7]['RoomNumber']
            RoomNumber19=BatchAdd_RoomType_data['data'][1]['Rooms'][8]['RoomNumber']
            RoomNumber20=BatchAdd_RoomType_data['data'][1]['Rooms'][9]['RoomNumber']

            BatchAdd_RoomType={'RoomTypeId1':RoomTypeId1,
                               'RoomTypeId2':RoomTypeId2,
                               'RoomNumber1':RoomNumber1,
                               'RoomNumber2':RoomNumber2,
                               'RoomNumber3':RoomNumber3,
                               'RoomNumber4':RoomNumber4,
                               'RoomNumber5':RoomNumber5,
                               'RoomNumber6':RoomNumber6,
                               'RoomNumber7':RoomNumber7,
                               'RoomNumber8':RoomNumber8,
                               'RoomNumber9':RoomNumber9,
                               'RoomNumber10':RoomNumber10,
                               'RoomNumber11':RoomNumber11,
                               'RoomNumber12':RoomNumber12,
                               'RoomNumber13':RoomNumber13,
                               'RoomNumber14':RoomNumber14,
                               'RoomNumber15':RoomNumber15,
                               'RoomNumber16':RoomNumber16,
                               'RoomNumber17':RoomNumber17,
                               'RoomNumber18':RoomNumber18,
                               'RoomNumber19':RoomNumber19,
                               'RoomNumber20':RoomNumber20}
            return BatchAdd_RoomType


        else:
            print "BatchAdd_RoomType is Failed. Message:%s Date:%s"%(Message,today)
            BatchAdd_RoomType={'Result':False}
            return BatchAdd_RoomType     

def Check_In(**self):
        payload = {
    "OccupationChangedList": [],
    "BillItemChangedList": [],
    "CustomerChangedList": [],
    "Data":
    {
    "Action": "1",
    "BillItems": [
        {
            "IsDeposit": False,
            "Amount": 100,
            "CreditTypeValue": "C9140",
            "CreditTypeName": "微信",
            "DebitTypeValue": "D1000",
            "DebitTypeName": "房费"
        }
    ],
    "Channel": {
        "k": "Hotel",
        "v": "酒店前台"
    },
    "CheckinType": "Normal",
    "HasGuaranty": False,
    "IsCheckout": False,
    "Liaison": {
        "Address": "",
        "Folk": "",
        "Gender": "0",
        "Mobile": "",
        "Name": "",
        "Point": 0.0,
        "arrowStatus": False
    },
    "OccupationsInfo": [
        {
            "EndDateTime":"%s"%tomorrow,
            "RoomFee": [
                {
                    "ActualPrice": 300.0,
                    "Date": "%s"%today,
                    "ExternalPrice": 0.0,
                    "IsExternalPrice": False,
                    "OrignMarketPrice": 300.0
                }
            ],
            "RoomNumber": self['RoomNumber'],
            "RoomType": {
                "k": self['RoomTypeId'],
                "v": "3"
            },
            "StartDateTime": "%s"%today
        }
    ],
    "Remark": ""
    }
}
        r = requests.request('POST',
                              self['url'], 
                              headers=Headers ,
                              data=json.dumps(payload))

        Check_In_data = json.loads(r.text)
        businessCode=CommonMoudle(Check_In_data['businessCode'] ,200)
        resultCode=CommonMoudle(Check_In_data['resultCode'] ,200) 
    
def Check_Out(**self):
     payload = {
    "RoomNumbers": [self['RoomNumber']],
    "InternalRemark": "备注信息",
    "BillItems": [{
                "IsDeposit": False,
                "Amount": 200,
                "CreditTypeValue": "C9140",
                "DebitTypeValue": "D1000",         
                "PayState": "0"
            },
            {
                "Reason": "",
                "IsDeposit": False,
                "Amount": 0.01,
                "CreditTypeValue": "C9140",
                "PayState": "0"
            }]
}
                   
        r = requests.request('PUT', self['url'], headers=Headers ,data=json.dumps(payload))

        Check_Out_data = json.loads(r.text)
        businessCode=CommonMoudle(Check_Out_data['businessCode'] ,200)
        resultCode=CommonMoudle(Check_Out_data['resultCode'] ,200)


    

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
    
    Check_In(url=Check_In_url,
             RoomTypeId=RoomType['RoomTypeId1'],
             RoomNumber=RoomType['RoomNumber1'])
  
    

    

    
    