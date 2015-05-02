from random import randint

n = input("Enter dice side: ")
n = int(n)

first_player = input("Enter first player name: ")
second_player = input("Enter second player name: ")

first_player_result = randint(1, n)
print(first_player + "rolls:" + str(first_player_result))
second_player_result = randint(1, n)
print(second_player + "rolls:" + str(second_player_result))

if first_player_result > second_player_result:
    print(first_player + " " + "wins!")
else:
    print(second_player + " " + "wins!")
