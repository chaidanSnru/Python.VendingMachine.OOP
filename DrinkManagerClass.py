import json
from DrinkClass import Drink

class DrinkManager:
    # สร้าง initian method
    def __init__(self, drinkjson):
        # กำหนด list เปล่าชื่อว่า __drinkdata
        self.__drinkdata = []
        # อ่าน DrinkData.json เพื่อเอาข้อมูล name price และ quantity มาสร้าง drink obj โดยเก็บใน listของ drinkmanager
        with open(drinkjson) as fd:
            drinklist = json.load(fd)
            for drinkdic in drinklist:
                # สร้าง object drink
                drink = Drink(drinkdic["name"], drinkdic["price"], drinkdic["quantity"])
                # เก็บลงใน [drink] ใน drinkmanager 
                self.add__drinkdata(drink)

    # สร้าง add__drinkdata() สำรับเก็บ drink เข้า []
    def add__drinkdata(self, drink):
        self.__drinkdata.append(drink)

    def get__drinkdata(self):
        return self.__drinkdata

    def getavailable__drinkdata(self):
        availabledrink = []
        for drink in self.__drinkdata:
            if drink.get__quantity() > 0:
                stringAvailableDrinkwithPrice = drink.get__name() + " ราคา " + str(drink.get__price()) + " บาท "
                availabledrink.append(stringAvailableDrinkwithPrice)
        return availabledrink

    def recordDrink(self, jsondrinkdata):
        # เปิด file สำหรับเก็บข้อมูลจำนวนกระป๋องเมื่อจ่ายเครื่องดื่่มแล้ว(เราสามารถเอาทับ DrinkData.json ก็ได้แต่เก็บแยกเพื่อให้เห็นได้ชัด)
        with open("DrinkDataAfterSpendDrink.json", "w") as write_file:
            write_file.write(jsondrinkdata)
    
    def spenceDrink(self, drinkname):
        print(f"ทำการจ่าย {drinkname} จำนวน 1 กระป๋อง")