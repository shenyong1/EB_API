Feature: RoomType
  
Scenario: search RoomType  
    Given Add_RoomType "http://testwww.51pms.net:8001/api/rooms/RoomType/" and "R11111" and "W1111"
    When Search_All_RoomType "http://testwww.51pms.net:8001/api/rooms/RoomType/" and "R11111" and "W1111"
    Then Del_RoomType "http://testwww.51pms.net:8001/api/rooms/RoomType/" and "51CN4KV58M"