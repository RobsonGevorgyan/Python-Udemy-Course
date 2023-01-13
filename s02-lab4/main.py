import os

def CountingWords(path):
    f = open(path)
    text = f.read()
    text = text.split()
    counter = 0
    for i in range(len(text)):
        counter = counter + 1
    f.close()
    return counter

pathToMyFile = r'C:\Users\rgeworgjan\PycharmProjects\file.txt'

#if os.path.isfile(pathToMyFile):
#    print(CountingWords(pathToMyFile)

result = os.path.isfile(pathToMyFile) and CountingWords(pathToMyFile)

print(result)