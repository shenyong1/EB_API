from Config.EB_API_Config import *

def CommonMoudle(Path,data):
    if Path==data:
        return True
    else:
        return False

def Modify_RoomType(url,RoomTypeName,RoomTypeId,weekdayPrice,RoomNumber1,RoomID,IsActive1):
        payload = {
                    "Id": RoomTypeId,
                    "RoomTypeName": RoomTypeName,
                    "weekdayPrice": weekdayPrice,
                    "IsActive": True,
                    "Rooms": [
            {
                "Id":RoomID,
                "RoomNumber": RoomNumber1,
                "IsActive": IsActive1
            }
        ]
        }
                   
        r = requests.request('PUT', url, headers=Headers ,data=json.dumps(payload))

        Modify_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(Modify_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(Modify_RoomType_data['resultCode'] ,200)
        NewRoomTypeName=Modify_RoomType_data['data']['RoomTypeName']
        NewIsActive=Modify_RoomType_data['data']['Rooms'][0]['IsActive']
        weekdayPrice=Modify_RoomType_data['data']['weekdayPrice']        
        RoomNumber=Modify_RoomType_data['data']['Rooms'][0]['RoomNumber']
        RoomTypeId=Modify_RoomType_data['data']['Rooms'][0]['RoomTypeId']   
         
        if businessCode & resultCode ==True:
            if weekdayPrice==999 and NewRoomTypeName==str(RoomTypeName) and NewIsActive==False:
                print "Modify_RoomType is Pass. Date:%s"%today
                return True
            else:
                print "Modify_RoomType is Failed. Date:%s"%today
                return False
        else:
            print "Modify_RoomType is Failed. Date:%s"%today
            return False            

def Del_RoomType(url,RoomTypeID):
    r = requests.request('DELETE', url+RoomTypeID, headers=Headers)
    Del_RoomType_data = json.loads(r.text)
    businessCode=CommonMoudle(Del_RoomType_data['businessCode'] ,200)
    resultCode=CommonMoudle(Del_RoomType_data['resultCode'] ,200) 
    
    
    if businessCode & resultCode ==True:
        print "Del_RoomType is Pass. Date:%s"%today
        return True
    else:
        print "Del_RoomType is Failed. Date:%s"%today
        return False        

def Add_RoomType(url,RoomTypeName,RoomNumber,weekdayPrice=300):
        payload = {
                   "RoomTypeName": RoomTypeName,
                   "weekdayPrice": weekdayPrice,
                   "IsActive": True,
                   "Rooms": [
                    {
                    "RoomNumber": RoomNumber,
                    "IsActive": True
                    }
                             ]


                             }
        r = requests.request('POST', url, headers=Headers ,data=json.dumps(payload))

        Add_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(Add_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(Add_RoomType_data['resultCode'] ,200) 
        
        if businessCode & resultCode ==True:
            print "Add_RoomType is Pass. Date:%s"%today   
            RoomTypeName=Add_RoomType_data['data']['RoomTypeName']
            RoomNumber=Add_RoomType_data['data']['Rooms'][0]['RoomNumber']
            RoomTypeId=Add_RoomType_data['data']['Rooms'][0]['RoomTypeId']
            RoomID=Add_RoomType_data['data']['Rooms'][0]['Id']
            return (RoomTypeName,RoomNumber,RoomTypeId,RoomID,True)
        else:
            print "Add_RoomType is Failed. Date:%s"%today
            return False


def Search_All_RoomType(url,RoomTypeName=None,RoomNumber=None):
    r = requests.request('GET', url, headers=Headers)
    All_RoomType_data = json.loads(r.text)

        
    if  RoomTypeName is None and RoomNumber is None:
        businessCode=CommonMoudle(All_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(All_RoomType_data['resultCode'] ,200)
        if businessCode==True and resultCode==True:
            print "Search_All_RoomType is Pass. Date:%s"%today
            return True
        else:
            print "Search_All_RoomType is Failed!!. Date:%s"%today
            return False                               

    else:
        for v in All_RoomType_data['data']:
            i=v
            if i['RoomTypeName']==RoomTypeName:
                for v in i['Rooms']:
                    if v['RoomNumber']==RoomNumber:
                        print "Add_RoomType is Pass In Search_All_RoomType!. Date:%s"%today
                        return True
                    else:
                        print "Add_RoomType is Failed In Search_All_RoomType!. Date:%s"%today 
                        return False
        else:
            print "Add_RoomType is Failed In Search_All_RoomType!!. Date:%s"%today 
            return False
                      
if __name__ == "__main__":
    RoomID=Add_RoomType(Add_RoomType_url,Room['RoomTypeName'],Room['RoomNumber'])
    Del_RoomType(Del_RoomType_url, RoomID[2])

    Search_All_RoomType(Search_All_RoomType_url,RoomID[0],RoomID[1])
#     Modify_RoomType(Modify_RoomType_url,Room['NewRoomTypeName'],RoomID[2],999,RoomID[1],RoomID[3],False)




    
    
    
    
    