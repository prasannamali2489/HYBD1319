'''note/ table
=
-
*
/
//
%
check
int+int float string bolean list tuple set dict frozenset

different datatypes addition,or other'''
print("addition of all datatypes: ")
print("int")
n1=10
n2=20
print(n1+n2)
# we can do addition of integer datatype

print("float")
n3=10.5
n4=20.5
print(n3+n4)
# we can do addition of float datatype

print("string")
str1="Python "
str2="Coding"
print(str1+str2)
# we can do addition of string datatype .It is called concatenation of two string

print("boolean")
print(True+True)  # ans = 2
print(False+False)# ans = 0
print(False+True) # ans 1
print(True+False)# ans = 1
# we can do addition of boolean datatype

print("complex")
n5=10+10j
n6=10-10j
print(n5+n6)
# we can do addition of complex datatype

print("List")
l1=[1,2,3,4]
l2=["ram","raj","raju","ramu"]
print(l1+l2)
# we can do addition of list datatype, where we can extend list

print("tuple")
t1=(1,2,3,4)
t2=("ram","raj","raju","ramu")
print(t1+t2)
# we can do addition of tuple datatype,i in which two tuple are join in single tuple.

print("set")  
s1={1,2,3,4,5,67,"ram"}
s2={"ram","raj","raju","ramu",4, 3}
print(s2+s1)  
# TypeError: unsupported operand type(s) for + ,-,/ ,//, %, * : 'set' and 'set' we can do operation like union(|) , interaction(&), difference(-)

print("FrozenSet")   
f1 = frozenset([1,2,3,4])
f2 = frozenset((1,4,5,6)) 
print(f1+f2) 
# TypeError: unsupported operand type(s) for +,-,/ ,//, %, *: 'set' and 'set' we cn do operation like union , interaction

print("Dictionary") 
d1={1:"ram",2:"shayam"}
d2={1:"raj",2:"rao"}
d3={1:5,2:6}
d4={1:5,2:4}
print(d3+d4)
 #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print("-\t--"*20)

print("Subtraction of all datatypes: ")

print("int")
n1=20
n2=10
print(n1-n2)
# subtraction of two integers gives integer result

print("float")
n3=20.5
n4=10.5
print(n3-n4)
# subtraction of two float numbers gives float result

print("string")
str1="Python"
str2="Coding"
print(str1-str2)
# TypeError occurs because subtraction is not supported for string datatype

print("boolean")
print(True-True)
print(False-False)
print(True-False)
print(False-True)
# boolean behaves like integer (True=1, False=0) so subtraction works

print("complex")
n5=10+10j
n6=5+5j
print(n5-n6)
# subtraction of complex numbers subtracts real and imaginary parts

print("List")
l1=[1,2,3]
l2=[4,5]
print(l1-l2)
# TypeError occurs because subtraction is not supported for list datatype

print("tuple")
t1=(1,2,3)
t2=(4,5)
print(t1-t2)
# TypeError occurs because subtraction is not supported for tuple datatype

print("set")
s1={1,2,3,4}
s2={2,3}
print(s1-s2)
# subtraction works as set difference (elements in s1 but not in s2)

print("frozenset")
f1=frozenset([1,2,3,4])
f2=frozenset([3,4])
print(f1-f2)
# subtraction works as set difference in frozenset

print("dictionary")
d1={1:2}
d2={3:4}
print(d1-d2)
# TypeError occurs because subtraction is not supported for dictionary
print("-\t--"*20)

print("Multiplication of all datatypes:")

print("int")
n1=10
n2=5
print(n1*n2)
# multiplication of two integers gives integer result

print("float")
n3=10.5
n4=2.0
print(n3*n4)
# multiplication of two floats gives float result

print("string")
str1="Python "
print(str1*3)
# string multiplied by integer repeats the string 3 times

print("boolean")
print(True*True)
print(True*False)
# boolean behaves like integer (True=1, False=0)

print("complex")
n5=2+3j
n6=1+2j
print(n5*n6)
# multiplication follows complex number multiplication rules

print("List")
l1=[1,2,3]
print(l1*2)
# list multiplied by integer repeats the list elements

print("tuple")
t1=(1,2,3)
print(t1*2)
# tuple multiplied by integer repeats tuple elements

print("set")
s1={1,2,3}
s2={4,5}
print(s1*s2)
# TypeError because multiplication is not supported for sets

print("Dictionary")
d1={1:2}
d2={3:4}
print(d1*d2)
# TypeError because multiplication is not supported for dictionaries
print("\t--"*20)

print("Division of all datatypes:")

print("int")
print(10/5)
# division of integers returns float result

print("float")
print(10.5/2)
# division of floats returns float result

print("string")
print("Python"/2)
# TypeError because division is not supported for strings

print("boolean")
print(True/True)
# True=1 so result becomes 1.0

print("complex")
print((2+3j)/(1+2j))
# division works for complex numbers

print("List")
print([1,2]/2)
# TypeError because division is not supported for lists

print("tuple")
print((1,2)/2)
# TypeError because division is not supported for tuples

print("set")
print({1,2}/{3,4})
# TypeError because division is not supported for sets

print("dictionary")
print({1:2}/{3:4})
# TypeError because division is not supported for dictionaries
print("\t--"*20)

print("Floor Division of all datatypes:")

print("int")
print(10//3)
# floor division returns integer quotient without decimal

print("float")
print(10.5//2)
# floor division returns largest integer less than result

print("string")
print("Python"//2)
# TypeError because floor division is not supported for strings

print("boolean")
print(True//True)  # True=1 so result becomes 1
print(True//False)  # Error (division by zero)
print(False//True)  # 0

print("complex")
print((2+3j)//(1+2j))
# TypeError because floor division is not supported for complex numbers

print("List")
print([1,2]//2)
# TypeError because floor division is not supported for lists

print("tuple")
print((1,2)//2)
# TypeError because floor division is not supported for tuples

print("set")
print({1,2}//{3,4})
# TypeError because floor division is not supported for sets

print("dictionary")
print({1:2}//{3:4})
# TypeError because floor division is not supported for dictionaries

print("Modulus of all datatypes:")

print("int")
print(10%3)
# modulus returns remainder after division

print("float")
print(10.5%2)
# modulus works with float and returns remainder

print("string")
print("Python"%2)
# TypeError because modulus is not supported for string with integer

print("boolean")
print(True% True)   # True=1 so remainder is 0
print(False % True)  # 0
print(True % 2)      # 1

print("complex")
print((2+3j)%(1+2j))
# TypeError because modulus is not supported for complex numbers

print("List")
print([1,2]%2)
# TypeError because modulus is not supported for lists

print("tuple")
print((1,2)%2)
# TypeError because modulus is not supported for tuples

print("set")
print({1,2}%{3,4})
# TypeError because modulus is not supported for sets

print("dictionary")
print({1:2}%{3:4})
# TypeError because modulus is not supported for dictionaries



print("Different Datatype Arithmetic Operations")

# Integer and Float
a = 10
b = 5.5
print("int + float =", a + b)   # Supported: result is float (15.5)
print("int - float =", a - b)   # Supported: result is float (4.5)
print("int * float =", a * b)   # Supported: result is float (55.0)
print("int / float =", a / b)   # Supported: division always returns float
print("int // float =", a // b) # Supported: floor division removes decimal part
print("int % float =", a % b)   # Supported: returns remainder after division

# Integer and Boolean
a = 10
b = True
print("int + boolean =", a + b)  # Supported: True behaves like 1 → result = 11
print("int - boolean =", a - b)  # Supported: True = 1 → result = 9
print("int * boolean =", a * b)  # Supported: True = 1 → result = 10
print("int / boolean =", a / b)  # Supported: True = 1 → result = 10.0
print("int // boolean =", a // b) # Supported: floor division result = 10
print("int % boolean =", a % b)  # Supported: remainder of 10 % 1 = 0

# Integer and Complex
a = 10
b = 2 + 3j
print("int + complex =", a + b) # Supported: integer converted to complex
print("int - complex =", a - b) # Supported: subtract real and imaginary parts
print("int * complex =", a * b) # Supported: multiply real and imaginary parts
print("int / complex =", a / b) # Supported: division result is complex

# Integer and String
a = 3
b = "Python "
print( a * b) # Supported: string repeats 3 times
# Unsupported operations
print(a + b) # Unsupported: int + string → TypeError because numbers cannot add with string
print(a - b)  # Unsupported: subtraction not allowed between int and string
print(a / b)  # Unsupported: division between int and string not allowed

# Integer and List
a = 2
b = [1,2,3]
print( a * b) # Supported: list repeats two times → [1,2,3,1,2,3]
print(a + b)# Unsupported: integer cannot add with list
print(a - b)# Unsupported: subtraction between int and list not allowed

# Integer and Tuple
a = 3
b = (4,5,6)
print( a * b) # Supported: tuple repeats three times
print(a + b)# Unsupported: integer cannot add with tuple


# Set operations (unsupported for arithmetic)
s1 = {1,2,3}
s2 = {4,5}
print(s1 + s2)# Unsupported: sets do not support + operator
print(s1 * s2)# Unsupported: sets do not support multiplication


# Dictionary operations (unsupported)
d1 = {1:"A"}
d2 = {2:"B"}
print(d1 + d2)# Unsupported: dictionaries cannot be added
print(d1 - d2)# Unsupported: dictionaries do not support subtraction
