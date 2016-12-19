# -*- coding: utf-8 -*-
from Config.EB_API_Config import *
from nose.config import flag
from string import lower


def CommonMoudle(name,TotalAmount,length):
    if TotalAmount>=10: 
        if length==10:
            print "%s JSOM_Data is Right.Date:%s"%(name,today)

        else:
            print "%s JSOM_Data is Error.Date:%s"%(name,today)
            return False
    else:
        print "%s JSOM_Data is %s.Date:%s"%(name,TotalAmount,today)
        
def RoomTypeName(RoomTypeName):
    sql="SELECT * FROM iPms.RoomType where RoomTypeName='%s'"%RoomTypeName
#     print sql
    curs = conn.cursor()
    RoomTypeName_Total=curs.execute(sql)
    RoomTypeName_Data=curs.fetchall()
#     print "data:%s"%RoomTypeName_Data
    conn.close()
    for i in RoomTypeName_Data:
        NewRoomTypeid=i['Id']
        return NewRoomTypeid
    
def Time(**self):
    if self['roomTypeId']!='None':
        self['roomTypeId']=RoomTypeName(self['roomTypeId'])
     
        
    parser={'roomTypeId':"&roomTypeId=%s"%self['roomTypeId'],
           'dateTimeType':"&dateTimeType=%s"%self['dateTimeType'],
           'queryDateTimeBegin':"&queryDateTimeBegin=%s"%self['queryDateTimeBegin'],
           'queryDateTimeEnd':"&queryDateTimeEnd=%s"%self['queryDateTimeEnd']}
    
    list=[]
    for key in parser:
        k2=parser[key]
        k3=k2[-4:]
        print k3
        if k3!="None":
            list.append(k2)
    k4=list[0:]
    print k4
    parTmp=""
    for item in k4:
        parTmp=parTmp+item
        
    newurl=self['url']+parTmp
    print newurl
    
    r = requests.request('GET', newurl, headers=Headers)
    All_Name_data = json.loads(r.text)
    TotalAmount=All_Name_data['data']['TotalCount']
    length=len(All_Name_data['data']['Data'])
    CommonMoudle("Search for Orders" , TotalAmount,length)  
    
    SQL_parser={'roomTypeId':" and PhysicalRoomTypeId='%s'"%self['roomTypeId']}   

    SQL_list=[]
    for key in SQL_parser:
        s2=SQL_parser[key]
        s3=s2[-6:]
        print s3
        if s3!="'None'":
            SQL_list.append(s2)
    s4=SQL_list[0:]
    print s4
    sql_parTmp=""
    for item in s4:
        sql_parTmp=sql_parTmp+item
    print sql_parTmp
    
    old_sql="select * from iPmsBiz.`Occupation` where ownerId='%s'"%self['storeid']
    
    if self['dateTimeType']==1:
        old_sql="select * from iPmsBiz.`Occupation` where ownerId='%s' and EstimatedDepartureTime between '%s' and '%s'"%(self['storeid'],self['queryDateTimeBegin'],self['queryDateTimeEnd'])
    else:
        old_sql="select * from iPmsBiz.`Occupation` where ownerId='%s' and EstimatedArriveTime between '%s' and '%s'"%(self['storeid'],self['queryDateTimeBegin'],self['queryDateTimeEnd'])
        
        
    sql= old_sql + sql_parTmp
    print sql
    curs = conn.cursor()
    All_Name_Total=curs.execute(sql)
    All_Name_Total_Data=curs.fetchall()
#     print "data:%s"%All_Name_Total


    print TotalAmount
    print All_Name_Total
    
    if TotalAmount==All_Name_Total:
        print "Search for By orders Amount is Right. Date:%s"%today  
    else:
        print "Search for By orders Amount is Error. Date:%s"%today
    


# def Name(url,storeid,name=None,iphone=None,orgId=None,order=None,status=None,dateTimeType=None,queryDateTimeBegin=None,queryDateTimeEnd=None):
def Name(**self):
    

        
    parser={'CustomerName':"&CustomerName=%s"%self['name'],
            'mobile':"&mobile=%s"%self['iphone'],
            'OrgId':"&OrgId=%s"%self['OrgId'],
            'order':"&order=%s"%self['order'],
            'status':"&status=%s"%self['status']}

        

    list=[]
    for key in parser:
        k2=parser[key]
        k3=k2[-4:]
        print k3
        if k3!="None":
            list.append(k2)
    k4=list[0:]
    print k4
    parTmp=""
    for item in k4:
        parTmp=parTmp+item
        
    newurl=self['url']+parTmp
    print newurl  
     
    r = requests.request('GET', newurl, headers=Headers)
    All_Name_data = json.loads(r.text)
    TotalAmount=All_Name_data['data']['TotalCount']
    length=len(All_Name_data['data']['Data'])
    CommonMoudle("Search for By Name orders" , TotalAmount,length)
    
    SQL_parser={'MainliaisonName':" and MainliaisonName='%s'"%self['name'],
                'MainliaisonMobile':" and MainliaisonMobile='%s'"%self['iphone'],
                'OrgId':" and OrgId='%s'"%self['OrgId'],
                'OrderStatus':" and OrderStatus='%s'"%self['status'],
                'OrderId':" and OrderId='%s'"%self['order']}   

    SQL_list=[]
    for key in SQL_parser:
        s2=SQL_parser[key]
        s3=s2[-6:]
        print s3
        if s3!="'None'":
            SQL_list.append(s2)
    s4=SQL_list[0:]
    print s4
    sql_parTmp=""
    for item in s4:
        sql_parTmp=sql_parTmp+item
    print sql_parTmp
    
    old_sql="select * from iPmsBiz.`Order` where ownerId='%s'"%self['storeid']
    sql= old_sql + sql_parTmp
          
    print sql
    curs = conn.cursor()
    All_Name_Total=curs.execute(sql)
    All_Name_Total_Data=curs.fetchall()

#     conn.close()
    print TotalAmount
    print All_Name_Total
    
    if TotalAmount==All_Name_Total:
        print "Search for By orders Amount is Right. Date:%s"%today
    else:
        print "Search for By orders Amount is Error. Date:%s"%today

        
def verify(value):
    print value
    if value=='':
        newvalue={'Newvalue':"None"}
        return newvalue
    else:
        newvalue={'Newvalue':value}
        return newvalue
    
def All_Store(**self):
    print self
    r = requests.request('GET', self['url'], headers=Headers)
    All_Store_data = json.loads(r.text)
    TotalAmount=All_Store_data['data']['TotalCount']
    length=len(All_Store_data['data']['Data'])
    CommonMoudle("Search for By All Store orders" , TotalAmount,length)        
#     print "Data:%s"%Data
#     print "json:%s"%TotalAmount    
    sql=("select * from iPmsBiz.`Order` where ownerId=%s;")%(self['storeid'])
    curs = conn.cursor()
    All_Store_Total=curs.execute(sql)
#     print "data:%s"%All_Store_Total
    All_Store_Total_Data=curs.fetchall()
#     conn.close()
    
    if TotalAmount==All_Store_Total:
        print "Search for By All Store orders is Pass.Date:%s"%today
        for i in All_Store_Total_Data:
            print i
            name=verify(value=i['MainLiaisonName'])  
            iphone=verify(value=i['MainLiaisonMobile'])
            OrgId=verify(value=i['OrgId'])
            order=verify(value=i['OrderId'])
            status=verify(value=i['OrderStatus'])
            
            print name,iphone,OrgId,order,status
            q={'name':name['Newvalue'],
               'iphone':iphone['Newvalue'],
               'OrgId':OrgId['Newvalue'],
               'order':order['Newvalue'],
               'status':status['Newvalue'],
               'result':True}
            print dict(q)
            return dict(q)
    else:
        print "Search for By All Store orders is Failed.Json:%s,Data:%s,Date:%s"%(TotalAmount,All_Store_Total,today)
        for i in All_Store_Total_Data:
            print i
            name=verify(value=i['MainLiaisonName'])  
            iphone=verify(value=i['MainLiaisonMobile'])
            OrgId=verify(value=i['OrgId'])
            order=verify(value=i['OrderId'])
            status=verify(value=i['OrderStatus'])
            
            q={'name':name['Newvalue'],
               'iphone':iphone['Newvalue'],
               'OrgId':OrgId['Newvalue'],
               'order':order['Newvalue'],
               'status':status['Newvalue'],
               'result':False}
            print dict(q)
            return dict(q)
    
  
    

if __name__ == "__main__":
    Order_Detail=All_Store(storeid=Headers['ownerid'],url=PO_Search_url)

    Name(url=PO_Search_url, 
         storeid=Headers['ownerid'],
         iphone="None",
         name='房客',
         OrgId='None',
         order='None',
         status='None')
    
    Time(url=PO_Search_url,
         storeid=Headers['ownerid'],
         roomTypeId='None',
         dateTimeType='0',
         queryDateTimeBegin='2016-12-12',
         queryDateTimeEnd='2016-12-13'
         )
    
    