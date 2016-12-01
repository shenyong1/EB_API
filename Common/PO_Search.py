from Config.EB_API_Config import *
from nose.config import flag


def CommonMoudle(name,TotalAmount,length):
    if TotalAmount>=10: 
        if length==10:
            print "%s JSOM_Data is Right."%name

        else:
            print "%s JSOM_Data is Error."%name
            return False

def Name(url,storeid,name):
    CustomerName="&CustomerName=%s"%name
    r = requests.request('GET', url+CustomerName, headers=Headers)
    All_Name_data = json.loads(r.text)
    TotalAmount=All_Name_data['data']['TotalCount']
    length=len(All_Name_data['data']['Data'])
    CommonMoudle("Search for all Name orders" , TotalAmount,length)

#     print "json:%s"%TotalAmount    
    sql=("select * from iPmsBiz.`Order` where ownerId=%s and MainliaisonName='%s';")%(storeid,name)
    curs = conn.cursor()
    All_Name_Total=curs.execute(sql)
#     print "data:%s"%All_Name_Total

    conn.close()
    
    if TotalAmount==All_Name_Total:
        print "Search for Name orders is Pass."  
        return True
    else:
        print "Search for Name orders is Failed."  
        return False

    
def All_Store(url,storeid):
    r = requests.request('GET', url, headers=Headers)
    All_Store_data = json.loads(r.text)
    TotalAmount=All_Store_data['data']['TotalCount']
    length=len(All_Store_data['data']['Data'])
    CommonMoudle("Search for all store orders" , TotalAmount,length)


        
#     print "Data:%s"%Data
#     print "json:%s"%TotalAmount    
    sql=("select * from iPmsBiz.`Order` where ownerId=%s;")%storeid
    curs = conn.cursor()
    All_Store_Total=curs.execute(sql)
#     print "data:%s"%All_Store_Total
    All_Store_Total_Data=curs.fetchall()
#     conn.close()
    
    if TotalAmount==All_Store_Total:
        print "Search for all store orders is Pass."
        for i in All_Store_Total_Data:
            name=i['MainLiaisonName']    
            return name,True
    else:
        print "Search for all store orders is Failed."
        for i in All_Store_Total_Data:
            name=i['MainLiaisonName']    
            return name,False
    
  
    

if __name__ == "__main__":
    Order_Detail=All_Store(PO_Search_url,Headers['ownerid'])
    Name(PO_Search_url, Headers['ownerid'],Order_Detail[0])
    
    