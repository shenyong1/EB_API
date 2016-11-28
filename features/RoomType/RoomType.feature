Feature: RoomType
  
Scenario: search selenium  
    Given Add_RoomType(Add_RoomType_url,"N1000","10000") 
    When Search_All_RoomType(Search_All_RoomType_url,"N1000","10000")
    Then Del_RoomType(Del_RoomType_url, RoomID[2])