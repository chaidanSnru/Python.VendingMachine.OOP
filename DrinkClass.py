class Drink:
    def __init__(self, name, price, quantity):
        # ชื่อเครื่องดื่ม
        self.__name = name
        # ราคาเครื่องดื่ม
        self.__price = price
        # จำนวนเครื่องดื่ม
        self.__quantity = quantity

    def get__name(self):
        return self.__name

    def set__name(self, x):
        self.__name = x    

    def get__price(self):
        return self.__price

    def set__price(self, y):
        self.__name = y    

    def get__quantity(self):
        return self.__quantity

    def set__quantity(self, z):
        self.__quantity = z