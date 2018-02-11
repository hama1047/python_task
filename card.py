import random

class Card:
#カード情報
    num = ("A",2,3,4,5,6,7,8,9,10,"J","Q","K")
    suit = ("club","diamond","heart","spade")

#shuffle関数:100回シャッフルする
    def shuffle(card1,card2):
        for i in range(100):
            n = card2
            card2 = card1
            card1 = n
#disp変数：カード枚数を表示させる
    def disp(dealer_sheets_num):
        print("dealer: {0}".format(dealer_sheets_num))
#num_change変数:cardが絵札なら10代入,Aなら11代入
    def num_change(card):
        if card == "J" or "Q" or "K":
            card = 10
        if card == "A":
            card = 11
#hantei変数:勝ち負け判定する
    def hantei(player_point,dealer_point):
        if dealer_point > player_point:
            return 1
        elif player_point == dealer_point:
            return 2
        else: return 3
