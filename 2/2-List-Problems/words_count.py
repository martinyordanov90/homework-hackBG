word = input("Enter word :")

n = input("Enter number :")
n = int(n)

count = 1
sum_word = 0

while count <= n:
    current_word = input("Enter word:")
    if current_word == word:
        sum_word += 1
    count += 1
print(word + " is found " + str(sum_word) + " times")


    
    
