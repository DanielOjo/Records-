class Entry():
    def __init__(self, term, meaning):
        self.term = term
        self.meaning = meaning

def InitialiseDictionary():
    techList.append(Entry('Algorithm','a description of a process that achieves some task'))
    techList.append(Entry('Function','a routine that is called as part of an expression and returns a value'))
    techList.append(Entry('Identifier','a unique name given to a variable, procedure or function'))
    techList.append(Entry('Iteration','a sequence of steps that is repeated until some condition is met'))
    techList.append(Entry('Variable','a location in memory that contains data'))

def GetMeaning(term):
    index = 0
    wantedIndex = -1
    while index < len(techList)-1:
        if techList[index].term == term:
            wantedIndex = index
        else:
            index = index + 1
        return techList[index].meaning
    if wantedIndex != -1:
        return techList[index].meaning
    else:
        return 'not listed'
    
#-----------------------------------------#
# main program
print('A Brief Technical Dictionary')
print()

techList = []
InitialiseDictionary()

# prompt for word to look up and find word
lookUpTerm = input('Enter a technical term to check its definition: ')
meaningOfTerm = GetMeaning(lookUpTerm)
print('The definition of', lookUpTerm, 'is', meaningOfTerm)


