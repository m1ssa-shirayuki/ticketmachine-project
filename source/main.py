import sys

print('券売機シミュレータ')
buy = []

# 最初の処理を選ぶ
while True:
    result = input('券売機処理 : 1\n管理画面 : 2\n終了 : 3\n')
    # 数字であり０より大きく４より小さい場合次の処理に
    if result.isdigit() and int(result) > 0 and int(result) < 4:
        result = int(result)
        break
    # それ以外の場合エラー文を表示して再度受け取り処理
    else:
        print('指定された数字の中から入力して下さい。')
        

# 1が選ばれた場合
if result == 1:
    print('1.特製ラーメン 1000円\n2.醤油ラーメン 780円\n3.塩ラーメン 880円\n4.ごはん 150円\n----\n')
    while True:
        tmp = input('購入する商品番号(支払いに進む場合はc) >>> ')
        if tmp.isdigit() and int(tmp) > 0 and int(tmp) < 5:
            print('商品選択時の処理')
        elif tmp == 'c':
            print('支払処理')
            break
        else:
            print('指定された数字から入力してください。')

# 3が選ばれた時に終了
if result == 3:
    print('終了が選ばれました。')
    sys.exit()