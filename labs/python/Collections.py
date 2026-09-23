## python supports 3 types of collections: list, tuple and dictionary 

### 1) List
## list use brackets " [] "
## they are mutable - meaning they can be changed
## they allow duplicates
## they can also allow mix of different data types - this means it can have both interger and strings in the same list
print("We are dealing with list as a collection")
# syntax:

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

## accessing list position 
# this process is known as indexing
# indexing in list start at 0 
# syntax:

print(myFruitList[0]) # return the first value in the list
print(myFruitList[1]) # return second value
print(myFruitList[2]) # return 3rd value

## you can also use indexing to change the value in a list
myFruitList[2] = "oranges"
print(myFruitList)

### 2) Tuple
print()
print("We are dealing with tuple as a collection")
## tuple are like list but the key difference is as follows
# they use parentheses ()
# they cant be changed once set/defined - immutable

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# tuple indexing also starts at 0
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


### 3) Dictonary
print()
print("We are dealing with Dictionary as a collection")

# is simple a list with named positions called "Keys"

myFavouriteFruiteDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}

print(myFavouriteFruiteDictionary)
print(type(myFavouriteFruiteDictionary))


# indexing in dictionary is a bit diffent than indexing in list and tuples
# instead of using index via number starting from 0
# we simple use the key value 

print(myFavouriteFruiteDictionary["Akua"])  # where "Akua" is the key value being used to get the output which is "apple"
print(myFavouriteFruiteDictionary["Saanvi"])
print(myFavouriteFruiteDictionary["Paulo"])