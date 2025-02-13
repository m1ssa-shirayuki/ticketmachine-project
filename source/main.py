import sys
    
price = [1000, 780, 880, 150]
buy = [0, 0, 0, 0]
cart = [0, 0, 0, 0]
def main(price, buy, cart):
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
            from buy import buy_process
            buy_process(price, buy, cart)            
        # 2が選ばれた時に管理画面
        elif result == 2:
            from control import control
            control(price, buy, cart)
    # 3が選ばれた時に終了
        else:
            print('終了が選ばれました。')
            sys.exit()
    
if __name__ == '__main__':
    main(price, buy, cart)