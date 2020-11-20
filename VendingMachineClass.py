import json
from DrinkManagerClass import DrinkManager
from MoneyManagerClass import MoneyManager


class VendingMachine:
    def __init__(self, drinkmanager, moneymanager):
        self.__drinkmanager = drinkmanager
        self.__moneymanager = moneymanager

    def vendingmachineStart(self):
        # เปิด loop infinity
        # หยุด loop infinity ด้วย ctrl + c
        while True:
            print("ตู้หยอดน้ำยินดีให้บริการ")
            print("ท่านสามารถเลือกหยอดน้ำได้ดังนี้")
            print(self.__drinkmanager.getavailable__drinkdata())
            print(f"ณ. ตอนนี้ท่านหยอดเงิน {self.__moneymanager.get__customermoney()} บาท")
            # รับ input ของลูกค้า
            customermoney = int(input("กรุณาหยอดเงิน 1 2 5 หรือ 10 บาท สั่งสินค้ากด 0: "))
            # ถ้าหยอด 1 บาท ให้เอาเงินที่หยอดบวกเพิ่มเข้าเรื่อยๆกับ customermoney
            if customermoney == 1:
                self.__moneymanager.set__customermoney(self.__moneymanager.get__customermoney()+customermoney)
            # ถ้าหยอด 2 บาท ให้เอาเงินที่หยอดบวกเพิ่มเข้าเรื่อยๆกับ customermoney
            elif customermoney == 2:
                self.__moneymanager.set__customermoney(self.__moneymanager.get__customermoney()+customermoney)
            # ถ้าหยอด 5 บาท ให้เอาเงินที่หยอดบวกเพิ่มเข้าเรื่อยๆกับ customermoney  
            elif customermoney == 5:
                self.__moneymanager.set__customermoney(self.__moneymanager.get__customermoney()+customermoney)
            # ถ้าหยอด 10 บาท ให้เอาเงินที่หยอดบวกเพิ่มเข้าเรื่อยๆกับ customermoney    
            elif customermoney == 10:
                self.__moneymanager.set__customermoney(self.__moneymanager.get__customermoney()+customermoney)
            # ถ้ากดเลือกสินค้า
            elif customermoney == 0:
                print("ท่านสามารถเลือกหยอดน้ำได้ดังนี้")
                print(self.__drinkmanager.getavailable__drinkdata())
                print(f"ณ. ตอนนี้ท่านหยอดเงิน {self.__moneymanager.get__customermoney()} บาท")
                # เก็บว่าลูกค้าเลือกเครื่องดื่มอะไร
                drinkCan = input("กรุณาพมิชื่อเครื่องดื่มที่ท่านต้องการ : ")
                # เปิด for เพื่อตรวจสอบข้อมูลของ [drink] ของ drinkmanager
                for adrinkCan in self.__drinkmanager.get__drinkdata():
                    # ถ้า drink ใน [drink] ตรงกับที่ลูกค้าเลือก
                    if adrinkCan.get__name() == drinkCan:
                        # ตรวจสอบว่าเงินที่หยอดมากกว่าราคาเครื่องดื่มที่เลือกหรือไม่
                        if self.__moneymanager.get__customermoney() < adrinkCan.get__price():
                            print("เงินที่หยอดน้อยกว่าราคาสินค้ากรุณาหยอดใหม่")
                        else:
                            # คำนวนเงินทอน
                            returnChangemoney = self.__moneymanager.get__customermoney() - adrinkCan.get__price()
                            # คำนวนเงินเก็บในตู้
                            self.__moneymanager.set__changemoney(self.__moneymanager.get__changemoney()+adrinkCan.get__price())
                            # ลดจำนวนเครื่องดื่มลง 1 กระป๋อง
                            adrinkCan.set__quantity(adrinkCan.get__quantity()-1)
                            # ทำการ reset cutomermoney ให้เป็น 0
                            self.__moneymanager.set__customermoney(0)
                            # สร้างเอกสาร format json จาก drinkmanager.get__drinkdata()
                            drinkJsonString = json.dumps([drinkobj.__dict__ for drinkobj in self.__drinkmanager.get__drinkdata()])
                            # ทำการบันทึกจำนวนกระป๋องใหม่ลง file
                            self.__drinkmanager.recordDrink(drinkJsonString)
                            # สร้างเอกสาร format json จาก moneymanager
                            moneyJsonString = json.dumps([self.__moneymanager.__dict__])
                            # ทำการบันทึกจำนวนเงินใหม่ลง file
                            self.__moneymanager.recordMoney(moneyJsonString)                            
                            # ทำการจ่ายเงินทอน
                            self.__moneymanager.payChangeMoney(returnChangemoney)
                            # ทำการจ่ายเครื่องดื่ม
                            adrinkname = adrinkCan.get__name()
                            self.__drinkmanager.spenceDrink(adrinkname)
                        break
            else:
                print("ท่านหยอดเงินผิดกรุณาหยอดใหม่ !!!")