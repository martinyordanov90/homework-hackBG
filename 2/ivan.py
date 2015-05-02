counter = 0

book1_name = "Learn You Haskell"
book1_price = 0
counter = counter + 1

book2_name = "The Healthy Programmer"
book2_price = 50
counter = counter + 1

book3_name = "Code Complete"
book3_price = 60
counter = counter + 1

book4_name = "The Pragmatic Programmer"
book4_price = 20
counter = counter + 1

book5_name = "Pro Git"
book5_price = 0
counter = counter + 1

book6_name = "Introductio to Algorithms"
book6_price = 80
counter = counter + 1

book7_name = "Concrete Mathematics"
book7_price = 100
counter = counter + 1

total_sum = 0

print(book1_name + str(book1_price))
print(book2_name + str(book2_price))
print(book3_name + str(book3_price))
print(book4_name + str(book4_price))
print(book5_name + str(book5_price))
print(book6_name + str(book6_price))
print(book7_name + str(book7_price)) 

total_sum = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price
print(total_sum)
print(counter)
discount = (book6_price + book7_price) - ((book6_price + book7_price)* 0.25)
print(discount)
