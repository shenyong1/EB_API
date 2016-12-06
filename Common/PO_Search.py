from Config.EB_API_Config import *
from nose.config import flag
from _mysql import NULL



def CommonMoudle(name,TotalAmount,length):
    if TotalAmount>=10: 
        if length==10:
            print "%s JSOM_Data is Right.Date:%s"%(name,today)

        else:
            print "%s JSOM_Data is Error.Date:%s"%(name,today)
            return False
    else:
        print "%s JSOM_Data is %s.Date:%s"%(name,TotalAmount,today)


# def Name(url,storeid,name=None,iphone=None,orgId=None,roomTypeId=None,order=None,status=None,dateTimeType=None,queryDateTimeBegin=None,queryDateTimeEnd=None):
def Name(**self):
#     alist=[]
#     for key in self:
#         s1=self[key]
#         if s1!='':
#             alist.append(s1)
#     s2=alist[0:]
#     print s2
            
    

#     CustomerName="&CustomerName=%s"%name
    mobile="&mobile=%s"%self['iphone']
#     otaOrderId="&otaOrderId=%s"%self['order']
#     statusKey="&statusKey=%s"%self['status']
    parser={'CustomerName':"&CustomerName=%s"%self['name'],'mobile':"&mobile=%s"%self['iphone']}
    SQL_parser={'MainliaisonName':"MainliaisonName='%s'"%self['name'],'MainliaisonMobile':"and MainliaisonMobile='%s'"%self['iphone']}
    list=[]
    for key in parser:
        k2=parser[key]
        k3=k2[-4:]
        print k3
        if k3!="None":
            list.append(k2)
    k4=list[0:]
    print k4
    if len(k4)==1:
        newurl=self['url']+k4[0]
        print newurl
    if len(k4)==2:
        newurl=self['url']+k4[0]+k4[1]
        print newurl
    if len(k4)==3:
        newurl=self['url']+k4[0]+k4[1]+k4[2]
        print newurl
    if len(k4)==4:
        newurl=self['url']+k4[0]+k4[1]+k4[2]+k4[3]
        print newurl
    if len(k4)==5:
        newurl=self['url']+k4[0]+k4[1]+k4[2]+k4[3]+k4[4]
        print newurl
    if len(k4)==6:
        newurl=self['url']+k4[0]+k4[1]+k4[2]+k4[3]+k4[4]+k4[5]
        print newurl
    if len(k4)==7:
        newurl=self['url']+k4[0]+k4[1]+k4[2]+k4[3]+k4[4]+k4[5]+k4[6]
        print newurl
        

    r = requests.request('GET', newurl, headers=Headers)
    All_Name_data = json.loads(r.text)
    TotalAmount=All_Name_data['data']['TotalCount']
    length=len(All_Name_data['data']['Data'])
    CommonMoudle("Search for By Name orders" , TotalAmount,length)
    
             
    sql=("select * from iPmsBiz.`Order` where ownerId=%s and MainliaisonName='%s';")%(self['storeid'],self['name'])
    curs = conn.cursor()
    All_Name_Total=curs.execute(sql)
    All_Name_Total_Data=curs.fetchall()
#     print "data:%s"%All_Name_Total

    conn.close()
    
    if TotalAmount==All_Name_Total:
        print "Search for By Name orders Amount is Right. Date:%s"%today
        for i in All_Name_Total_Data:
            MainLiaisonName=i['MainLiaisonName']
            if MainLiaisonName==self['name']:
                print "Search for By Name's %s orders is Pass. Date:%s"%(MainLiaisonName,today) 
                return True
            else:
                print "Search for By Name's %s orders is Failed. Json:%s,Data:%s,Date:%s"%(MainLiaisonName,TotalAmount,All_Name_Total,today)  
                return False
    else:
        print "Search for By Name orders Amount is Error. Date:%s"%today

        
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
            verify(value=i['MainLiaisonName'])  
            verify(value=i['MainLiaisonMobile'])
            q={'name':verify['Newvalue'],'iphone':verify['Newvalue'],'result':True}
            print dict(q)
            return dict(q)
    else:
        print "Search for By All Store orders is Failed.Json:%s,Data:%s,Date:%s"%(TotalAmount,All_Store_Total,today)
        for i in All_Store_Total_Data:
            name=verify(value=i['MainLiaisonName'])  
            iphone=verify(value=i['MainLiaisonMobile'])
            print name,iphone
            q={'name':name['Newvalue'],'iphone':iphone['Newvalue'],'result':False}
            print dict(q)
            return dict(q)
    
  
    

if __name__ == "__main__":
    Order_Detail=All_Store(storeid=Headers['ownerid'],url=PO_Search_url)

    Name(url=PO_Search_url, storeid=Headers['ownerid'],name=Order_Detail['name'],iphone=Order_Detail['iphone'])
    
    