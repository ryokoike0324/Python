import random

B_list = [i for i in random.sample(range(1,16),5)]
I_list = [i for i in random.sample(range(16,31),5)]
N_list = [i for i in random.sample(range(31,46),5)]
G_list = [i for i in random.sample(range(46,61),5)]
O_list = [i for i in random.sample(range(61,76),5)]

lineList = [B_list,I_list,N_list,G_list,O_list]

# リストの縦横をビンゴに合わせる
def format_bingo(num_list):
    Bingo = []
    i = 0
    while i < 5:
        temp_list = []
        for list in num_list:
            temp_list.append(list[i])
        Bingo.append(temp_list)
        i += 1
    return Bingo

# 真ん中に穴をあける(真ん中を■にする)
def holePunch(bingo_list):
    bingo_list[2][2] = "■"

# 整数のリストをBingoに則した文字列に変換する
def strBingo(nums_list):
    Bingo = []
    for list in nums_list:
        temp_str = '|'
        for n in list:
            if n == "■":
                sqare = " ■|"
                temp_str += sqare
            else:
                format_num = "{:2d}|".format(n)
                temp_str += format_num
        Bingo.append(temp_str)
    return Bingo

# リーチ数をカウントする
def countReach(nums_list):
    count = 0
    # ビンゴの横軸にリーチがあるか調べる
    for list in nums_list:
        if list.count('■') == 4:
            count += 1
    # 縦軸のビンゴリストを作る
    y_bingo = format_bingo(nums_list)

    # ビンゴの縦軸にリーチがあるか調べる
    for list in y_bingo:
        if list.count('■') == 4:
            count += 1
    # ビンゴの左斜め軸のリストを作り、リーチがあるか調べる
    left_list = [
                nums_list[0][0],
                nums_list[1][1],
                nums_list[2][2],
                nums_list[3][3],
                nums_list[4][4]]
    if left_list.count('■') == 4:
        count += 1
    # ビンゴの右斜め軸のリストを作り、リーチがあるか調べる
    right_list = [
                nums_list[0][4],
                nums_list[1][3],
                nums_list[2][2],
                nums_list[3][1],
                nums_list[4][0]]
    if right_list.count('■') == 4:
        count += 1
    return count

# 数字があたりか判定
def is_hit(bingo,num):
    for list in bingo:
        if num in list:
            return True
    return False

# 数字が的中した場合、ビンゴを更新する
def update_bingo(bingo,num):
    for list in bingo:
        i = 0
        while i < 5:
            if list[i] == num:
                list[i] = '■'
                return
            i += 1

# ビンゴがそろっているかどうか調べる
def is_bingo(nums_list):
    for list in nums_list:
        if list.count('■') == 5:
            return True
    y_bingo = format_bingo(nums_list)
    # 縦軸を調べる
    for list in y_bingo:
        if list.count('■') == 5:
            return True
    # ビンゴの左斜め軸のリストを作り、リーチがあるか調べる
    left_list = [
                nums_list[0][0],
                nums_list[1][1],
                nums_list[2][2],
                nums_list[3][3],
                nums_list[4][4]]
    if left_list.count('■') == 5:
        return True
    # ビンゴの右斜め軸のリストを作り、リーチがあるか調べる
    right_list = [
                nums_list[0][4],
                nums_list[1][3],
                nums_list[2][2],
                nums_list[3][1],
                nums_list[4][0]]
    if right_list.count('■') == 5:
        return True
     

# Bingoを出力する
formattedList = format_bingo(lineList)
# 真ん中を■にする
holePunch(formattedList)
get_nums = list(range(1,76))


while True:
    bingo = strBingo(formattedList)
    print("----------------")
    print("|Ｂ|Ｉ|Ｎ|Ｇ|Ｏ|")
    print("----------------")
    for list in bingo:
        print(list)
        print("----------------")
    if is_bingo(formattedList):
        print('congratulations!')
        break
    else:
        reachCount = countReach(formattedList)
        print(f'リーチ数：{reachCount}')
        input('エンターキーを押して下さい：')
        rand_num = random.choice(get_nums)
        get_nums.remove(rand_num)
        print(f"出た数字：{rand_num}")
        input('エンターキーを押して下さい：')
        if is_hit(formattedList,rand_num):
            print('Hit')
            update_bingo(formattedList,rand_num)
            input('エンターキーを押して下さい：')
        else:
            print('Deviate')
            input('エンターキーを押して下さい：')


        
        
    
    





# print_bingo(F_BINGO)

    

        

# new_bingo = input("")

# while 1:

# print("----------------")
