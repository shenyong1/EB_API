import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import string
import requests
from random import choice

import tablib
from nose.config import flag
from openpyxl import Workbook, load_workbook
from openpyxl.styles import *
from openpyxl.utils import get_column_letter
from openpyxl.writer.excel import ExcelWriter

from _ast import Return
from _mysql import result
from Config.EB_API_Config import *



def GetNumber(length=8, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

def CommonMoudle(Path, data):
    if Path == data:
        return True
    else:
        return False

#def Modify_RoomType(url,RoomTypeName,RoomTypeId,weekdayPrice,RoomNumber1,RoomID,IsActive1):
def Modify_RoomType(**self):
    payload = {"Id": self['RoomTypeId'], 
               "RoomTypeName": self['RoomTypeName'],
               "weekdayPrice": self['weekdayPrice'],
               "IsActive": True,
               "Rooms": [
            {
                "Id":self['RoomID'],
                "RoomNumber": self['RoomNumber'],
                "IsActive": self['IsActive']
            }
        ]
        }
    r = requests.request('PUT', self['url'], headers=Headers, data=json.dumps(payload))
    Modify_RoomType_data = json.loads(r.text)
    businessCode = CommonMoudle(Modify_RoomType_data['businessCode'] , 200)
    resultCode = CommonMoudle(Modify_RoomType_data['resultCode'], 200)
    if businessCode & resultCode == True:
            NewRoomTypeName = Modify_RoomType_data['data']['RoomTypeName']
            NewIsActive = Modify_RoomType_data['data']['Rooms'][0]['IsActive']
            weekdayPrice = Modify_RoomType_data['data']['weekdayPrice']        
            RoomNumber = Modify_RoomType_data['data']['Rooms'][0]['RoomNumber']
            RoomTypeId = Modify_RoomType_data['data']['Rooms'][0]['RoomTypeId'] 
            if weekdayPrice == 999 and NewRoomTypeName==str(self['RoomTypeName']) and NewIsActive==False:
                print "Modify_RoomType is Pass. Date:%s"%today
                Save(name="Modify_RoomType",
                     businessCode=Modify_RoomType_data['businessCode'],
                     resultCode=Modify_RoomType_data['resultCode'],
                     Message=Modify_RoomType_data['Message'],
                     result="Pass",
                     CaseNumber=self['CaseNumber'])
                Modify_RoomType={'Result':True}
                return Modify_RoomType
            else:
                print "Modify_RoomType is Failed. Date:%s"%today
                Save(name="Modify_RoomType",
                     businessCode=Modify_RoomType_data['businessCode'],
                     resultCode=Modify_RoomType_data['resultCode'],
                     Message=Modify_RoomType_data['Message'],
                     result="Failed",
                     CaseNumber=self['CaseNumber'])
                Modify_RoomType={'Result':False}
                return Modify_RoomType
    else:
            print "Modify_RoomType is Failed. Date:%s"%today
            Save(data=Modify_RoomType_data,
                 name="Modify_RoomType",
                 businessCode=Modify_RoomType_data['businessCode'],
                 resultCode=Modify_RoomType_data['resultCode'],
                 Message=Modify_RoomType_data['Message'],
                 CaseNumber=self['CaseNumber'],
                 result="Failed")
            Modify_RoomType={'Result':False}
            return Modify_RoomType         

def Del_RoomType(**self):
    r = requests.request('DELETE', self['url']+self['RoomTypeId'], headers=Headers)
    Del_RoomType_data = json.loads(r.text)
    businessCode=CommonMoudle(Del_RoomType_data['businessCode'] ,200)
    resultCode=CommonMoudle(Del_RoomType_data['resultCode'] ,200) 
    
    
    if businessCode & resultCode ==True:
        print "Del_RoomType is Pass. Date:%s"%today
        Save(name="Del_RoomType",
             businessCode=Del_RoomType_data['businessCode'],
             resultCode=Del_RoomType_data['resultCode'],
             Message=Del_RoomType_data['Message'],
             result="Pass",
             CaseNumber=self['CaseNumber'])
        Del_RoomType={'Result':True}
        return Del_RoomType
    else:
        print "Del_RoomType is Failed. Date:%s"%today
        Save(name="Del_RoomType",
             businessCode=Del_RoomType_data['businessCode'],
             resultCode=Del_RoomType_data['resultCode'],
             Message=Del_RoomType_data['Message'],
             result="Failed",
             CaseNumber=self['CaseNumber'])
        Del_RoomType={'Result':False}
        return Del_RoomType   

def Add_RoomType(**self):
        payload = {
                   "RoomTypeName": self['RoomTypeName'],
                   "weekdayPrice": self['weekdayPrice'],
                   "IsActive": True,
                   "Rooms": [
                    {
                    "RoomNumber": self['RoomNumber'],
                    "IsActive": True
                    }
                             ]


                             }
        r = requests.request('POST',
                              self['url'], 
                              headers=Headers ,
                              data=json.dumps(payload))

        Add_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(Add_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(Add_RoomType_data['resultCode'] ,200) 
        Message=Add_RoomType_data['Message']
        
        if businessCode & resultCode ==True:
            print "Add_RoomType is Pass. Message:%s Date:%s"%(Message,today)  
            RoomTypeName=Add_RoomType_data['data']['RoomTypeName']
            RoomNumber=Add_RoomType_data['data']['Rooms'][0]['RoomNumber']
            RoomTypeId=Add_RoomType_data['data']['Rooms'][0]['RoomTypeId']
            RoomID=Add_RoomType_data['data']['Rooms'][0]['Id']
            
            Save(name="Add_RoomType",
                 businessCode=Add_RoomType_data['businessCode'],
                 resultCode=Add_RoomType_data['resultCode'],
                 Message=Add_RoomType_data['Message'],
                 result="Pass",
                 CaseNumber=self['CaseNumber'])
            RoomType={'RoomTypeName':RoomTypeName,
               'RoomNumber':RoomNumber,
               'RoomTypeId':RoomTypeId,
               'RoomID':RoomID,
               'Result':True}
            return RoomType

        else:
            print "Add_RoomType is Failed. Message:%s Date:%s"%(Message,today)
            Save(name="Add_RoomType",
                 businessCode=Add_RoomType_data['businessCode'],
                 resultCode=Add_RoomType_data['resultCode'],
                 Message=Add_RoomType_data['Message'],
                 result="Failed",
                 CaseNumber=self['CaseNumber'])
            RoomType={'Result':False}
            return RoomType

def Search_RoomType(**self):
    r = requests.request('GET', self['url'], headers=Headers)
    All_RoomType_data = json.loads(r.text)
    

    for v in All_RoomType_data['data']:
        i=v
        if i['RoomTypeName']==self['RoomTypeName']:
            Message="Add_RoomType is Pass In Search_RoomType!. Date:%s"%today
            Lastresult="Pass"
            break        
        else:
            Message="Add_RoomType is Failed In Search_RoomType!. Date:%s"%today
            Lastresult="Failed"
    print Message
    Save(name="Search_All_RoomType",
         businessCode=All_RoomType_data['businessCode'],
        resultCode=All_RoomType_data['resultCode'],
        Message='',
        result=Lastresult,
        CaseNumber=self['CaseNumber'])
        
    sql=("SELECT * FROM iPms.RoomType where id = '%s' and IsActive = 1;")%self['RoomTypeId']
    curs = conn.cursor()
    RoomTypeTotal=curs.execute(sql)
    All_RoomType_Total_Data=curs.fetchall()
    conn.close()
    
    if RoomTypeTotal==1:
        print "Data:RoomType TotalAmount is Right"
#         Save(data=RoomTypeTotal,name="Search_All_RoomType_Total",result="Pass")
        Search_RoomType={'Result':True}
        return Search_RoomType
    else:
        print "Data:RoomType TotalAmount is Error"
#         Save(data=RoomTypeTotal,name="Search_All_RoomType_Total",result="Failed")
        Search_RoomType={'Result':False}
        return Search_RoomType
        
def RoomType_Status(**self):
    if self['RoomTypeId']==None:
        print "RooMTypeID is None Date:%s"%today
        RoomType_Status={'Result':False}
        return RoomType_Status
    else:
        r = requests.request('GET', self['url']+self['RoomTypeId'], headers=Headers)
        RoomType_Status_data = json.loads(r.text)

        Status=CommonMoudle(RoomType_Status_data['data'] ,True)
        if Status==True:
            print "RoomType_Status is True. Date:%s"%today
            Save(name="RoomType_Status",
                 businessCode=RoomType_Status_data['businessCode'],
                 resultCode=RoomType_Status_data['resultCode'],
                 Message=RoomType_Status_data['data'],                 
                 result="Pass",
                 CaseNumber=self['CaseNumber'])
            RoomType_Status={'Result':True}
            return RoomType_Status
        elif Status==False:
            print "RoomType_Status is False. Date:%s"%today
            Save(name="RoomType_Status",
                 businessCode=RoomType_Status_data['businessCode'],
                 resultCode=RoomType_Status_data['resultCode'],
                 Message=RoomType_Status_data['data'],                 
                 result="Failed",
                 CaseNumber=self['CaseNumber']
                 )
            RoomType_Status={'Result':True}
            return RoomType_Status
        else:
            print "RoomType_Status is failed. Date:%s"%today
            Save(name="RoomType_Status",
                 businessCode=RoomType_Status_data['businessCode'],
                 resultCode=RoomType_Status_data['resultCode'],
                 Message=RoomType_Status_data['data'],                 
                 result="Failed",
                 CaseNumber=self['CaseNumber'])
            RoomType_Status={'Result':False}
            return RoomType_Status

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
            }
        ]
        }]
        
                   
        r = requests.request('POST', self['url'], headers=Headers ,data=json.dumps(payload))
        T=r.elapsed.microseconds/1000

        BatchAdd_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(BatchAdd_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(BatchAdd_RoomType_data['resultCode'] ,200)
        Message=BatchAdd_RoomType_data['Message']

         
        if businessCode & resultCode ==True and T<300:
            print "BatchAdd_RoomType is Pass. Message:%s Date:%s Time:%s"%(Message,today,T)             
            Save(name="BatchAdd_RoomType",
                 businessCode=BatchAdd_RoomType_data['businessCode'],
                 resultCode=BatchAdd_RoomType_data['resultCode'],
                 Message=BatchAdd_RoomType_data['Message'],
                 result="Pass",
                 CaseNumber=self['CaseNumber'])
            BatchAdd_RoomType={'Result':True}
            return BatchAdd_RoomType

        else:
            print "BatchAdd_RoomType is Failed. Message:%s Date:%s Time:%s"%(Message,today,T)
            Save(name="BatchAdd_RoomType",
                 businessCode=BatchAdd_RoomType_data['businessCode'],
                 resultCode=BatchAdd_RoomType_data['resultCode'],
                 Message=BatchAdd_RoomType_data['Message'],
                 result="Failed",
                 CaseNumber=self['CaseNumber'])
            BatchAdd_RoomType={'Result':False}
            return BatchAdd_RoomType       

        
def Save(**self):
    ft = Font(name='Arial Unicode MS',
    size=11,
    bold=False,
    italic=False,
    vertAlign=None,
    underline='none',
    strike=False,
    color='FF000000')

    D={'name':self['name'],
       'result':self['result'],
       'businessCode':self['businessCode'],
       'resultCode':self['resultCode'],
       'Message':self['Message'],
       'CaseNumber':self['CaseNumber']}
    wb = Workbook()
    ws = wb.active

#     ws.append((D['name'],D['result']))
#     print D['result']
#     wb.save("D:\EB_API\TestReport\TestReport.xlsx")
    ws['A1'].font = 'Date'
    ws['B1'].font = 'API Name'
    ws['C1'].font = 'Result'
    wb = load_workbook(filename=u'D:\EB_API\TestReport\TestReport.xlsx')

 
 
    SheetNames = wb.sheetnames

 
 
    ws = wb.get_sheet_by_name(SheetNames[0])
 
 
    rows = ws.max_row
    cols = ws.max_column
    for i in range(1,rows+1):
        for l in range(1,cols+1):
            col = get_column_letter(l)
#             print ws.cell('%s%s'%(col,i)).value
            
 
    ws.append((D['CaseNumber'],FileName,D['name'],D['businessCode'],D['resultCode'],D['Message'],D['result']))
    wb.save('D:\EB_API\TestReport\TestReport.xlsx')

        
                                   
if __name__ == "__main__":
    RoomTypeName=GetNumber(8)
    RoomTypeName1=GetNumber(8)
    RoomTypeName2=GetNumber(8)  
      
    RoomNumber=GetNumber(10)
    RoomNumber1=GetNumber(10)
    RoomNumber2=GetNumber(10)
    RoomNumber3=GetNumber(10)
    RoomNumber4=GetNumber(10)
    
    NewRoomTypeName=GetNumber(9)
    
    RoomType=Add_RoomType(CaseNumber='TCS_001',
                          url=RoomType_API_url,
                          RoomTypeName=RoomTypeName,
                          RoomNumber=RoomNumber,
                          weekdayPrice='300')
# 
#      
#     RoomType_Status(url=RoomType_Status_url,
#                     RoomTypeId=RoomType['RoomTypeId'],
#                     CaseNumber='TCS_001')
# 
# #def Modify_RoomType(url,RoomTypeName,RoomTypeId,weekdayPrice,RoomNumber1,RoomID,IsActive1):
#     

#     Modify_RoomType(
#                     CaseNumber='TCS_001',
#                     url=RoomType_API_url,
#                     RoomTypeName=NewRoomTypeName,
#                     RoomTypeId=RoomType['RoomTypeId'],
#                     weekdayPrice=999,
#                     RoomNumber=RoomType['RoomNumber'],
#                     RoomID=RoomType['RoomID'],
#                     IsActive=False)
#        
#     Del_RoomType(url=RoomType_API_url, RoomTypeId=RoomType['RoomTypeId']) 
#          
#     RoomType_Status(CaseNumber='TCS_001',
#                     url=RoomType_Status_url,
#                     RoomTypeId=RoomType['RoomTypeId'])
#      
    Search_RoomType(CaseNumber='TCS_001',
                    url=Search_RoomType_url,
                    RoomTypeName=RoomType['RoomTypeName'],
                    RoomNumber=RoomType['RoomNumber'],
                    RoomTypeId=RoomType['RoomTypeId'])
    
#     RoomType=BatchAdd_RoomType(CaseNumber='TCS_001',
#                           url=Search_RoomType_url,
#                           RoomTypeName1=RoomTypeName1,
#                           OTARoomTypeName='Test',
#                           OTARoomTypeId='Z23582JSC',
#                           RoomNumber1_1=RoomNumber1,
#                           RoomNumber1_2=RoomNumber2,
#                           RoomTypeName2=RoomTypeName2,
#                           RoomNumber2_1=RoomNumber3,
#                           RoomNumber2_2=RoomNumber4,
#                           weekdayPrice='300')
