# loop

# print("Hello world"*10)

# for = is used for range
# while = is used for condition

# general syntax for loop
# for (int i=0; i<=10; i++){
#     block of code
# }

# loop syntax for python
# for i in range(s,stop,jump):
#     block of code

# for i in range(11):  #range can be (0,10)
#     print("hi",i)

# print("for loop end")

# without using loop
# ls = [25,41,63,96,85,74,45,8,62,12]
# if 85 in ls:
#     print ("given number is present in list")
# else:
#     print("not present")

#using loop
# ls = [25,41,63,96,85,74,45,8,62,12]
# n = len(ls)
# for i in range(n):
#     if ls[i] == 85:
#         print("present")
#         break
#     else:
#         print("absent")

# ls = [25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,94]
# n = len(ls)
# for i in range(n):
#     if ls[i] <= 15:
#         print(ls[i])
#     else:
#         print("higher than 15")

# ls = [25, 41, 63, 96, 85, 74, 45, 8, 62, 12, 41, 32, 856, 96, 97, 94]

# for i in ls:
#     if i <= 50:
#         print(i)

# while loop

#syntax for while
# i=0 # initialization
# while condition:
#     block of Code
#     i++

#example for while loop
# i = 0
# while i <= 10:
#     print('welcome')
#     i += 1

# condition = True
# while condition:
#     quit = input("do you wanna quit? press Y/y : ")
#     if  quit == "Y" or quit == "y":
#         print ("by")
#     else:
#         condition = False
#         print ("wlcome")


# ls = [25, 41, 63, 96, 85, 74, 45, 8, 62, 12, 41, 32, 856, 96, 97, 94]
# for i in ls:
#     if i%2 == 0:
#         # print ("its a even number")
#         print (i)
        # ls2 = i
        # print(ls2)
    # else:
    #     print ("its not a even number")

# saala code hi galat h mera
# ls = [25, 41, 63, 96, 85, 74, 45, 8, 62, 12, 41, 32, 856, 96, 97, 94]
# i = 0
# while ls[i] %2 == 0:
#     print(ls[i])
#     i += 1


# ls = [25, 41, 63, 96, 85, 74, 45, 8, 62, 12, 41, 32, 856, 96, 97, 94]

# index = 0
# while index < len(ls):
#     if ls[index] % 2 == 1:
#         print(ls[index])
#     index += 1


# ls = [25, 41, 63, 96, 85, 74, 45, 8, 62, 12, 41, 32, 856, 96, 97, 94]
# for i in ls:
#     print(i)
#     i = i+i
#     print(i)

ls = [25, 41, 63, 96, 85, 74, 45, 8, 62, 12, 41, 32, 856, 96, 97, 94]
n = 0
for i in ls:
    n += i
print("total sum of ls is : ", n)
