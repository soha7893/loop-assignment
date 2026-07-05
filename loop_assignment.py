#Q 1 Mutiplication Table
user_number = int (input ("enter a number  :  "))
for number in range (1, 11):
    result = user_number * number
    print (f"{user_number} X {number} = {result}")
print ( 50* "=" )
#Q 2 Count even number
counter = 0
for i in range (1, 31):
    if i %2 == 0:
        print (f"{i}")
        counter += 1
print (f"Total even number = {counter} ") 
print ( 50* "=" )
#Q 3 Password Attempt
correct_password = "python123"
attemps = 0
max_attemps = 3
while attemps < max_attemps:
    user_password = input("Please enter your password:  ")
    if user_password == correct_password:
        print("Acess granted")
        break
    else:
            attemps += 1
            print("Incorrect password, try again")
if attemps == max_attemps:
     print("Account blocked")
#Q 4 Calculate Average Marks
input_user_mark = int(input("How many marks do you want to enter?  "))
total_marks = 0
count = 1
while count <= input_user_mark:
    mark = float(input(f"Enter mark {count} "))
    total_marks += mark
    count +=1
average = total_marks / input_user_mark
print (f"Average: {average}")
print ( 50* "=" )
#Another solution using for loop
total_marks = 0
input_user_mark = int(input("How many marks do you want to enter?  "))
for i in range(1, input_user_mark+1):
    mark = float(input(f"Enter mark numbe {i}  "))
    total_marks += mark
average = total_marks / input_user_mark
print(f"Average: {average}")
#Q 5 Number Guessing Game
secret_number = 7
while True:
    user_guess_number = int(input("Guess the number :  "))
    if user_guess_number > secret_number:
        print("Too high")
    elif user_guess_number < secret_number:
     print ("Too low")
    elif user_guess_number == secret_number:
           print ("correct !")
           break
#Q 6 Simple ATM menu
balance = 100
while True:
    print ("1. Check balance")
    print ("2. Deposite money")
    print ("3. Withdraw money")
    print ("4. Exit")
    user_choice = int(input("Please enter an option (1-4):  "))
    if user_choice == 1:
        print (f"current balance is: {balance}")
    elif user_choice == 2:
        deposit_amount = float (input("Enter amount you want to deposite:  "))
        balance += deposit_amount
        print(f"You deposited {deposit_amount}. Your new balance is: {balance}")
    elif user_choice == 3:
        withdraw_amount = float(input("Enter amount you want to withdraw:   "))
        if withdraw_amount > balance:
            print ("insufficient balance")
        else:
            balance -= withdraw_amount
            print(f"you withdrawed {withdraw_amount}.the remaining balance is:{balance}")            
    elif user_choice == 4:
        print ("thank you!")
        break
    else:
        print("Invalid optin, please choose a valid option (1-4)")
print(50 *"=")
#bonus1
item_count = 0
total_price = 0
most_expensive = 0
the_cheapest =0
while True:
    item_price = float(input("Enter item price or 0 to finish "))
    if item_price == 0 :
        break
    item_count +=1
    total_price += item_price
    if item_price > most_expensive :
        most_expensive = item_price
    if item_price < the_cheapest or the_cheapest == 0 :
        the_cheapest = item_price
if item_count == 0:
    print ("No items were added")    
else:
    average_price = total_price / item_count
    print(f"Number of items: {item_count}")
    print(f"Total price: {total_price}") 
    print(f"Average item price:{average_price}")
    print(f"Most expensive item: {most_expensive}") 
    print(f"Cheapest item: {the_cheapest}") 
    print (50*"=")
#bonus2
student_total_marks = 0.0
num_students = int(input("How many students do you want to enter?  "))
for i in range (num_students):
        print(50 * "-")
        name = input("Enter student name:  ")
        num_marks = int(input(f"How many marks for   {name}  "))
        for j in range (1 , num_marks + 1 ):
            mark = float(input(f"Enter mark {j}  "))
            student_total_marks += mark
        student_average = student_total_marks / num_marks
        if student_average > 50.0:       
                result = "Passed"
        else:
                result = "Failed"    
        print(f"{name}'s average is: {student_average}")
        print(f"Result: {result}")
                             