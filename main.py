import card


print("BJゲーム開始")

#手札を２枚入れる処理を書く

while True:

    disp(dealer.len)
    print("あなたの手札です↓")
    print(player)
    print("相手の手札です↓")
    print(dealer)

    print("もう１枚カードを引く？ yes:1,no:2")
    ans = int(input())

    if ans == 1:
        pass
    #1枚引くプログラム
    elif ans == 2:
        break
    else:
        print("1か2で答えてください")


result = hantei(player_sum,dealer_sum)
#if文でどっちが勝ったか表示
if result == 1:
    print("あなたの負けです。")
elif result == 2:
    print("あなたの勝ちです！")
else :
    print("引き分けです")

print("--end--")
