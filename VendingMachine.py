from DrinkManagerClass import DrinkManager
from MoneyManagerClass import MoneyManager
from VendingMachineClass import VendingMachine

def main():
    # สร้าง drinkmanger Obj
    drinkmanager = DrinkManager("DrinkData.json")
    # สร้าง moneymanager obj
    moneymanager = MoneyManager("MoneyData.json")
    # สร้าง vendingmachine
    vendingmachine = VendingMachine(drinkmanager, moneymanager)
    # เริ่มใช้งาน vending machine
    vendingmachine.vendingmachineStart()

# ตรวจสอบว่าชื่อ module เป็น main หรือไม่ ถ้าใช่ก็ให้ทำงาน (เป็นการกำหนด main ให้ python)
if __name__ == "__main__":
    main()
