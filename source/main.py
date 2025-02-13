import sys

def payment_process():
    payment_message = '購入一覧'
    total = 0
    if buy[0] != 0:
        payment_message += f'特製ラーメン {buy[0]}個'
        total += price[0] * buy[0]
    
    if buy[1] != 0:
        payment_message += f'醤油ラーメン {buy[1]}個'
        total += price[1] * buy[1]
        
    if buy[2] != 0:
        payment_message += f'塩ラーメン {buy[2]}個'
        total += price[2] * buy[2]
        
    if buy[3] != 0:
        payment_message += f'ごはん {buy[3]}個'
        total += price[3] * buy[3]
        
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
            print(f'お釣り{balance - total}円です。\n')
            break
    
price = [1000, 780, 880, 150]
buy = [0, 0, 0, 0]

# 最初の処理を選ぶ
while True:
    while True:
        print('券売機シミュレータ')
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
        print(f'1.特製ラーメン {price[0]}円\n2.醤油ラーメン {price[1]}円\n3.塩ラーメン {price[2]}円\n4.ごはん {price[3]}円\n----\n')
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
        
    # 2が選ばれた時に管理画面
    elif result == 2:
        while True:
            print(f'1.特製ラーメン {price[0]}円 {buy[0]}個販売 合計{price[0] * buy[0]}円\n2.醤油ラーメン {price[1]}円 {buy[1]}個販売 合計{price[1] * buy[1]}円\n3.塩ラーメン {price[2]}円 {buy[2]}個販売 合計{price[2] * buy[2]}円\n4.ごはん {price[3]}円 {buy[3]}個販売 合計 {price[3] * buy[3]}円\n---\n総売上金額 {price[0] * buy[0] + price[1] * buy[1] + price[2] * buy[2] + price[3] * buy[3]}円')
            manager_result = input('---管理メニュー---\n1.売上をリセットする\n2.商品の価格を変更する\n※売上がリセットされていないと利用できません。\n3.管理画面を終了する\n---\n管理コード入力 >>> ')
            
            if not manager_result.isdigit():
                print('数字を入力してください。')
            elif int(manager_result) > 3 or int(manager_result) < 1:
                print('1から3の間で入力してください。')
            elif int(manager_result) == 1:
                buy = [0, 0, 0, 0]
                print('売上をリセットしました。')
            elif int(manager_result) == 2:
                if buy == [0, 0, 0, 0]:
                    goods = input('1.特製ラーメン\n2.醤油ラーメン\n3.塩ラーメン\n4.ごはん\n価格を変更する商品の番号を入力してください。 >>> ')
                    if not goods.isdigit():
                        print('正しい値を入力してください。')
                    elif int(goods) > 4 or int(goods) < 1:
                        print('値は1から4の間でなければなりません。')
                    else:
                        new_price = input('新しい価格を入力してください。 >>> ')
                        if not new_price.isdigit():
                            print('正しい値を入力してください。')
                        else:
                            ask = input('よろしいですか？ y or n')
                            if ask != 'y' and ask != 'Y' and ask != 'n' and ask != 'N':
                                print('どちらかを入力してください。')
                            elif ask == 'y' or ask == 'Y':
                                price[int(goods) - 1] = int(new_price)
                                print('変更しました。')
                            else:
                                print('キャンセルしました。')
                else:
                    print('売上をリセットしてから実行してください。')
            else:
                # pass
                break
                

# 3が選ばれた時に終了
    else:
        print('終了が選ばれました。')
        sys.exit()
    
