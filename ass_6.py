'''You are given the following lists: you need to write a program 
that will take only the unique values and print them out in a dictionary 
using the first letter of the item as the key'''

brands = ["Hermes", "Gucci", "Chanel", "Gucci",
           "Louis Vuitton", "Hermes", "Chanel","hugo boss", 
           "Guess", "Gucci", "Louis Vuitton"]

# creating an empty dictionary dict_brand
dict_brand= {}
unique_brands = set(brands) # to get unique values from the provided list

for brand in unique_brands:
    first_letter = brand[0].upper() #converting first letter of each value to upper case
    if first_letter not in dict_brand:
        dict_brand[first_letter]= [brand]
    else:
        dict_brand[first_letter].append(brand)
print(dict_brand)

'''Writing a program that asks a user for input and prints out 
if the number is an Armstrong number or not'''

user_num = int(input("Enter a number: "))
sum = 0
y = user_num
while y > 0:
   digit = y % 10 
   y //= 10
   sum += digit**3

if user_num == sum:
    print(f'the {user_num} is an armstrong number!')
else:
    print(f'the {user_num} is not an armstrong number!')


#Writing a program that will take a string and print out all the characters that have even indexes

#first we define a function: even_num and the parameter(str)
str = "Uguge Bunmi"
def even_num(str):
    for letter in range(len(str)): #looping via the str and getting the length and range
        if letter % 2 == 0:
            print(str[letter])

even_num(str)
even_num("mildred")
even_num("God is good all the time")


#Writing a program that will take a string and print out all the characters that have odd indexes

str = "Uguge"
def odd_num(str):
    for letter in range(len(str)):
        if letter % 2 ==1:
            print(str[letter])

odd_num(str)

str = "Uguge Bunmi" #to get the range and length of a str
print(len(str))
print(range(len(str)))
e = range(len(str))
print(e)


    
    










       