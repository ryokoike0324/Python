class Cart:
    def __init__(self):
        self.__items = []

    def addItem(self,item):
        self.__items.append(item)

    def showCart(self,is_return):
        items = self.__items
        if items:
            i = 0
            for item in items:
                item.showItem(is_return,i)
                i += 1
        else:
            print('ありません。')

    # カート内の合計金額を返す
    def getTotalPrice(self):
        items = self.__items
        sum = 0
        for item in items:
            sum += item.price
        return sum

    def returnCartItem(self,index):
        self.__items.pop(index)

    def itemsCount(self):
        return len(self.__items)

