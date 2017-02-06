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
        },
{
                    "RoomTypeName":   self['RoomTypeName3'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber3_1']
            },
            {
                "RoomNumber": self['RoomNumber3_2']
            },
            {
                "RoomNumber": self['RoomNumber3_3']
            },
            {
                "RoomNumber": self['RoomNumber3_4']
            },
            {
                "RoomNumber": self['RoomNumber3_5']
            },
            {
                "RoomNumber": self['RoomNumber3_6']
            },
            {
                "RoomNumber": self['RoomNumber3_7']
            },
            {
                "RoomNumber": self['RoomNumber3_8']
            },
            {
                "RoomNumber": self['RoomNumber3_9']
            },
            {
                "RoomNumber": self['RoomNumber3_10']
            }
                              
                              ]
                   },
{
                    "RoomTypeName":   self['RoomTypeName4'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber4_1']
            },
            {
                "RoomNumber": self['RoomNumber4_2']
            },
            {
                "RoomNumber": self['RoomNumber4_3']
            },
            {
                "RoomNumber": self['RoomNumber4_4']
            },
            {
                "RoomNumber": self['RoomNumber4_5']
            },
            {
                "RoomNumber": self['RoomNumber4_6']
            },
            {
                "RoomNumber": self['RoomNumber4_7']
            },
            {
                "RoomNumber": self['RoomNumber4_8']
            },
            {
                "RoomNumber": self['RoomNumber4_9']
            },
            {
                "RoomNumber": self['RoomNumber4_10']
            }
                              
                              ]
                   },
{
                    "RoomTypeName":   self['RoomTypeName5'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber5_1']
            },
            {
                "RoomNumber": self['RoomNumber5_2']
            },
            {
                "RoomNumber": self['RoomNumber5_3']
            },
            {
                "RoomNumber": self['RoomNumber5_4']
            },
            {
                "RoomNumber": self['RoomNumber5_5']
            },
            {
                "RoomNumber": self['RoomNumber5_6']
            },
            {
                "RoomNumber": self['RoomNumber5_7']
            },
            {
                "RoomNumber": self['RoomNumber5_8']
            },
            {
                "RoomNumber": self['RoomNumber5_9']
            },
            {
                "RoomNumber": self['RoomNumber5_10']
            }
                              
                              ]
                   },
{
                    "RoomTypeName":   self['RoomTypeName6'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber6_1']
            },
            {
                "RoomNumber": self['RoomNumber6_2']
            },
            {
                "RoomNumber": self['RoomNumber6_3']
            },
            {
                "RoomNumber": self['RoomNumber6_4']
            },
            {
                "RoomNumber": self['RoomNumber6_5']
            },
            {
                "RoomNumber": self['RoomNumber6_6']
            },
            {
                "RoomNumber": self['RoomNumber6_7']
            },
            {
                "RoomNumber": self['RoomNumber6_8']
            },
            {
                "RoomNumber": self['RoomNumber6_9']
            },
            {
                "RoomNumber": self['RoomNumber6_10']
            }
                              
                              ]
                   },
{
                    "RoomTypeName":   self['RoomTypeName7'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber7_1']
            },
            {
                "RoomNumber": self['RoomNumber7_2']
            },
            {
                "RoomNumber": self['RoomNumber7_3']
            },
            {
                "RoomNumber": self['RoomNumber7_4']
            },
            {
                "RoomNumber": self['RoomNumber7_5']
            },
            {
                "RoomNumber": self['RoomNumber7_6']
            },
            {
                "RoomNumber": self['RoomNumber7_7']
            },
            {
                "RoomNumber": self['RoomNumber7_8']
            },
            {
                "RoomNumber": self['RoomNumber7_9']
            },
            {
                "RoomNumber": self['RoomNumber7_10']
            }
                              
                              ]
                   },
{
                    "RoomTypeName":   self['RoomTypeName8'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber8_1']
            },
            {
                "RoomNumber": self['RoomNumber8_2']
            },
            {
                "RoomNumber": self['RoomNumber8_3']
            },
            {
                "RoomNumber": self['RoomNumber8_4']
            },
            {
                "RoomNumber": self['RoomNumber8_5']
            },
            {
                "RoomNumber": self['RoomNumber8_6']
            },
            {
                "RoomNumber": self['RoomNumber8_7']
            },
            {
                "RoomNumber": self['RoomNumber8_8']
            },
            {
                "RoomNumber": self['RoomNumber8_9']
            },
            {
                "RoomNumber": self['RoomNumber8_10']
            }
                              
                              ]
                   },
{
                    "RoomTypeName":   self['RoomTypeName9'],
                    "weekdayPrice":   self['weekdayPrice'],
                    "OTARoomTypeName":self['OTARoomTypeName'],
                    "OTARoomTypeId":  self['OTARoomTypeId'],
                    "Rooms": [
            {
                "RoomNumber": self['RoomNumber9_1']
            },
            {
                "RoomNumber": self['RoomNumber9_2']
            },
            {
                "RoomNumber": self['RoomNumber9_3']
            },
            {
                "RoomNumber": self['RoomNumber9_4']
            },
            {
                "RoomNumber": self['RoomNumber9_5']
            },
            {
                "RoomNumber": self['RoomNumber9_6']
            },
            {
                "RoomNumber": self['RoomNumber9_7']
            },
            {
                "RoomNumber": self['RoomNumber9_8']
            },
            {
                "RoomNumber": self['RoomNumber9_9']
            },
            {
                "RoomNumber": self['RoomNumber9_10']
            }
                              
                              ]
                   }
                   ]
        
                   
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
            RoomTypeId3=BatchAdd_RoomType_data['data'][2]['Rooms'][0]['RoomTypeId']
            RoomTypeId4=BatchAdd_RoomType_data['data'][3]['Rooms'][0]['RoomTypeId']
            RoomTypeId5=BatchAdd_RoomType_data['data'][4]['Rooms'][0]['RoomTypeId']
            RoomTypeId6=BatchAdd_RoomType_data['data'][5]['Rooms'][0]['RoomTypeId']
            RoomTypeId7=BatchAdd_RoomType_data['data'][6]['Rooms'][0]['RoomTypeId']
            RoomTypeId8=BatchAdd_RoomType_data['data'][7]['Rooms'][0]['RoomTypeId']
            RoomTypeId9=BatchAdd_RoomType_data['data'][8]['Rooms'][0]['RoomTypeId']    
            
            
            
            
            
            
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

            RoomNumber21=BatchAdd_RoomType_data['data'][2]['Rooms'][0]['RoomNumber']
            RoomNumber22=BatchAdd_RoomType_data['data'][2]['Rooms'][1]['RoomNumber']
            RoomNumber23=BatchAdd_RoomType_data['data'][2]['Rooms'][2]['RoomNumber']            
            RoomNumber24=BatchAdd_RoomType_data['data'][2]['Rooms'][3]['RoomNumber']
            RoomNumber25=BatchAdd_RoomType_data['data'][2]['Rooms'][4]['RoomNumber']
            RoomNumber26=BatchAdd_RoomType_data['data'][2]['Rooms'][5]['RoomNumber']
            RoomNumber27=BatchAdd_RoomType_data['data'][2]['Rooms'][6]['RoomNumber']
            RoomNumber28=BatchAdd_RoomType_data['data'][2]['Rooms'][7]['RoomNumber']
            RoomNumber29=BatchAdd_RoomType_data['data'][2]['Rooms'][8]['RoomNumber']
            RoomNumber30=BatchAdd_RoomType_data['data'][2]['Rooms'][9]['RoomNumber']

            RoomNumber31=BatchAdd_RoomType_data['data'][3]['Rooms'][0]['RoomNumber']
            RoomNumber32=BatchAdd_RoomType_data['data'][3]['Rooms'][1]['RoomNumber']
            RoomNumber33=BatchAdd_RoomType_data['data'][3]['Rooms'][2]['RoomNumber']            
            RoomNumber34=BatchAdd_RoomType_data['data'][3]['Rooms'][3]['RoomNumber']
            RoomNumber35=BatchAdd_RoomType_data['data'][3]['Rooms'][4]['RoomNumber']
            RoomNumber36=BatchAdd_RoomType_data['data'][3]['Rooms'][5]['RoomNumber']
            RoomNumber37=BatchAdd_RoomType_data['data'][3]['Rooms'][6]['RoomNumber']
            RoomNumber38=BatchAdd_RoomType_data['data'][3]['Rooms'][7]['RoomNumber']
            RoomNumber39=BatchAdd_RoomType_data['data'][3]['Rooms'][8]['RoomNumber']
            RoomNumber40=BatchAdd_RoomType_data['data'][3]['Rooms'][9]['RoomNumber']

            RoomNumber41=BatchAdd_RoomType_data['data'][4]['Rooms'][0]['RoomNumber']
            RoomNumber42=BatchAdd_RoomType_data['data'][4]['Rooms'][1]['RoomNumber']
            RoomNumber43=BatchAdd_RoomType_data['data'][4]['Rooms'][2]['RoomNumber']            
            RoomNumber44=BatchAdd_RoomType_data['data'][4]['Rooms'][3]['RoomNumber']
            RoomNumber45=BatchAdd_RoomType_data['data'][4]['Rooms'][4]['RoomNumber']
            RoomNumber46=BatchAdd_RoomType_data['data'][4]['Rooms'][5]['RoomNumber']
            RoomNumber47=BatchAdd_RoomType_data['data'][4]['Rooms'][6]['RoomNumber']
            RoomNumber48=BatchAdd_RoomType_data['data'][4]['Rooms'][7]['RoomNumber']
            RoomNumber49=BatchAdd_RoomType_data['data'][4]['Rooms'][8]['RoomNumber']
            RoomNumber50=BatchAdd_RoomType_data['data'][4]['Rooms'][9]['RoomNumber']

            RoomNumber51=BatchAdd_RoomType_data['data'][5]['Rooms'][0]['RoomNumber']
            RoomNumber52=BatchAdd_RoomType_data['data'][5]['Rooms'][1]['RoomNumber']
            RoomNumber53=BatchAdd_RoomType_data['data'][5]['Rooms'][2]['RoomNumber']            
            RoomNumber54=BatchAdd_RoomType_data['data'][5]['Rooms'][3]['RoomNumber']
            RoomNumber55=BatchAdd_RoomType_data['data'][5]['Rooms'][4]['RoomNumber']
            RoomNumber56=BatchAdd_RoomType_data['data'][5]['Rooms'][5]['RoomNumber']
            RoomNumber57=BatchAdd_RoomType_data['data'][5]['Rooms'][6]['RoomNumber']
            RoomNumber58=BatchAdd_RoomType_data['data'][5]['Rooms'][7]['RoomNumber']
            RoomNumber59=BatchAdd_RoomType_data['data'][5]['Rooms'][8]['RoomNumber']
            RoomNumber60=BatchAdd_RoomType_data['data'][5]['Rooms'][9]['RoomNumber']

            RoomNumber61=BatchAdd_RoomType_data['data'][6]['Rooms'][0]['RoomNumber']
            RoomNumber62=BatchAdd_RoomType_data['data'][6]['Rooms'][1]['RoomNumber']
            RoomNumber63=BatchAdd_RoomType_data['data'][6]['Rooms'][2]['RoomNumber']            
            RoomNumber64=BatchAdd_RoomType_data['data'][6]['Rooms'][3]['RoomNumber']
            RoomNumber65=BatchAdd_RoomType_data['data'][6]['Rooms'][4]['RoomNumber']
            RoomNumber66=BatchAdd_RoomType_data['data'][6]['Rooms'][5]['RoomNumber']
            RoomNumber67=BatchAdd_RoomType_data['data'][6]['Rooms'][6]['RoomNumber']
            RoomNumber68=BatchAdd_RoomType_data['data'][6]['Rooms'][7]['RoomNumber']
            RoomNumber69=BatchAdd_RoomType_data['data'][6]['Rooms'][8]['RoomNumber']
            RoomNumber70=BatchAdd_RoomType_data['data'][6]['Rooms'][9]['RoomNumber']

            RoomNumber71=BatchAdd_RoomType_data['data'][7]['Rooms'][0]['RoomNumber']
            RoomNumber72=BatchAdd_RoomType_data['data'][7]['Rooms'][1]['RoomNumber']
            RoomNumber73=BatchAdd_RoomType_data['data'][7]['Rooms'][2]['RoomNumber']            
            RoomNumber74=BatchAdd_RoomType_data['data'][7]['Rooms'][3]['RoomNumber']
            RoomNumber75=BatchAdd_RoomType_data['data'][7]['Rooms'][4]['RoomNumber']
            RoomNumber76=BatchAdd_RoomType_data['data'][7]['Rooms'][5]['RoomNumber']
            RoomNumber77=BatchAdd_RoomType_data['data'][7]['Rooms'][6]['RoomNumber']
            RoomNumber78=BatchAdd_RoomType_data['data'][7]['Rooms'][7]['RoomNumber']
            RoomNumber79=BatchAdd_RoomType_data['data'][7]['Rooms'][8]['RoomNumber']
            RoomNumber80=BatchAdd_RoomType_data['data'][7]['Rooms'][9]['RoomNumber']
            
            RoomNumber81=BatchAdd_RoomType_data['data'][8]['Rooms'][0]['RoomNumber']
            RoomNumber82=BatchAdd_RoomType_data['data'][8]['Rooms'][1]['RoomNumber']
            RoomNumber83=BatchAdd_RoomType_data['data'][8]['Rooms'][2]['RoomNumber']            
            RoomNumber84=BatchAdd_RoomType_data['data'][8]['Rooms'][3]['RoomNumber']
            RoomNumber85=BatchAdd_RoomType_data['data'][8]['Rooms'][4]['RoomNumber']
            RoomNumber86=BatchAdd_RoomType_data['data'][8]['Rooms'][5]['RoomNumber']
            RoomNumber87=BatchAdd_RoomType_data['data'][8]['Rooms'][6]['RoomNumber']
            RoomNumber88=BatchAdd_RoomType_data['data'][8]['Rooms'][7]['RoomNumber']
            RoomNumber89=BatchAdd_RoomType_data['data'][8]['Rooms'][8]['RoomNumber']
            RoomNumber90=BatchAdd_RoomType_data['data'][8]['Rooms'][9]['RoomNumber']

            BatchAdd_RoomType={'RoomTypeId1':RoomTypeId1,
                               'RoomTypeId2':RoomTypeId2, 
                               'RoomTypeId3':RoomTypeId3,
                               'RoomTypeId4':RoomTypeId4,
                               'RoomTypeId5':RoomTypeId5,
                               'RoomTypeId6':RoomTypeId6,
                               'RoomTypeId7':RoomTypeId7,
                               'RoomTypeId8':RoomTypeId8,
                               'RoomTypeId9':RoomTypeId9,                                                           
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
                               'RoomNumber20':RoomNumber20,
                               'RoomNumber21':RoomNumber21,
                               'RoomNumber22':RoomNumber22,
                               'RoomNumber23':RoomNumber23, 
                               'RoomNumber24':RoomNumber24, 
                               'RoomNumber25':RoomNumber25, 
                               'RoomNumber26':RoomNumber26, 
                               'RoomNumber27':RoomNumber27, 
                               'RoomNumber28':RoomNumber28, 
                               'RoomNumber29':RoomNumber29, 
                               'RoomNumber30':RoomNumber30, 
                               'RoomNumber31':RoomNumber31, 
                               'RoomNumber32':RoomNumber32, 
                               'RoomNumber33':RoomNumber33, 
                               'RoomNumber34':RoomNumber34, 
                               'RoomNumber35':RoomNumber35, 
                               'RoomNumber36':RoomNumber36, 
                               'RoomNumber37':RoomNumber37, 
                               'RoomNumber38':RoomNumber38, 
                               'RoomNumber39':RoomNumber39, 
                               'RoomNumber40':RoomNumber40, 
                               'RoomNumber41':RoomNumber41, 
                               'RoomNumber42':RoomNumber42, 
                               'RoomNumber43':RoomNumber43, 
                               'RoomNumber44':RoomNumber44, 
                               'RoomNumber45':RoomNumber45, 
                               'RoomNumber46':RoomNumber46, 
                               'RoomNumber47':RoomNumber47, 
                               'RoomNumber48':RoomNumber48, 
                               'RoomNumber49':RoomNumber49, 
                               'RoomNumber50':RoomNumber50, 
                               'RoomNumber51':RoomNumber51, 
                               'RoomNumber52':RoomNumber52, 
                               'RoomNumber53':RoomNumber53, 
                               'RoomNumber54':RoomNumber54, 
                               'RoomNumber55':RoomNumber55, 
                               'RoomNumber56':RoomNumber56, 
                               'RoomNumber57':RoomNumber57, 
                               'RoomNumber58':RoomNumber58, 
                               'RoomNumber59':RoomNumber59, 
                               'RoomNumber60':RoomNumber60, 
                               'RoomNumber61':RoomNumber61, 
                               'RoomNumber62':RoomNumber62, 
                               'RoomNumber63':RoomNumber63, 
                               'RoomNumber64':RoomNumber64, 
                               'RoomNumber65':RoomNumber65, 
                               'RoomNumber66':RoomNumber66, 
                               'RoomNumber67':RoomNumber67, 
                               'RoomNumber68':RoomNumber68, 
                               'RoomNumber69':RoomNumber69, 
                               'RoomNumber70':RoomNumber70, 
                               'RoomNumber71':RoomNumber71, 
                               'RoomNumber72':RoomNumber72, 
                               'RoomNumber73':RoomNumber73, 
                               'RoomNumber74':RoomNumber74, 
                               'RoomNumber75':RoomNumber75, 
                               'RoomNumber76':RoomNumber76, 
                               'RoomNumber77':RoomNumber77, 
                               'RoomNumber78':RoomNumber78, 
                               'RoomNumber79':RoomNumber79, 
                               'RoomNumber80':RoomNumber80, 
                               'RoomNumber81':RoomNumber81, 
                               'RoomNumber82':RoomNumber82, 
                               'RoomNumber83':RoomNumber83, 
                               'RoomNumber84':RoomNumber84, 
                               'RoomNumber85':RoomNumber85, 
                               'RoomNumber86':RoomNumber86, 
                               'RoomNumber87':RoomNumber87, 
                               'RoomNumber88':RoomNumber88, 
                               'RoomNumber89':RoomNumber89,
                               'RoomNumber90':RoomNumber90                                                          
                               }
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
    
# def Check_Out(**self):
#      payload = {
#     "RoomNumbers": [self['RoomNumber']],
#     "InternalRemark": "备注信息",
#     "BillItems": [{
#                 "IsDeposit": False,
#                 "Amount": 200,
#                 "CreditTypeValue": "C9140",
#                 "DebitTypeValue": "D1000",         
#                 "PayState": "0"
#             },
#             {
#                 "Reason": "",
#                 "IsDeposit": False,
#                 "Amount": 0.01,
#                 "CreditTypeValue": "C9140",
#                 "PayState": "0"
#             }]
# }
#                    
#         r = requests.request('PUT', self['url'], headers=Headers ,data=json.dumps(payload))
# 
#         Check_Out_data = json.loads(r.text)
#         businessCode=CommonMoudle(Check_Out_data['businessCode'] ,200)
#         resultCode=CommonMoudle(Check_Out_data['resultCode'] ,200)


    

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
                          
                          RoomTypeName3=RoomTypeName[3],
                          RoomNumber3_1=RoomNumber[21],
                          RoomNumber3_2=RoomNumber[22],
                          RoomNumber3_3=RoomNumber[23],                          
                          RoomNumber3_4=RoomNumber[24],                            
                          RoomNumber3_5=RoomNumber[25],                            
                          RoomNumber3_6=RoomNumber[26],                            
                          RoomNumber3_7=RoomNumber[27],                            
                          RoomNumber3_8=RoomNumber[28],                            
                          RoomNumber3_9=RoomNumber[29],                            
                          RoomNumber3_10=RoomNumber[30],
                          
                          RoomTypeName4=RoomTypeName[4],
                          RoomNumber4_1=RoomNumber[31],
                          RoomNumber4_2=RoomNumber[32],
                          RoomNumber4_3=RoomNumber[33],                          
                          RoomNumber4_4=RoomNumber[34],                            
                          RoomNumber4_5=RoomNumber[35],                            
                          RoomNumber4_6=RoomNumber[36],                            
                          RoomNumber4_7=RoomNumber[37],                            
                          RoomNumber4_8=RoomNumber[38],                            
                          RoomNumber4_9=RoomNumber[39],                            
                          RoomNumber4_10=RoomNumber[40],
                          
                          RoomTypeName5=RoomTypeName[5],
                          RoomNumber5_1=RoomNumber[41],
                          RoomNumber5_2=RoomNumber[42],
                          RoomNumber5_3=RoomNumber[43],                          
                          RoomNumber5_4=RoomNumber[44],                            
                          RoomNumber5_5=RoomNumber[45],                            
                          RoomNumber5_6=RoomNumber[46],                            
                          RoomNumber5_7=RoomNumber[47],                            
                          RoomNumber5_8=RoomNumber[48],                            
                          RoomNumber5_9=RoomNumber[49],                            
                          RoomNumber5_10=RoomNumber[50],
                          
                          RoomTypeName6=RoomTypeName[6],
                          RoomNumber6_1=RoomNumber[51],
                          RoomNumber6_2=RoomNumber[52],
                          RoomNumber6_3=RoomNumber[53],                          
                          RoomNumber6_4=RoomNumber[54],                            
                          RoomNumber6_5=RoomNumber[55],                            
                          RoomNumber6_6=RoomNumber[56],                            
                          RoomNumber6_7=RoomNumber[57],                            
                          RoomNumber6_8=RoomNumber[58],                            
                          RoomNumber6_9=RoomNumber[59],                            
                          RoomNumber6_10=RoomNumber[60],  
                          
                          RoomTypeName7=RoomTypeName[7],
                          RoomNumber7_1=RoomNumber[61],
                          RoomNumber7_2=RoomNumber[62],
                          RoomNumber7_3=RoomNumber[63],                          
                          RoomNumber7_4=RoomNumber[64],                            
                          RoomNumber7_5=RoomNumber[65],                            
                          RoomNumber7_6=RoomNumber[66],                            
                          RoomNumber7_7=RoomNumber[67],                            
                          RoomNumber7_8=RoomNumber[68],                            
                          RoomNumber7_9=RoomNumber[69],                            
                          RoomNumber7_10=RoomNumber[70],
                          
                          RoomTypeName8=RoomTypeName[8],
                          RoomNumber8_1=RoomNumber[71],
                          RoomNumber8_2=RoomNumber[72],
                          RoomNumber8_3=RoomNumber[73],                          
                          RoomNumber8_4=RoomNumber[74],                            
                          RoomNumber8_5=RoomNumber[75],                            
                          RoomNumber8_6=RoomNumber[76],                            
                          RoomNumber8_7=RoomNumber[77],                            
                          RoomNumber8_8=RoomNumber[78],                            
                          RoomNumber8_9=RoomNumber[79],                            
                          RoomNumber8_10=RoomNumber[80],
                          
                          RoomTypeName9=RoomTypeName[9],
                          RoomNumber9_1=RoomNumber[81],
                          RoomNumber9_2=RoomNumber[82],
                          RoomNumber9_3=RoomNumber[83],                          
                          RoomNumber9_4=RoomNumber[84],                            
                          RoomNumber9_5=RoomNumber[85],                            
                          RoomNumber9_6=RoomNumber[86],                            
                          RoomNumber9_7=RoomNumber[87],                            
                          RoomNumber9_8=RoomNumber[88],                            
                          RoomNumber9_9=RoomNumber[89],                            
                          RoomNumber9_10=RoomNumber[90],                                    
                          weekdayPrice='300')
    
    Check_In(url=Check_In_url,
             RoomTypeId=RoomType['RoomTypeId1'],
             RoomNumber=RoomType['RoomNumber1'])
  
    

    

    
    