
class Card:
#カード情報
    self.num = ("A",2,3,4,5,6,7,8,9,10,"J","Q","K")
    
    def heart:
        self.name = "H"
    def diamond:
        self.name = "D"
    def club:
        self.name = "C"
    def spade:
        self.name = "S"

#disp変数：カード枚数を表示させる
    def disp(dealer_sheets_num):
        for dealer_sheets_num in dealer_sheets_num < dealer_sheets_num:
            print("player: {0}, dealer: {1}".format(dealer_sheets_num,dealer_sheets_num))
#num変数:cardが絵札なら10代入,Aなら11代入
    def num(card):
        if card == "J" || "Q" || "K":
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
