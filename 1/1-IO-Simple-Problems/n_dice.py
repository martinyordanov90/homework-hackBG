from random import randint

n = input("Enter dice: ")
n = int(n)

dice_rolled1 = randint(1, n)
print(dice_rolled1)

dice_rolled2 = randint(1, n)
print(dice_rolled2)

dice_sum1 = dice_rolled1 + dice_rolled2
print("The sum is: " + str(dice_sum1))

dice_rolled3 = randint(1, n)
print(dice_rolled3)

dice_sum2 = dice_rolled1 + dice_rolled2 + dice_rolled3
print("The sum is: " + str(dice_sum2))
