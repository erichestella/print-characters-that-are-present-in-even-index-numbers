#putting some title 
print('PRINTING THE WORD AT EVEN INDEX NUMBERS. \n')

#adding some variable to type the word
word = input('Type the word you want:\n ')

#adding up some display
print('\nResult:')

#it controls the word to display only that has even index numbers
for i in range(0, len(word), 2):
    print(word[i])
