  
import random
import string

letters_of_password = int(input('Enter Number of letters of password: '))
numbers_of_password = int(input('Enter Number of numbers of password: '))
#random.choice return a random element from a sequence
#the for loop iterate the generator 
number_list =  ''.join(random.choice(string.digits) for i in range(numbers_of_password))
letter_list = ''.join(random.choice(string.ascii_letters) for i in range(letters_of_password))
    
syntax_list = number_list + letter_list + '$%^!@#'
if len(syntax_list) < 6:
    print('Password should be minimum 6 characters')
    exit()
#random sample return a len(syntax_list) list from syntax_list    
result = random.sample(syntax_list, len(syntax_list)) 
# join method/function is used to remove the list sintax and get a simple string
password = ''.join((result))
print('Your pasword is {}'.format(password))
    