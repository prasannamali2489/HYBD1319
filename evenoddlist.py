'''you have one list of student marks. create two sublists foe rvrn or odd marks students'''
std=[45,65,89,99,90,78,78,94,34,54,56,46,45,23,34,54,67,09,89,87]
evenstd=[]
oddstd=[]
for i in std:
    if i%2==0:
        evenstd.append(i)
    else:
        oddstd.append(i)
print("List of even  marks: ",evenstd)
print("List of odd  marks : ",oddstd)