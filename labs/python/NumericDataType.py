# Data types

# 1) Numeric data types

print ("python has three numeric types: int, float, and complex")

## a) working with interger data types

#variables
# think of variables as a means of storing data

print("We are dealing with Interger data type")

#syntax :

myValue=1

# where by myValue is the variable and 1 is the data stored inside it

## lets take a step back to learn about the: "type()" and "str()" build-in function
# for now dont worry about other built in functions you will learn more as we continue on 
# type() -- is used to show the data type of a variable
# str() -- is used to convert an argument into collection of letters called a string
# syntax :

print(type(myValue))

print(str(myValue) + " is of data type " + str(type(myValue)))

# I also want you to print the "myValue" variable on its own so that you can see the difference when the "type()" built-in function is not used
# unlike the previous file on "Hello_World.py" where we where printing a sentence (which is a string data type we will learn later)
# when you want to print a variable the syntax you use is as follows:

print(myValue)

## b) Working with float data types
#float is a data type that is used to store decimal numbers
print(" ")
print("We are dealing with float data type")

myValue=3.14
print(myValue)
# check its data type
print(type(myValue))  

print(str(myValue) + " is of data type " + str(type(myValue)))

## c) Complex data types
print(" ")
print("We are dealing with complex data type")

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))





## d)  Bool data types
print(" ")
print("We are dealing with boolean data type")

## boolean data types are on two usuall "True" or "False"

myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))


