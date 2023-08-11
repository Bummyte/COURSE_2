#to display the string on the page

str = "The quick brown fox jumps over the lazy dog"
print(str)

#Print the length of the string to the page
print(len(str))

#Print the string in all uppercase letters
print(str.upper ())

#Print the string in all lowercase letters
print (str.lower ())

#Print the string in the title case
print(str.title ())

#Print the string in reverse
print(str[::-1])

#Print the string in reverse title case
print(str[:: -1].title())

#Count the number of times the letter “a” appears in the string
print(str.count("a"))

#Count the number of times the word “the” appears in the string
print(str.count("the"))

#Replace the word “the” with the word “a”
print(str.replace("the","a"))


#to count the frequency of each letter in the string and save the results in a dictionary
#define the dictionary as frequency_dict
frequency_dict = {}


for letter in str:
    if letter.isalpha():
        letter_lower = letter.lower()  #convert all letter to lower case, so the letters can be seen as same 
        if letter_lower in frequency_dict:
            frequency_dict[letter_lower] += 1
        else:
            frequency_dict[letter_lower] = 1
        
print(frequency_dict)

#to interpolate the below list into a string
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for person,gender,age in zip(people,sex,age):
    interpolate_string = f"{person} the {gender} is {age} years old."
    print(interpolate_string)


        
        