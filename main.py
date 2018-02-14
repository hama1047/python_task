from card import Card
from collections import Counter
import random



#辞書型(手札)
dealer = {}
player = {}
card_log = {}
#宣言
dealer_sum = 0
player_sum = 0

BJ = Card()
print("--BJゲーム開始--")

#手札を２枚入れる処理を書く
#合計数を計算
for i in range(2):
    ##------カードを引く流れ(dealer)------
    card_num = BJ.shuffle_num()
    card_suit = BJ.shuffle_suit()
    #↓log
    while True:

        if True == card_num in card_log.keys():
            if True == card_suit in card_log.values():
                card_num = BJ.shuffle_num()
                card_suit = BJ.shuffle_suit()
        else: 
            card_log.setdefault(Card.num[card_num], Card.suit[card_suit])
            dealer.setdefault(Card.num[card_num], Card.suit[card_suit])
            break

    dealer.setdefault(Card.num[card_num], Card.suit[card_suit])
    dealer_sum  = dealer_sum + BJ.num_change(Card.num[card_num])
    #↓Aを1として数える
    if True == dealer_sum > 22:
        if True == 'A' in dealer.keys():
            c = Counter(dealer)
            dealer_sum = dealer_sum - c['A']*10
    ##-------ここまで---------

    ##------カードを引く流れ(player)------ 
    card_num = BJ.shuffle_num()
    card_suit = BJ.shuffle_suit()
    #↓log
    while True:
        if True == card_num in card_log.keys():
            if True == card_suit in card_log.values():
                card_num = BJ.shuffle_num()
                card_suit = BJ.shuffle_suit()
        else:
            card_log.setdefault(Card.num[card_num], Card.suit[card_suit])
            player.setdefault(Card.num[card_num], Card.suit[card_suit])
            break

    player_sum = player_sum + BJ.num_change(Card.num[card_num])
    #↓Aの変換
    if True == player_sum > 22:
        if True == 'A' in player.keys():
            c = Counter(player)
            player_sum = player_sum - c['A']*10

    player.setdefault(Card.num[card_num], Card.suit[card_suit])
    ##-------ここまで---------                                                             

while True:

    if dealer_sum > 21 or player_sum > 21:
        break
    print("あなたの手札です↓")
    print("{0}合計:{1}".format(player,player_sum))#合計表示
    print("相手の手札です↓")
    print("{0}合計:{1}".format(dealer,dealer_sum))#合計表示


    print("もう１枚カードを引く？ yes:1,no:2")
    ans = int(input())    

    #BJ.enemy_brain(dealer_sum)
    ##------カードを引く流れ------ 
    if dealer_sum < 17:
        card_num = BJ.shuffle_num()
        card_suit = BJ.shuffle_suit()
    #↓log 
        while True:
            if True == card_num in card_log.keys():
                if True == card_suit in card_log.values():
                    card_num = BJ.shuffle_num()
                    card_suit = BJ.shuffle_suit()
            else:
                card_log.setdefault(Card.num[card_num], Card.suit[card_suit])
                dealer.setdefault(Card.num[card_num], Card.suit[card_suit])
                break
        dealer.setdefault(Card.num[card_num], Card.suit[card_suit])
        dealer_sum = dealer_sum + BJ.num_change(Card.num[card_num])
    #↓Aの変換
        if True == dealer_sum > 22:
            if True == 'A' in dealer.keys():
                c = Counter(dealer)
                dealer_sum = dealer_sum - c['A']*10
        dealer.setdefault(Card.num[card_num], Card.suit[card_suit])
   ##-------ここまで--------- 


    if ans == 1:
    ##------カードを引く流れ------ 
        card_num = BJ.shuffle_num()
        card_suit = BJ.shuffle_suit()
        #↓log                                                                                    
        while True:
            if True == card_num in card_log.keys():
                if True == card_suit in card_log.values():
                    card_num = BJ.shuffle_num()
                    card_suit = BJ.shuffle_suit()
            else:
                card_log.setdefault(Card.num[card_num], Card.suit[card_suit])
                player.setdefault(Card.num[card_num], Card.suit[card_suit])
                break
            
        player_sum = player_sum + BJ.num_change(Card.num[card_num])
        #↓Aの変換                                                                                 
        if True == player_sum > 22:
            if True == 'A' in player.keys():
                c = Counter(player)
                player_sum = player_sum - c['A']*10
        player.setdefault(Card.num[card_num], Card.suit[card_suit])
    ##-------ここまで--------- 

    elif ans == 2:
        break
    else:
        print("1か2で答えてください")

result = BJ.hantei(player_sum,dealer_sum)
print("あなたの手札です↓")
print("{0}合計:{1}".format(player,player_sum))#合計表示                                        
print("相手の手札です↓")
print("{0}合計:{1}".format(dealer,dealer_sum))#合計表示 
#if文でどっちが勝ったか表示
if result == 1:
    print("あなたの負けです。")
elif result == 2:
    print("あなたの勝ちです！")
else :
    print("引き分けです")

print("--end--")
