import csv
from shop import Shop
from item import Item
from customer import Customer


class Program:

    __SHOP_NAME = 'ジョイ'
    __PRODUCT_NAME = []
    __PRODUCE_PRICE = []
    with open("./products.csv","r",encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for ro in reader:
            __PRODUCT_NAME.append(ro[1].replace('"',''))
            __PRODUCE_PRICE.append(int(ro[2].replace('"','')))

    def __init__(self,shop_name,product_name,product_price):
        self.__shop_name = shop_name
        self.__product_name = product_name
        self.__product_price = product_price

    @staticmethod
    def main():
        shop = Shop(Program.__SHOP_NAME)
        i = 0
        while i < 5:
            item = Item(i,Program.__PRODUCT_NAME[i],Program.__PRODUCE_PRICE[i])
            shop.addItem(item)
            i += 1
        shop.showShop()

        print()
        customer = Customer("田中",20000000)
        print(f"Customer を氏名={customer.name}で作成しました ")
        customer.showCustomer()
        print('□購入したい商品を選んでください。')
        # qが入力されたらループを抜ける
        while True:
            item_no = input("□商品番号（q で終了/t で合計計算/s で精算/r 返品/）? ")
            if isinstance(item_no,str):
                # 精算して終了する（ｑ）
                if item_no == "q":
                    customer.showCustomer()
                    customer.register()
                    break
                # 精算してから買い物を続ける
                elif item_no == "s":
                    customer.showCustomer()
                    customer.register()
                    shop.showShop()
                    continue
                # カート内合計金額表示
                elif item_no == "t":
                    print(f"現在のカート内の合計金額は {customer.showTotalPrice()} 円です。")
                    continue
                # 返品処理
                elif item_no == "r":
                    customer.returnItem()
                    shop.showShop()

            try:
                item_no = int(item_no)
            except ValueError:
                print("整数値で入力してください")
                continue
            # 入力された値をチェック（整数か、０以上５未満か）
            if 0 <= item_no < 5:
                want_item = shop.buyItem(item_no)
                if want_item:
                    customer.buyItem(want_item)
                else:
                    print("指定の商品はありません")
            else:
                print("■指定の商品はありません")



Program.main()