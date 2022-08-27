programming_dictionary = {
    "Bug": "An error in a programming that prevents th programming from running as expected",
    "Function":"A peice of code that you can call over and over again",
    "Loop": "Action of doing something over and over again"
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])

#Adding new item to dictionary 
programming_dictionary["Loop"] = "Action of doing something over and over again it can go infinity"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}


#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


#Loop through a dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
