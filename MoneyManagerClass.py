import json

class MoneyManager:
    def __init__(self, moneyjson):
        # อ่าน MoneyData.json เพื่อเอาข้อมูลเงินทอน changeMonoey กับเงินลูกค้า customerMoney มาสร้าง moneymanager
        with open(moneyjson) as fm:
            moneylist = json.load(fm)
        # เงินทอน
        self.__changemoney = moneylist[0]["changeMoney"]
        # เงินลูกค้าทั้งหมด
        self.__customermoney = moneylist[0]["customerMoney"]

    def get__changemoney(self):
        return self.__changemoney

    def set__changemoney(self, x):
        self.__changemoney = x

    def get__customermoney(self):
        return self.__customermoney

    def set__customermoney(self, y):
        self.__customermoney = y

    def recordMoney(self, jsonmoneydata):
         # เปิด file สำหรับเก็บข้อมูลเงินเมื่อจ่ายเครื่องดื่่มแล้ว(เราสามารถเอาทับ MoneyData.json ก็ได้แต่เก็บแยกเพื่อให้เห็นได้ชัด)    
        with open("MoneyDataAfterSpendDrink.json", "w") as write_file:
            write_file.write(jsonmoneydata)

    def payChangeMoney(self, changemoney):
        print(f"ทอนเงิน {changemoney} บาท")