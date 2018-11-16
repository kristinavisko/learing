"""Load 5 int double-digit numbers. If the entered number is not double-digit,
throw it away. Sum the last digits of each entered number and print the sum."""

i = 0
y = []
sum = 0
right_number = 5
print ("Please insert five int double-digit numbers")

while i < 5:
    print ("You need to enter", right_number, "numbers")
    insert_number = int(input("Insert number"))
    
    if insert_number > 9 and insert_number < 100:
        y.append(insert_number)
        insert_number = insert_number % 10  #% by 10 always gives last digit of a number
        sum += insert_number
        i+=1
        right_number -= 1
print ("Sum of the last digits of each entered number is:", sum)




