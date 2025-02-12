import sys


print('券売機シミュレータ')
buy = []

while True:
    result = input('券売機処理 : 1\n管理画面 : 2\n終了 : 3\n')
    # if result.isdigit() and result > 0 and result < 4:
    #     result = int(result)
    #     break
    # else:
    #     print('指定された数字の中から入力して下さい。')

while result:
    print('1.特製ラーメン 1000円\n2.醤油ラーメン 780円\n3.塩ラーメン 880円\n4.ごはん 150円\n----\n')
    tmp = input('購入する商品番号(支払いに進む場合はc) >>> ')
    # if tmp.isdigit() and tmp > 0 and tmp < 5:
    #     print('商品選択時の処理')
    # else:
    #     print('指定された数字から入力してください。')
