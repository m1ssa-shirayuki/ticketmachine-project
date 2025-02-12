import sys

def payment_process():
    payment_message = '購入一覧'
    total = 0
    if buy[0] != 0:
        payment_message += f'特製ラーメン {buy[0]}個'
        total += 1000 * buy[0]
    
    if buy[1] != 0:
        payment_message += f'醤油ラーメン {buy[1]}個'
        total += 780 * buy[1]
        
    if buy[2] != 0:
        payment_message += f'塩ラーメン {buy[2]}個'
        total += 880 * buy[2]
        
    if buy[3] != 0:
        payment_message += f'ごはん {buy[3]}個'
        total += 150 * buy[3]
        
    print(f'合計金額{total}円です。')
    
    while True:
        balance = input('現金を投入してください。 >>> ')
        # isdigitでマイナスを扱う際、Falseになってしまって文字列と負の数の判定ができないのでスライスを用いて負の数かどうかを判定
        if balance[0] == '-':
            print('金額は正の値でなければなりません。')
        # 数値でない場合
        elif not balance.isdigit():
            print('金額は数値でなければなりません。')
        # 合計金額に足りていない場合
        elif int(balance) < total:
            print('金額が不足しています。')
        # 合計金額以上だった場合お釣りを返して終了
        else:
            balance = int(balance)
            print(f'お釣り{balance - total}円です。')
            break
    

print('券売機シミュレータ')
buy = [0, 0, 0, 0]

# 最初の処理を選ぶ
while True:
    result = input('券売機処理 : 1\n管理画面 : 2\n終了 : 3\n')
    # 数字であり０より大きく４より小さい場合次の処理に
    if result.isdigit() and int(result) > 0 and int(result) < 4:
        result = int(result)
        break
    # それ以外の場合エラー文を表示して再度受け取り処理
    else:
        print('指定された数字の中から入力してください。')
        

# 1が選ばれた場合
if result == 1:
    print('1.特製ラーメン 1000円\n2.醤油ラーメン 780円\n3.塩ラーメン 880円\n4.ごはん 150円\n----\n')
    while True:
        tmp = input('購入する商品番号(支払いに進む場合はc) >>> ')
        if tmp.isdigit() and int(tmp) > 0 and int(tmp) < 5:
            tmp = int(tmp)
            print(f'{tmp}番が選択されました。')
            buy[tmp - 1] += 1
            print(buy)
        elif tmp == 'c':
            if buy[0] == 0 and buy[1] == 0 and buy[2] == 0 and buy[3] == 0:
                print('商品を選択してください。')
            else:
                print('支払処理')
                payment_process()
                break
        else:
            print('指定された数字から入力してください。')

# 3が選ばれた時に終了
if result == 3:
    print('終了が選ばれました。')
    sys.exit()
    
