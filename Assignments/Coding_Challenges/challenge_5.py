file = open('Assignments/Coding_Challenges/file.txt','r')

myset = set()

for line in file:
    for word in line.strip().split(','):
        myset.add(word)

print(myset)
print(type(myset))