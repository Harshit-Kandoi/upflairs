# age = int (input("Enter you age"))
# if age>=0 and age<=5:
#     print("go to sleep")
# elif age>=5 and age<=18:
#     print("go to play")
# elif age>=18 and age<=75:
#     print("you can vote")
# else:
#     print("go to sleep")



# number = int(input("enter a number"))
# if number%2 == 0:
#     print("it is a even number")
# else:
#     print("it is a odd number")

# from datetime import date

# todayDate = date.today()

# DOB = input("Please enter your Date of Birth: ")
# currentYear = todayDate.year

# age = (int(currentYear) - int(DOB))
# print(f'Your current age is: {age}')

# print ("\n")
# if age <= 5:
#     print("You are a baby.")
# elif age >= 5 and age < 13:
#     print("You are a toddler")
# elif age >= 13 and age < 18:
#     print("You are an teenager")
# elif age >= 18 and age < 60:
#     print("You are an adult.")    
# elif age >= 60:
#     print("You are a senior Citizen")

#     from datetime import date, datetime

# today_date = date.today()

# # Get date of birth input and parse it
# dob_input = input("Please enter your Date of Birth (YYYY-MM-DD): ")
# dob = datetime.strptime(dob_input, "%Y-%m-%d").date()

# # Calculate age
# age = today_date.year - dob.year - ((today_date.month, today_date.day) < (dob.month, dob.day))
# print(f'Your current age is: {age}')

# # Determine age category
# if age <= 5:
#     print("You are a baby.")
# elif age > 5 and age < 13:
#     print("You are a toddler")
# elif age >= 13 and age < 18:
#     print("You are a teenager")
# elif age >= 18 and age < 60:
#     print("You are an adult.")
# elif age >= 60:
#     print("You are a senior citizen")


Name = input ("Please enter your name : ")
print ("welcome to your virtual atm " + Name + " sir") 

message = """
enter a number for which option you want to work with

type 1 check balance
type 2 deposit amount
type 3 withdraw amount"""

print( message )
balance = 5000
print ("sir as a welcome gift you have 5000rs in your bank")

option = int (input(" select a option : "))

if option == 1:
    print(balance)
elif option == 2:
    deposit = int(input("enter a amount which you want to add in your bank : "))
    print(deposit)
    balance = balance + deposit
    print(balance)
    print("here's your current balance : ")
elif option == 3:
    withdraw = int(input("enter a amount you want to withdraw : "))
    print(withdraw)
    balance = balance - withdraw
    print (balance)
    if balance>=0:
        print ("your transaction is seccusefully exectuted")
    else:
        print("bank balance can't be negative")
else:
    print("please select a option between 1-3")

print("thx for using our virtual bank")


