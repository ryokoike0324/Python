import item

class Shop:
    def __init__(self,name):
        self.name = name
        self.__items = []

    # itemsへ対象の商品を追加します
    def addItem(self,item):
        self.__items.append(item)

    # 商品番号から対象の商品を返します
    def buyItem(self,itemNo):
        return self.__items[itemNo]

    def showShop(self):
        print("============================================ ")
        print(f'いらっしゃいませ。{self.name}です。')
        print('扱っている商品は、 ')
        for item in self.__items:
            item.showItems()
        print("============================================ ")
        

