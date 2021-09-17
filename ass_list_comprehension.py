import random
# #1-Find all of the numbers from 1–1000 that are divisible by 8
# # num_div=[item for item in range(1,1001) if item%8==0]
# # print(num_div)
# #2-Table of any number
# # get_num=int(input("Enter a Number : "))
# # table_num=[get_num*num for num in range(1,11)]
# # print(table_num)
# #3-Count the number of spaces in a string (use string above)
# # intro='saman soo much sa b zda cuit'
# # sol-1 : 
# # count_space=[len(item) for item in intro if str(item)==" " ]
# # Sol-2 : 
# # count_space=len([ item for item in intro if str(item)==" " 
# #     ])
# # print(count_space)
# #Find all of the numbers from 1–1000 that have a 6 in them
# # find_num=[x for x in range(1,1001) if '6' in str(x)]
# # print(find_num)
# #Remove all of the vowels in a string (use string above)
# # string='saman is a girl'
# # rem_vowel=[x for x in string if not x in ('a','e','i','o','u') 
# #     ]
# # print(rem_vowel)
# #Find all of the words in a string that are less than 5 letters (use string above)
# # string='saman,esha,ayesha,zunaira,huzaila,noor'
# # d=string.split(',')
# # count_letter=[x for x in d if len(x)>=5
# #     ]
# # print(count_letter)
# #Use a dictionary comprehension to count the length of each word in a sentence (use string above)
# # string='saman is a girl'
# # str_split=string.split(' ')
# # len_word={str_split[x]:(len(str_split[x])) for x in range(0,len(str_split))
# #     }
# # print(len_word)
# #Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
# div_num=[
#     x for x in range(1,1000) if True in [True for d in range(2,10)
#     if x%d==0
#     ]
#     ]
# print(div_num)
# #8-For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
# max_num={num:max([div for div in range(1,10) if num%div==0])
# for num in range(1,1000)
# }
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
# div_num=[x for x in range(1500,2701)
# if x%7==0 and x%5==0]
# print(div_num)


# print(com_input)
#Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, 
# user will get a "Well guessed!" message, and the program will exit.
# 1-List Comprehension
# take_input=[int(input('Enter a number : ')) for x in range(10)
#     ]
# com_input=[x for x in take_input if x==random.randint(1,9)
#     ]
#2- by loop
# for item in iter(int,1):
#     a=int(input("Enter a Number : "))
#     if a==random.randint(1,9):
#         print('Well Done Number Matched')
#         break//want word again
#Write a Python program that accepts a word from the user and reverse it
# word_rev=[(input('enter a name : ')) for x in range(2)]
# word_rev.reverse()
# print(word_rev)  
#in range find even odd num
# even_odd=[{x:'Even'} if x%2==0 
# else {x:'Odd'} for x in range(20)
# ]      
# print(even_odd)
#Count even odd numbers
# even_list=[
#     x for x in range(20) if x%2==0
# ]
# print(len(even_list))
#Write a Python program that prints each item and its corresponding type from the following list.
# a=[1,2,3,'saman',23.09]
# data_type={type(x)
# for x in a
# }
# print(data_type)
 #Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# a=[x for x in range(7)
# if  not str(x) in ('6','3')  
# ]
# print(a)
# a=[
#     0 if not i else
#         (x := [0, 1]) and 1 if i == 1 else
#             not x.append(x[-2] + x[-1]) and x[-1]
#     for i in range(10)
# ]
# print(a)//not understand
#10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# num_multiple=[ "fizzBuzz"
# if x%5==0 and x%3==0 else ("Buzz" if x%5==0 else 
# ("Fizz" if x%3==0 else x))
#      for x in range(1,51)]
# print(num_multiple)
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
# two_dim_array=[[0 for x in range(3)]for y in range(4)
#     ]
# print(two_dim_array)
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[col*row for col in range(col_num)] for row in range(row_num)]
# print(multi_list)
#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
# multi_input=[
# (input("enter a number : ").lower()).split(' ') for item in range(2)]
# print(multi_input)
# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence
# get_input=(input("Enter a number : "))
# div_input=[int(x) for x in (get_input.split(',')) if int(x)%5==0]
# print(div_input)
#hon program that accepts a string and calculate the number of digits and letters
count_alphabat=0
count_digit=0
# for item in range(5):
#     x=input('enter some thing : ')
#     if x.isdigit():
#         count_digit+=1
#     elif x.isalpha():
#         count_alphabat+=1
#     else:
#         pass
# print("strings are : ",count_alphabat)
# print("Digits are : ",count_digit)
# string='34'
# try:
#     cal_alpha_digit=[string for x in range(len(string)) 
#     if  int(string)
#     ]   
#     print(cal_alpha_digit)
# except: 
#     pass
#Reverse Strings
# a=input("Enter a String : ")
# # a=['saman','alia']
# rev_a=[item for item in a]
# print(rev_a)
# even_num=[x for x in range(100,401) if x%2==0]
# print(even_num)
#Dog age
# dog_age=int(input("Enter Dog age : "))
# dog_year=dog_age*4
# print("Dog's age in years : ",dog_year)
#Months days number
# print("""List of months : January,
#  February, March, April, May, June, 
#  July, August, September, October, November, and December.
# """)
# get_input=input("Enter a Month name : ")
# cade_fold=get_input.casefold()
# if cade_fold in ('january','march','may','july','august','october','december'):
#     print(get_input.capitalize(),"this month contain 31 days")
# elif cade_fold in ("april", "june","september","november"):
#     print(get_input.capitalize(),"this month contain 30 days")
# elif cade_fold=="february":
#     print(get_input,"This Month Contain 28/29 Days")
#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# get_int1=int(input("Enter a integer: "))
# get_int2=int(input("Enter a integer: "))
# sum_int=(get_int1+get_int2)
# if sum_int>=15 and sum_int<=20:
#     print('Output is 20')
# else:
#     print('Output is : ',sum_int)
    
#Write a Python program to check a string represent an integer or not.
# get_str=input("Enter a String : ")
# if get_str.isdigit():
#     print("string has digit")
# for item in get_str:
#     if item.isdigit():
#         print("string have digit ",item)
# str_digit=[item for item in get_str
# if item.isdigit()]
# print(str_digit)
#Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides
# get_inp1=int(input('Enter number 1 : '))
# get_inp2=int(input('Enter number 2 : '))
# get_inp3=int(input('Enter number 3 : '))
# if get_inp1==get_inp2==get_inp3:
#     print("Triangle")
# elif get_inp1==get_inp2 or get_inp1==get_inp3 or get_inp2==get_inp3:
#     print("isosceles")
# else:
#     print('Scalene')
#Months days number
print("""List of months : January,
 February, March, April, May, June, 
 July, August, September, October, November, and December.
""")
get_input=input("Enter a Month name : ")
cade_fold=get_input.casefold()
if cade_fold in ('january','march','may','july','august','october','december'):
    print(get_input.capitalize(),"this month contain 31 days")
elif cade_fold in ("april", "june","september","november"):
    print(get_input.capitalize(),"this month contain 30 days")
elif cade_fold=="february":
    print(get_input,"This Month Contain 28/29 Days")
if cade_fold in ('december','january','february'):
    print("Season is : Winter")
if cade_fold in ('march', 'april' ,'may'):
    print("Season is : Spring")
if cade_fold in ('june','july','august'):
    print("Season is : Summer")
if cade_fold in ('september','october','november'):
    print("Season is : Autumn")


    


    

    
    
    
    
