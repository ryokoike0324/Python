from cart import Cart

class Customer:
    def __init__(self,name,money):
        self.name = name
        self.__money = money
        self.__cart = Cart()
    
    def buyItem(self,item):
        self.__cart.addItem(item)

    def showCustomer(self,is_return=False):
        print("********************************************")
        print(f"私の名前は、{self.name} です。")
        print(f"所持金は {self.__money} 円です。")
        print("カートに入っている商品は、")
        self.__cart.showCart(is_return)
        print(f"商品の合計は {self.showTotalPrice()} 円です。")
        print("********************************************")

    def showTotalPrice(self):
        return self.__cart.getTotalPrice()

    # お会計処理
    def register(self):
        money = self.__money
        total = self.showTotalPrice()
        # カートを空に
        self.__cart = Cart()
        new_money = money - total
        print()
        print('////////////////////////////////////////////')
        print("商品を精算します。")
        print(f"商品の合計は {total} 円です。")
        if new_money >= 0:
            self.__money = new_money
            print(f"所持金は {new_money} 円となりました。")
        else:
            print("所持金が不足しています！")
            print("商品を精算することはできませんでした。")
            print(f"所持金は {money} 円です。")
        print('////////////////////////////////////////////')

    # 商品返品処理
    def returnItem(self):
        print()
        print("----------------------------------（返品中） ")
        while True:
            self.showCustomer(is_return=True)
            order_num = input( "□返品する注文番号（q で終了）?")
            # 終了させるか判定
            if isinstance(order_num,str) and order_num == "q":
                break
            # 入力値が整数型かチェック
            try:
                order_num = int(order_num)
            except ValueError:
                print("整数値で入力してください")
                continue
            # 入力値がカートのインデックス範囲内か
            items_count = self.__cart.itemsCount()
            if 0 <= order_num < items_count:
                self.__cart.returnCartItem(order_num)
            else:
                print("対象商品がありません。")
            print()
            print("----------------------------------（返品中） ")
    
    def init_cart(self):
        self.__cart = Cart()

            


        