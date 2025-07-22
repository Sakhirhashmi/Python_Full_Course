# 1 WAP to ptint  the length of a list (list in the parametrs)

# lst = [1, 2, 3, 4, 5,]

# def print_length(lst):
#     print("lenfth of the list is: ", len(lst))
#     return len(lst) 
# print(print_length(lst))


# # 2 WAP to print the element in  a single line

# l = [1, 2, 3, 4, 5]

# def print_element(l):
#     for i in l:
#         print(i, end=' ')

# print_element(l)


# WAP to to find the factorial of a n number by using the function.

# def factorial(n):   
#     factorial = 1
#     for i in range (1,n+1):
#         factorial *= i
#     print(factorial)
# factorial(5)
   
# 4 convert the USD to Pkrr

# def converter(usd_value):
#     pkr_value = usd_value * 281
#     print(usd_value,"USD", " = " , pkr_value,"PKR ")
# converter(300)


#5 WAF to take a input from the user and chck if a number is odd add into the string and if a number is even add into 
#the even number string.

# def separate_numbers():
#     user_value = input("Enter your value: ") 
#     odd_numbers = []
#     even_numbers = []
    
#     for i in user_value:
#         num = int(i)
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
    
#     print("Odd Numbers: ", odd_numbers)
#     print("Even Numbers: ", even_numbers)

# separate_numbers()



def separate_numbers():
    user_value = input("Enter your value: ")  # Take input as string
    odd_numbers = []
    even_numbers = []
    
    for digit in user_value:
        num = int(digit)
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    print("Odd Numbers: ", odd_numbers)
    print("Even Numbers: ", even_numbers)

separate_numbers()
