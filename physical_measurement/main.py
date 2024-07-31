import csv,datetime,re,os

class QQQException(Exception):
    pass

# 実行ファイルのディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))

# body_mng.csvのパスを指定
body_mng_path = os.path.join(current_dir, 'body_mng.csv')
# member_mst.csvのパスを指定
member_mst_path = os.path.join(current_dir, 'member_mst.csv')

# 入力をラップする関数
def input_with_qqq(prompt):
    value = input(prompt)
    if value == "QQQ":
        raise QQQException()
    return value

# 年齢を返す
def age(birtyday_str,date_year):
    year = int(birtyday_str[:4])
    month = int(birtyday_str[4:6])
    day = int(birtyday_str[6:])
    birthday = datetime.date(year, month, day)
    return (int(date_year.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

# def 

# 登録するデータをファイルへ書き込む
def writeFile(number,day,height,weight):
    with open(body_mng_path,"a",encoding="utf-8") as f:
        writer = csv.writer(f)
        write_list = [number,day,height,weight]
        writer.writerow(write_list)

def searchData(num):
    result = []
    with open(body_mng_path, "r") as f:
        csv.reader(f)
        for row in csv.reader(f):
            if row[0] == num:
                result.append(row)
    return result

def print_info(data,birthday):
    date_str = data[1]
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:])
    past_date = datetime.date(year, month, day)
    past_age = age(birthday,past_date)
    height = data[2]
    weight = data[3]
    print(f'{year} 年  {month:2} 月  {day:2} 日  {past_age:2}才 {height}cm {weight}kg')


# member_mst.csvのデータをmem_list１に格納
with open(member_mst_path,"r",encoding="utf-8") as f:
    keys = ["社員番号","氏名","生年月日"]
    mem_list = list(csv.DictReader(f,keys))

while True:
    print('(登録"INS"、閲覧"PRI"、終了"QQQ"）：')
    cmd = input("コマンド =>")
    if not isinstance(cmd,str):
        print("コマンドが間違っています。")
    #　コマンドの判定
    if cmd == "QQQ":
        print("操作を終了します。")
        break
    # データを登録する
    elif cmd == "INS":
        print("データを登録する")
        while True:
            try:
                # 社員番号チェック
                while True:
                    number = input_with_qqq("社員番号 =>")
                    if len(number.encode('utf-8')) == 4:
                        person = [row for row in mem_list if row['社員番号'] == number]
                        if person:
                            break
                        else:
                            print("データが見つかりません。")
                    else:
                        print("半角で4桁の整数を入力してください")
                # 社員番号から個人情報を表示
                person = [row for row in mem_list if row['社員番号'] == number]
                birthday = person[0]['生年月日']
                today = datetime.date.today()
                person_age = age(birthday,today)
                name = person[0]['氏名']
                print(f"氏名 ： {name} {person_age} 才 ")
                # 測定日
                day = input_with_qqq("測定日(YYYYMMDD) =>")
                while len(day.encode('utf-8')) != 8:
                    print("8桁の整数を入力してください")
                    day = input_with_qqq("測定日(YYYYMMDD) =>")
                # 身長
                height = input_with_qqq("身長(cm) =>")
                while not re.match(r'[0-9]{3}\.{1}[0-9]{1}', height):
                    print("数値をXXX.Xの形式で入力してください")
                    height = input_with_qqq("身長(cm) =>")
                # 体重
                weight = input_with_qqq("体重(kg) =>")
                while not re.match(r'[0-9]{2,3}\.{1}[0-9]{1}', weight):
                    print("数値をXXX.Xの形式で入力してください")
                    weight = input_with_qqq("体重(kg) =>")
                # 登録確認
                confirm = input_with_qqq("登録しますか(Y/N) =>")
                while True:
                    if confirm == "Y":
                        # ファイルへ書き込み処理
                        writeFile(number,day,height,weight)
                        break
                    elif confirm == 'N':
                        print("登録をキャンセルしました。")
                        break
                    else:
                        print("YかNを入力してください。")
                        confirm = input_with_qqq("登録しますか(Y/N) =>")
                # 継続確認
                continue_cmd = input_with_qqq("続けますか(Y/N) =>")
                while continue_cmd != 'Y' and continue_cmd != 'N':
                    print("YかNを入力してください。")
                    continue_cmd = input_with_qqq("続けますか(Y/N) =>")
                if continue_cmd == 'Y':
                    continue
                elif continue_cmd == 'N':
                    print('登録を終了します')
                    break
            except QQQException:
                break
            except TypeError:
                print('不正な入力値です。')
                break
    # 身体測定データ表示 
    elif cmd == "PRI" or cmd == "":
        while True:
            try:
            # 社員番号チェック
                while True:
                    number = input_with_qqq("社員番号 =>")
                    if len(number.encode('utf-8')) == 4:
                        person = [row for row in mem_list if row['社員番号'] == number]
                        if person:
                            break
                        else:
                            print("データが見つかりません。")
                    else:
                        print("半角で4桁の整数を入力してください")
                # 社員番号から個人情報を表示
                person = [row for row in mem_list if row['社員番号'] == number]
                birthday = person[0]['生年月日']
                today = datetime.date.today()
                person_age = age(birthday,today)
                name = person[0]['氏名']
                print(f"氏名 ： {name} {person_age} 才 ")
                person_datas = searchData(number)
                for data in person_datas:
                    print_info(data,birthday)
                # 継続確認
                continue_cmd = input_with_qqq("続けますか(Y/N) =>")
                while continue_cmd != 'Y' and continue_cmd != 'N':
                    print("YかNを入力してください。")
                    continue_cmd = input_with_qqq("続けますか(Y/N) =>")
                if continue_cmd == 'Y':
                    continue
                elif continue_cmd == 'N':
                    print('閲覧を終了します')
                    break
            except QQQException:
                break
    else:
        print("コマンドが間違っています")
        continue
