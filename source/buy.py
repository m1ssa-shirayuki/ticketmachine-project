def buy_process(price, buy):
    message = '購入一覧\n'
    total = 0
    cart = [0, 0, 0, 0]
    while True:
        i = input(f'1.特製ラーメン {price[0]}円\n2.醤油ラーメン {price[1]}円\n3.塩ラーメン {price[2]}円\n4.ごはん {price[3]}円\n商品番号を入力してください。(cを入力すると会計)')
        if i == 'c':
            if cart == [0, 0, 0, 0]:
                print('商品が選ばれていません。')
            else:
                break
        elif not i.isdigit() or int(i) > 4 or int(i) < 1:
            print('商品番号を指定してください。')
        else:
            i = int(i)
            cart[i - 1] += 1
    
    if cart[0] > 0:
        message += f'1.特製ラーメン {cart[0]}個\n' 
        total += price[0] * cart[0]
    
    if cart[1] > 0:
        message += f'2.醤油ラーメン {cart[1]}個\n'
        total += price[1] * cart[1]
        
    if cart[2] > 0:
        message += f'3.塩ラーメン {cart[2]}個\n'
        total += price[2] * cart[2]
        
    if cart[3] > 0:
        message += f'4.ごはん {cart[3]}個\n'
        total += price[3] * cart[3]
    
    print(f'合計{total}円です')
    
    while True:
        money = input('現金を投入してください。')
        if not money.isdigit() or int(money) < total or int(money) < 0:
            print('金額が不足しています。')
        else:
            money = int(money)
            break
    
    print(f'お釣り{money - total}円です。')
    buy[0] += cart[0]
    buy[1] += cart[1]
    buy[2] += cart[2]
    buy[3] += cart[3]
    return buy