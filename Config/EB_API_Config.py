import requests
import json
import random
import logging
import datetime
import time
import MySQLdb
import MySQLdb.cursors
from Common.PO_Search import *

Room ={'RoomTypeName':random.getrandbits(20),
       'RoomNumber':random.getrandbits(20),
       'NewRoomTypeName':random.getrandbits(30)}

Headers={'Content-Type':'application/json',
         'ownerid':'434265567985665',
         'orgid':'434265567985667'}

conn= MySQLdb.connect(
        host='192.168.9.24',
        port = 3306,
        user='root',
        passwd='p@ssw0rd',
        db ='iPms',
        charset='utf8',
        cursorclass = MySQLdb.cursors.DictCursor
        )

conn1= MySQLdb.connect(
        host='192.168.9.24',
        port = 3306,
        user='root',
        passwd='p@ssw0rd',
        db ='iPmsBiz',
        charset='utf8',
        cursorclass = MySQLdb.cursors.DictCursor
        )

FileName = time.strftime('%Y%m%d_%H:%M:%S',time.localtime(time.time()))
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=15)
tomorrow=today+datetime.timedelta(days=15)

#Server='http://192.168.32.179'

#Server='http://192.168.32.179'
Server='http://testwww.51pms.net:'

Port='8001'


RoomType_API          ='/api/rooms/RoomType/'

Search_RoomType_API   ='/api/rooms/RoomTypes/'

RoomType_Status_API   ='/api/rooms/CanDeleteRoomType/'

PO_Search_API         ='/api/GuestFolios/eb/combine?OwnerIds=%s'%Headers['ownerid']

Check_In_API          ='/api/ordercheckin/pos'

Check_Out_API          ='/api/ordercheckin/Checkout/'



RoomType_API_url     = Server+Port+RoomType_API

RoomType_Status_url  = Server+Port+RoomType_Status_API

Search_RoomType_url  = Server+Port+Search_RoomType_API 

PO_Search_url        = Server+Port+PO_Search_API 

Check_In_url         = Server+Port+Check_In_API

Check_Out_url         = Server+Port+Check_Out_API




