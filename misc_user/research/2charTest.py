import string
import operator
alphabet = 'abcdefghijklmnopqrstuvwxyzåäö1234567890'

arr = []
def funct1():
    for i in alphabet:
        for e in alphabet:
            arr.append(i+e)

funct1()


filepath = r'C:\Users\gunnar\Documents\github\todoky\research\muchtext.txt'
with open(filepath) as f:
    fileInMemory = f.readlines()

joined = ''.join(fileInMemory)
counter = 0
dd = {}
for i in arr:
    dd.update({i:joined.count(i)})


sortedDD = sorted(dd.items(), key=operator.itemgetter(1))

for i in sortedDD:
    print(f"{i}")

    