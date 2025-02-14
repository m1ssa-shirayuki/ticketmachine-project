def control_process(price, buy):
    print(f'1.特製ラーメン {price[0]}円 {buy[0]}個 {price[0] * buy[0]}円\n2.醤油ラーメン {price[1]}円 {buy[1]}個 {price[1] * buy[1]}円\n3.塩ラーメン {price[2]}円 {buy[2]}個 {price[2] * buy[2]}円\n4.ごはん {price[3]}円 {buy[3]}個 {price[3] * buy[3]}円\n総売上価格 {price[0] * buy[0] + price[1] * buy[1] + price[2] * buy[2] + price[3] * buy[3]}円')
    
    while True:
        choose = input('管理メニュー\n1.売上リセット\n2.商品価格変更(事前に売上のリセット必須)\n3.管理画面の終了')
        if not choose.isdigit() or int(choose) > 3 or int(choose) < 1:
            print('不正な値です。')
        elif int(choose) == 1:
            buy = [0, 0, 0, 0]
            print('売上をリセットしました。')
        elif int(choose) == 2:
            if buy != [0, 0, 0, 0]:
                print('売上をリセットしてください。')
            else:
                print(f'1.特製ラーメン {price[0]}円\n2.醤油ラーメン {price[1]}円\n3.塩ラーメン {price[2]}円\n4.ごはん {price[3]}円')
                goods = input('価格を変更する商品の番号を入力してください。')
                if not goods.isdigit() or int(goods) > 4 or int(goods) < 0:
                    print('不正な値です。')
                else:
                    goods = int(goods)
                    new_price = input('変更金額を入力してください。')
                    if not new_price.isdigit():
                        print('不正な値です。')
                    else:
                        new_price = int(new_price)
                        ask = input('よろしいですか？ y or n')
                        if ask == 'y' or ask == 'Y':
                            price[goods - 1] = new_price
                            print('変更しました。')
                        else:
                            print('キャンセルしました。')
        elif int(choose) == 3:
            return price, buy