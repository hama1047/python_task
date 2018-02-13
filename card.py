import random

class Card:
#カード情報
    num = ("A",2,3,4,5,6,7,8,9,10,"J","Q","K")
    suit = ("club","diamond","heart","spade")

#shuffle関数:シャッフルする
    def shuffle_num(self):
        card1 = random.randint(0,12)
        card2 = random.randint(0,12)
        return (card1*card2)%13
    def shuffle_suit(self):
        card1 = random.randint(0,3)
        card2 = random.randint(0,3)
        return (card1*card2)%4

#num_change変数:cardが絵札なら10代入,Aなら11代入
    def num_change(self,card):
        if card == "J":
            return 10
        elif card == "Q":
            return 10
        elif card == "K":
            return 10
        elif card == "A":
            return 11
        else: return card
#hantei変数:勝ち負け判定する(22以上になった場合を書く)
    def hantei(self,player_point,dealer_point):
        if player_point > 21 and dealer_point < 22:
            return 1
        elif dealer_point > 21 and player_point < 22:
            return 2
        elif dealer_point > 21 and player_point > 21:
            return 3
        elif dealer_point > player_point:
            return 1
        elif player_point == dealer_point:
            return 3
        elif player_point > dealer_point:
            return 2
#log関数:同じカードがあったらやり直す
        def log():
            pass
#enemy_brain関数:17以上ならそのままそれ以下なら引く
        def enemy_brain(sum):
            pass
