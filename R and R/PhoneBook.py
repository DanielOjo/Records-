# define class to hold contact details
class Contact():
    def __init__(self,name,number):
        self.name = name
        self.number = number

# function to display menu and get choice
def ShowMenu():
    print()
    print('1. Add a new entry')
    print('2. Edit an entry')
    print('3. Delete an entry')
    print('4. Look up number')
    print('9. Quit')
    print()
    thisChoice = input('Please enter the number of your choice: ')
    return thisChoice

# function to add an entry
def AddEntry():
    newName = input('Contact name: ')
    newNumber = input('Contact number: ')
    contactList.append(Contact(newName, newNumber))

# function to edit an entry
def EditEntry():
    indexSought = GetContactIndex()
    place_to_change = indexSought
    contact_name_change = str(input("Please enter their new contact name: "))
    number_change = str(input("Please enter their new number: "))
    contactList.pop(place_to_change)
    contactList.insert(place_to_change,contact_name_change,number_change)
    
# function to delete an entry
def DeleteEntry():
    indexSought = GetContactIndex()
    place_to_change = str(input("Please select a contact to delete: "))
    contactList.pop(place_to_change)


# function to find a number
def FindNumber():
    indexSought = GetContactIndex()
    number = contactList[indexSought].number
    print(number)
    
# function to find the index number of a name
def GetContactIndex():
    nameToFind = str(input("Please enter contact name: "))
    index = 0
    int(index)
    for index in (0,len(contactList)):
        if contactList[index].name == nameToFind:
            return index
    return -1

# function to populate initial contact list
# note: details may be loaded from a file for a real solution
def initialiseList():
    contactList.append(Contact('Andrew','07296469529'))
    contactList.append(Contact('Tommy','07392517863'))
    contactList.append(Contact('Oscar','07739343225'))
    contactList.append(Contact('Lola','07256010181'))
    contactList.append(Contact('Dominic','07430495302'))
    contactList.append(Contact('Rio','07648139073'))
    contactList.append(Contact('Alicia','07648139073'))
    contactList.append(Contact('Shakti','07592065561'))
    contactList.append(Contact('Alpha','07896194422'))
    contactList.append(Contact('Isabelle','07866810803'))

#--------------------------------------------------------------#
# main program

# set up initial list for phone book
contactList = []
initialiseList()

# generate menu with calls to functions to manage phone book
print('Phone book')
choice = ShowMenu()
while choice not in ['1', '2', '3', '4', '9']:
    choice = input('Please enter a valid choice: ')
if choice == '1':
    AddEntry()
elif choice == '2':
    EditEntry()
elif choice == '3':
    DeleteEntry()
elif choice == '4':
    FindNumber()
else:
    quit


