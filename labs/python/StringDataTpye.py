# Data Type

## 2) STRING DATA TYPES

# basic string syntax:

myString="This is a string."
print(myString)

print(type(myString))
print(myString + " is of data type " + str(type(myString)))

## b) String concatenation - process of combining two strings into one string 
#string concatenation is done using the plus sign " + "


firstString = "Water"
secondString = "fall"
# so below firstString has been combined with secondString to form  one word.
thirdString = firstString + secondString
print (thirdString)

# in scenerios where you are concatenating two strings that are not one word but form a sentence
print()
print("Working with string concatenating:")
name="James"
event="meets"
topic="code World"

# notice the difference between the two print statements
print( name + event + topic)
print()
print( name + " " + event + " " + topic )

# also notice the string concatenation has been done inside a print statement as opposed to the first one which was done through another variable

print()
print("Working with input with strings")
name = input("What is your name ")
print(name) 


# Formating output Strings

color = input("What is you favourite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a {} {}!".format(name, color, animal))
# what format does is insert this variables values in a systematic order where you see " {} "
# so basically insert name in the first {}, color in the second {} and animal in the third and last {}.
