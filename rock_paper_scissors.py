r='rock'
p='paper'
s='scissors'
p1=input("enter your choice player 1:").lower()
p2=input("enter your choice player2:").lower()
if p1==p2:
    print("It's a tie")
elif p1==r and p2==p:
    print("Player 2 wins")
elif p1=="p" and p2=="r":
    print("Player 1 wins")
elif p1=="r" and p2=="s":
    print("player 1 wins")
elif p1=="s" and p2=="r":
    print("player 2 wins")
elif p1=="p" and p2=="s":
    print("player 2 wins")
elif p1=="s" and p2=="p":
    print("player 1 wins")
else:
    print("check your inputs")