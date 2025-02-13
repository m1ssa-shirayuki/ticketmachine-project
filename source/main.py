price = [1000, 880, 780, 150]
buy = [0, 0, 0, 0]
def main():
    while True:
        result = input('1.購入処理\n2.管理画面\n3.終了処理\n')
        if not result.isdigit():
            print('数字を入力してください。')
        else:
            result = int(result)
            if result == 3:
                print('終了が選ばれました。')
                break
            elif result == 1:
                from buy import buy_process
                buy_process(price, buy)
            elif result == 2:
                from control import control_process
                control_process(price, buy)        

if __name__ == '__main__':
    main()