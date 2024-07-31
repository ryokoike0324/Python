class Item:
    def __init__(self,no,name,price):
        self.__no = no
        self.__name = name
        self.price = price

    def showItems(self):
        print(f"　{self.__no} {self.__name} : {self.price} 円")

    def showItem(self,is_return,index):
        if is_return:
            print(f"　{index} {self.__name} : {self.price} 円")
        else:
            print(f"　{self.__name} : {self.price} 円")