import requests
import json
import random
import logging
import datetime
import time
import MySQLdb

conn= MySQLdb.connect(
        host='192.168.9.24',
        port = 3306,
        user='root',
        passwd='p@ssw0rd',
        db ='iPms',
        )

today = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

Server='http://192.168.32.179'

Port=''


RoomType_API          ='/api/rooms/RoomType/'

Search_RoomType_API   ='/api/rooms/RoomTypes/'

RoomType_Status_API   ='/api/rooms/CanDeleteRoomType/'



RoomType_API_url     = Server+Port+RoomType_API

RoomType_Status_url  = Server+Port+RoomType_Status_API

Search_RoomType_url  = Server+Port+Search_RoomType_API 

Room ={'RoomTypeName':random.getrandbits(20),'RoomNumber':random.getrandbits(20),'NewRoomTypeName':random.getrandbits(30)}

Headers={'Content-Type':'application/json','ownerid':'434265567985665','orgid':'434265567985667'}
