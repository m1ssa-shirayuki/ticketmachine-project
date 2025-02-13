def control(price, buy, cart):
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
                from main import main
                main(price, buy, cart)