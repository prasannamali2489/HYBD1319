# question 1
'''table of any number using for loop in function programming'''
def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = ",num*i)
table(int(input("Enter a number :")))
'''
Enter a number :5
5 * 1 =  5
5 * 2 =  10
5 * 3 =  15
5 * 4 =  20
5 * 5 =  25
5 * 6 =  30
5 * 7 =  35
5 * 8 =  40
5 * 9 =  45
5 * 10 =  50'''


# question 2
'''check given number is palindrom or not'''
def palindrom(num):
    num=str(num)
    if num==num[::-1]:
        print(f"{num} is palindrom")
    else:
        print(num," is not palindrom")
palindrom(int(input("Enter a number :")))
'''
122  is not palindrom
122  is not palindrom
'''


# question 3
'''reverse the list'''
#way1
lst=[1,2,3,4,5,7,9,10]
def reverselist(lst):
    lst2=[]
    for i in lst:
        lst2=[i] + lst2
    print("reversed list is ",lst2)
reverselist(lst)
'''[10, 9, 7, 5, 4, 3, 2, 1]'''

# way2
def list(lst):
    print("reversed list is ",lst[::-1])
list([1,2,33,45,55])
'''reversed list is  [55, 45, 33, 2, 1]'''


# question 4
'''print right angle triangle'''
# Way1:
def RAT(n):
    for r in range(1,n+1):
        for c in range(1,r+1):
             print("*",end=" ")
        print()
RAT(int(input("Enter a number for Pattern Printing :  ")))

# Way2:
def pattern1(n):
    for i in range(1,n+1):
        print("* "*i)
pattern1(int(input("Enter a number for Pattern Printing :  ")))
'''
Enter a number for Pattern Printing :  5
* 
* *
* * *
* * * *
* * * * *
'''

# question 5
'''reverse right angle triangle'''
def pattern2(n):
    for i in range(1,n+1):
         print(" "*(n-i),"*"*i)
pattern2(int(input("Enter a number for Pattern Printing :  ")))
'''
Enter a number for Pattern Printing :  7
       *
      **
     ***
    ****
   *****
  ******
 *******
'''


# question 6
def pattern3(n):
    for i in range(n,0,-1):
        print("*"*i)
pattern3(int(input("Enter a number for Pattern Printing :  ")))
'''
Enter a number for Pattern Printing :  3
***
**
*
'''

# question 7
'''square pattern'''
def pattern4(n):
    for i in range(1,n+1):
        for j in range(n,0,-1):
             print("* ",end=" ")
        print()
pattern4(5)
'''
*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
'''
def pattern5(n):
    for r in range(1,n+1):
        for c in range(1,n+1):
            print("* ",end=" ") if r==1  or c==1 or c==n or r==n else print("  ",end=" ")
        print()
pattern5(5)
'''
*  *  *  *  *  
*           *  
*           *
*           *
*  *  *  *  *
'''

# question 8
'''Prime number'''
def prime(n):
    count=0
    for  i in range(2,n):
        if n%i==0:
            count+=1
            break
    if count==0:
        print(n," is a prime number")
    else:
        print(n," is not a prime number")
prime(int(input(" Enter a number : ")))
'''
 Enter a number : 19
19  is a prime number

 Enter a number : 22
22  is not aprime number

'''


