def swap(index1,index2,numbers):
    
    temp = numbers[index2]
    numbers[index2] = numbers[index1]
    numbers[index1] = temp
    #return numbers
    

my_list = [5,4,3,2,1]
print(swap(0,4,my_list))
print(my_list)

