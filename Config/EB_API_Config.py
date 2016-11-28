import requests
import json
import random
import logging
import datetime
import time


today = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

Server='http://testwww.51pms.net'

Port='8001'

Add_RoomType_API             ='/api/rooms/RoomType/'

Del_RoomType_API              ='/api/rooms/RoomType/'

Search_All_RoomType_API   ='/api/rooms/RoomTypes/'

Modify_RoomType_API       ='/api/rooms/RoomType/'

Add_RoomType_url              = Server+":"+Port+Add_RoomType_API

Search_All_RoomType_url     = Server+":"+Port+Search_All_RoomType_API

Del_RoomType_url                = Server+":"+Port+Del_RoomType_API

Modify_RoomType_url          = Server+":"+Port+Modify_RoomType_API

Room ={'RoomTypeName':random.getrandbits(20),'RoomNumber':random.getrandbits(20),'NewRoomTypeName':random.getrandbits(30)}

Headers={'Content-Type':'application/json','ownerid':'434265567985665','orgid':'434265567985667'}
