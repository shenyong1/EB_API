from Config.EB_API_Config import *
from nose.config import flag


def CommonMoudle(name,TotalAmount,length):
    if TotalAmount>=10: 
        if length==10:
            print "%s JSOM_Data is Right.Date:%s"%(name,today)

        else:
            print "%s JSOM_Data is Error.Date:%s"%(name,today)
            return False
    else:
        print "%s JSOM_Data is %s.Date:%s"%(name,TotalAmount,today)

def Name(url,storeid,name):
    CustomerName="&CustomerName=%s"%name
    r = requests.request('GET', url+CustomerName, headers=Headers)
    All_Name_data = json.loads(r.text)
    TotalAmount=All_Name_data['data']['TotalCount']
    length=len(All_Name_data['data']['Data'])
    CommonMoudle("Search for By Name orders" , TotalAmount,length)

#     print "json:%s"%TotalAmount    
    sql=("select * from iPmsBiz.`Order` where ownerId=%s and MainliaisonName='%s';")%(storeid,name)
    curs = conn.cursor()
    All_Name_Total=curs.execute(sql)
    All_Name_Total_Data=curs.fetchall()
#     print "data:%s"%All_Name_Total

    conn.close()
    
    if TotalAmount==All_Name_Total:
        print "Search for By Name orders Amount is Right. Date:%s"%today
        for i in All_Name_Total_Data:
            MainLiaisonName=i['MainLiaisonName']
            if MainLiaisonName==name:
                print "Search for By Name's %s orders is Pass. Date:%s"%(MainLiaisonName,today) 
                return True
            else:
                print "Search for By Name's %s orders is Failed. Json:%s,Data:%s,Date:%s"%(MainLiaisonName,TotalAmount,All_Name_Total,today)  
                return False
    else:
        print "Search for By Name orders Amount is Error. Date:%s"%today

        

    
def All_Store(url,storeid):
    r = requests.request('GET', url, headers=Headers)
    All_Store_data = json.loads(r.text)
    TotalAmount=All_Store_data['data']['TotalCount']
    length=len(All_Store_data['data']['Data'])
    CommonMoudle("Search for By All Store orders" , TotalAmount,length)        
#     print "Data:%s"%Data
#     print "json:%s"%TotalAmount    
    sql=("select * from iPmsBiz.`Order` where ownerId=%s;")%storeid
    curs = conn.cursor()
    All_Store_Total=curs.execute(sql)
#     print "data:%s"%All_Store_Total
    All_Store_Total_Data=curs.fetchall()
#     conn.close()
    
    if TotalAmount==All_Store_Total:
        print "Search for By All Store orders is Pass.Date:%s"%today
        for i in All_Store_Total_Data:
            name=i['MainLiaisonName']    
            return name,True
    else:
        print "Search for By All Store orders is Failed.Json:%s,Data:%s,Date:%s"%(TotalAmount,All_Store_Total,today)
        for i in All_Store_Total_Data:
            name=i['MainLiaisonName']    
            return name,False
    
  
    

if __name__ == "__main__":
    Order_Detail=All_Store(PO_Search_url,Headers['ownerid'])
    Name(PO_Search_url, Headers['ownerid'],Order_Detail[0])
    
    