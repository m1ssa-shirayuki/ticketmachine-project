def buy_process(price, buy, cart):
    # print(price)
    # print(buy)
    # print(cart)
    print(f'1.特製ラーメン {price[0]}円\n2.醤油ラーメン {price[1]}円\n3.塩ラーメン {price[2]}円\n4.ごはん {price[3]}円\n----\n')
    while True:
        tmp = input('購入する商品番号(支払いに進む場合はc) >>> ')
        if tmp.isdigit() and int(tmp) > 0 and int(tmp) < 5:
            tmp = int(tmp)
            print(f'{tmp}番が選択されました。')
            cart[tmp - 1] += 1
            # print(cart)
        elif tmp == 'c':
            if cart[0] == 0 and cart[1] == 0 and cart[2] == 0 and cart[3] == 0:
                print('商品を選択してください。')
            else:
                print('支払処理')
                payment_message = '購入一覧'
                total = 0
                if cart[0] != 0:
                    payment_message += f'特製ラーメン {cart[0]}個'
                    total += price[0] * cart[0]
                
                if cart[1] != 0:
                    payment_message += f'醤油ラーメン {cart[1]}個'
                    total += price[1] * cart[1]
                    
                if cart[2] != 0:
                    payment_message += f'塩ラーメン {cart[2]}個'
                    total += price[2] * cart[2]
                    
                if cart[3] != 0:
                    payment_message += f'ごはん {cart[3]}個'
                    total += price[3] * cart[3]
                    
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
                        for i in range(0, 4):
                            buy[i] = buy[i] + cart[i]
                        cart = [0, 0, 0, 0]
                        from main import main
                        main(price, buy, cart)
                            
        else:
            print('指定された数字から入力してください。')