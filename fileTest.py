import os

if os.path.exists('final.txt'):
    os.remove('final.txt')

file = open('test.txt', 'rt')
final = open('final.txt', 'a')
for line in file:
    index = line.find('(')
    if line[index+1] == 'n':
        userInput = input('Enter a noun: \n').upper()
        replaceString = line.replace('(n)', userInput)
    elif line[index+1] == 'v':
        userInput = input('Enter a verb: \n').upper()
        replaceString = line.replace('(v)', userInput)
    elif line[index+1] == 'a':
        userInput = input("Enter an adjective: \n").upper()
        replaceString = line.replace('(a)', userInput)
    elif line[index+1] == 'd':
        userInput = input("Enter an adverb: \n").upper()
        replaceString = line.replace('(d)', userInput)
    else:
        replaceString = line

    print('')
    final.write(replaceString)

file.close()
file.close()

print('\n-------------------------------------')
final = open('final.txt', 'rt')
print(final.read())
