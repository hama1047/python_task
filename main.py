from card import Card
import random


#辞書型(手札)
dealer = {}
player = {}

BJ = Card()
print("--BJゲーム開始--")
print(BJ.suit[1])


#手札を２枚入れる処理を書く
for i in range(2):
    card_num = random.randint(0,12)
    card_suit = random.randint(0,3)
    dealer.setdefault(Card.num[card_num], Card.suit[card_suit])
    card_num = random.randint(0,12)
    card_suit = random.randint(0,3)
    player.setdefault(Card.num[card_num], Card.suit[card_suit])

while True:

    #BJ.disp(len(dealer))←合計数を表示させる処理
    print("あなたの手札です↓")
    print(player)
    print("相手の手札です↓")
    print(dealer)

    print("もう１枚カードを引く？ yes:1,no:2")
    ans = int(input())

    if ans == 1:
        card_num = random.randint(0,12)
        card_suit = random.randint(0,3)
        player.setdefault(BJ.num[card_num], BJ.suit[card_suit])
    elif ans == 2:
        break
    else:
        print("1か2で答えてください")

#↑ここまでできた(合計を表示させる)
#dealerは16以下なら次のカードを引く17以上はそのまま
#↓判定する処理を書き換える
result = BJ.hantei(player_sum,dealer_sum)
#if文でどっちが勝ったか表示
if result == 1:
    print("あなたの負けです。")
elif result == 2:
    print("あなたの勝ちです！")
else :
    print("引き分けです")

print("--end--")
