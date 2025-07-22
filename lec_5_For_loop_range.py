# 1 WAP to print the vale from  1 to hundred while using the for loops 

# for i in range (1, 100):
#     print(i)

# 2 WAP to print the vale from 100 to 1 while using the for loops 

# for i in range (100, 0, -1):
#     print(i)
    
# 3 wap for a multiplicaton table usinf for Loop

# n = int (input("enter your number: "))

# for i in range (1 , 11):
#     print(n*i)


# 4 WAP TO find the sum of all natural number

# n = int (input("Enter your number: "))

# sum = 0 

# for i in range (1, n + 1):
#     sum += i
# print("Total number : ", sum)


# 5 WAP TO find the sfictorial of n  number

# n = int (input("Enter your number: "))

# factorial = 1

# for i in range (1, n + 1):
#     factorial*=i
# print(factorial)




# 6. Print even numbers from 1 to 20


# for i in range(1, 21):  # loop from 1 to 20 (inclusive)
#     if i % 2 == 0:      # check if number is even
#         print(i)

#  7. print star


# for i in range (1, 6,):
#     print(i*"x")

# for i in range (6, 1, -1):
#     print(i* "x")
    

# Write a Python program that prints a pyramid pattern of stars. 

# n = int(input("Enter the number of rows for the pyramid: "))

# for i in range(1, n + 1):
#     print(' ' * (n - i), end='')
    
#     # Step 4: Print stars (2*i - 1)
#     print('*' * (2 * i - 1))

# print(i)

n = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, n + 1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


