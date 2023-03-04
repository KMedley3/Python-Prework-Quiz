#Question 1
def hello_name(user_name):
     user_name = input('Enter your username: ')
     print('hello_' + user_name + '!')
    
hello_name()

# Question 2
# When the directions say "returns nothing" I'm assuming it means no return statement

def first_odds():
     for x in range(100):
         if x % 2 == 1:
             print(x)

first_odds()

# #Question 3
def max_num_in_list(a_list):
     print(max(a_list))
    
a_list = [9, 20, 44, 13, 7, 68, 24, 77]
max_num_in_list(a_list)

#Question 4
a_year = 2008
def is_leap_year(a_year):
     if (a_year % 4 == 0) or (a_year % 100 == 0 and 
                               a_year % 400 == 0):
         print('This is a leap year!')
         return True
     else:
         print('This is not a leap year')

is_leap_year(a_year)

#Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

a_list = [1, 2, 45,  4, 5, 6]

print(is_consecutive(a_list))