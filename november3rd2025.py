# # question 1
# i = 1
# while i < 6:
#     print(i)
#     i=i + 1
#output: 1 2 3 4 5

# # question 2
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")
#output: i is no longer less than 6

# # question 3
# for x in range(3):
#     print(x)
#output: 0 1 2

# # question 4
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # question 5
# for x in range(6):
#     print(x)

# # question 6
# output: 2 3 4

# question 7
# correct answer: if

# question 8
#output 1 3

# question 9
# output 1 2

# question 10
# for i in range(1,6,2):
#     print(i)
# output: 1 3 5
# for i in range(0,102,2):
#     print(i)
# output: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100

# question 11
# answer: for loop

# question 12
# answer: continue

# question 13
# output: 3 4 5

# question 14

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# choice = int(input("Enter a number between 1 and 7: "))
# if 1 <= choice <= 7:
#     print(days[choice - 1])
# else:
#     print("Invalid input! Please enter a number between 1 and 7.")

# choice = int(input("Enter a number between 1 and 7: "))
# match choice:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input! Please enter a number between 1 and 7.")

import random

random.randint(1, 9)

random_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi"]

match choice:
    case 1:
        print(random_words[0])
    case 2:
        print(random_words[1])
    case 3:
        print(random_words[2])
    case 4:
        print(random_words[3])
    case 5:
        print(random_words[4])
    case 6:
        print(random_words[5])
    case 7:
        print(random_words[6])
    case 8:
        print(random_words[7])
    case 9:
        print(random_words[8])