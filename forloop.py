'''Create a program to display given no is prime or not in many ways using for loop'''
# Way 1 : using count=0 We start range from 1 to end on num+1.
#                       we take end point is num+1 because range stop at  point num-1
num=97
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print(count)
if count==2:  # if count is == 2 then its prime number otherwise not aprime number
    print(num," is a prime number")
else:
    print(num," is  not aprime number")



# Way 2: using count =0 , we start range from 2 and end point is num
#                        # because we know that prime number can divisible by 1 and itself. 
                         # therefore, We start range from 2 and end on num
                         #  This way we can optimize the code than way 1 ,because here we can do less iteration .
num=47
count=0
for i in range(2,num):
    if num%i==0:
        count+=1
if count==0:
       print(num," is a prime number")
else:
    print(num," is  not aprime number")


# Way 3: using count=2 & floor division(//)   we can use floor division that optimzie the code than way 1,way 2.
num=13
count=2
for i in range(2,num//2): # here we use num//2+1 ,the reason behind these as follows 
                            # Any number that can not be divide by more than its half number
    if num%i==0:
        count+=1
if count<3:
       print(num," is a prime number")
else:
    print(num," is  not aprime number")


# Way 4: using   floor division, 
num=17
count=0
for i in range(2,num//2+1): 
    if num%i==0:
        count+=1
if count<1:
       print(num," is a prime number")
else:
    print(num," is  not a prime number")


# Way 5:using Break, - use the break keyword for minimize the number of iterations.
num=18
count=0
for i in range(2,num//2):
    if num%i==0:
        count+=1
        break  #   if condition is true at a first time then break the for loop and print the Number is Not prime
if count>0:
    print(num, " is not a prime number.")
else:
    print(num ," is prime number.")


'''find prime no between 1 to 100'''
for num in range(1,100):           ## It will generate the numbers from 1 to 99
    for i in range(2,num):        ## it will check the number is divisible by 2 to num-1
        if num%i==0:
            break
    else:
        print(num)