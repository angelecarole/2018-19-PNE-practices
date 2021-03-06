import json
import termcolor

# -- Open the json file
f = open("person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

print("total number of people:", len(person["People"]))

my_list = person["People"]

for n, person in enumerate(my_list):
 #Print the information in the object
 print()
 termcolor.cprint("Name: ", 'green', end="")
 print(person['Firstname'], person['Lastname'])

 termcolor.cprint("Age: ", 'green', end="")
 print(person['age'])

 # Get the phoneNumber list
 phoneNumbers = person['phoneNumber']

 # Print the number of elements int the list
 termcolor.cprint("Phone numbers: ", 'green', end='')
 print(len(phoneNumbers))

 # Print all the numbers
 for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i+1), 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("    Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'red', end='')
    print(num['number'])