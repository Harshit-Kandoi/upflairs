#user defined
# def add_two():
#     num1 = 10
#     num2 = 20
#     result = num1 + num2
#     return result

# # calling
# output = add_two()
# print(output)

# output2 = add_two()
# print(output2)

# def add_two(num1, num2):  #parameters
#     result = num1 + num2
#     return result

# #calling
# output = add_two(num1 = 25, num2 = 25)
# print(output)

# ls = [4,67,45,53,345,54,86]

# def my_len(ls):
# count = 0
# for item in ls:
#     count +=1
#     return count

# print (len(ls))
# print(my_len(ls))

# def calculate_average(numbers):
#     if len(numbers) == 0:
#         return 0
#     return sum(numbers) / len(numbers)

# user_input = input("Enter numbers separated by spaces: ")
# numbers = list(map(float, user_input.split()))

# average = calculate_average(numbers)

# print(f"The average is: {average}")


# ##module 
# manager_name = "harshit kandoi"
# manager_id = "hello@gmail.com"
# manager_pass = "helo@12345"
# manager_salary = 80000

# employee_name = "rocky"
# employee_id = "empl@gmail.com"
# employee_pass = "emp12345"
# employee_salary = 45000

# def average_finder(ls):
#     total_sum = 0
#     count = 0
#     for item in ls:
#         total_sum += item
#         count += 1
#     average = total_sum / count
#     print("your average is : ", round(average, 2))