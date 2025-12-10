'''import keyword
print(keyword.kwlist)'''

#To print name ayehsa
'''n=input("Enter here:")
if n=='ayesha':
    print('Hello Ayesha!')
print('Program ended')
'''
#WAP to check the given value is collection data or not.

'''n=eval(input("Enter here:"))
if type(n) in [str,list,tuple,set,dict]:
    print("Yes it is a collection data type")
print('Program ended')
'''
'''n=eval(input("Enter here:"))
if type(n)==str or type(n)==list or type(n)==tuple or type(n)==set or type(n)==dict: 
    print("Yes it is a collection data type")
print('Program ended')'''

# WAP to check  the given value is single value data type or not.
'''n=eval(input("Enter here:"))
if type(n) in [int,float,complex,bool]:
    print("Yes it is a single data type")
print('Program ended')'''

'''n=eval(input("Enter here:"))
if type(n) not in [str,list,tuple,set,dict]:
    print("Yes it is a single value data type")
print('Program ended')'''
#WAPTC the person is eligible for vote or not

'''age=int(input("Enter here:"))
if age>=18:
    print("Eligible for vote")
print('Program ended')'''

# WAPTC the given string is palindrome or not.
'''n=(input("Enter here:"))
if n==n[::-1]:
    print("Yes it is a palindrome")
else:
    print("It is not a palindrome ")
print('Program ended')'''

#WAPTC the given integer number is palindrome or not using if else
'''print("Program started")
n=int(input("Enter here:"))
if n==int(str(n)[::-1]):
    print("Yes it is a palindrome")
else:
    print("It is not a palindrome ")
print('Program ended')'''

#WAPTC the given string is upper case or not.
'''print("Program started")
n=input("Enter here:")
if n.isupper():
    print("Yes it is upper case")
else:
    print("It is not upper case ")  
print('Program ended')
'''
#OR
'''n='D'
if 'A'<=n<='Z':
    print("Yes it is upper case")
else:
    print("It is not upper case ")
print('Program ended')   '''
'''madhu=[10,20,30,40]
print(madhu[0:4:2])'''
'''l=(input("Enter a number:"))'''


# WAPTC the entered value is in uppercase or lowercase or digit or special character.
'''n=input("Enter here:")
if 'A'<=n<='Z':
    print("It is uppercase")
elif 'a'<=n<='z':
    print("It is lowercase")
elif '0'<=n<='9':
    print("It is digit")
else:
    print("It is special character")
print('Program ended') '''   

# WAPTC whenever the user enters a number, check whether the number represents the day of the week which starts 
# from sunday as 1 to saturday as 7, and print the corresponding day name. 
# If the number is out of range, print "Invalid Input".
'''n=int(input("Enter here:"))
if n==1:
    print("Sunday")
elif n==2:
    print("Monday")
elif n==3:
    print("Tuesday")
elif n==4:
    print("Wednesday")
elif n==5:
    print("Thursday")
elif n==6:
    print("Friday")
elif n==7:
    print("Saturday")
else:
    print("Invalid Input")
print('Program ended')  '''  

# WAPT remove all the duplicate values from the given list .
'''l=[1,2,2,3,4,4,5,6,7]
v=list(set(l))
print(v)'''

#WAPT remove all the duplicate values from the given list without using set()
'''l=[1,2,2,3,4,4,5,6,7]
d={}.fromkeys(l)
{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
print(list(d))'''

#Game of ROCKS, PAPER, SCISSORS
'''import random
l=['rock','paper','scissors']
c=random.randint(1,2)
user=input("Enter your choice (rock/paper/scissors): ")
if user.lower() =='rock' and l[c]=='paper':
    print("User wins")
elif user.lower() =='rock' and l[c]=='scissors':
    print("Computer wins")
elif user.lower() =='paper' and l[c]=='scissors':
    print("Computer wins")
elif user.lower() =='paper' and l[c]=='rock':
    print("User wins")
elif user.lower() =='scissors' and l[c]=='rock':
    print("Computer wins")
elif user.lower() =='scissors' and l[c]=='paper':
    print("User wins")
elif user.lower() ==l[c]:
    print("It's a tie")
else:
    print("Invalid input")
print(f"Computer chose: {l[c]}")'''

# WAP to check the entered character is special character or not without using not operator.
'''n=input("Enter here:")
if ('A'<=n<='Z' or 'a'<=n<='z' or '0'<=n<='9'):
    print("It is not special character")
else:
    print("It is special character")'''

# WAP to check the entered character is special character or not.
'''n=input("Enter here:")
if not ('A'<=n<='Z' or 'a'<=n<='z' or '0'<=n<='9'):
    print("It is special character")
else:
    print("It is not special character")'''
#example for nested if.
'''user= input("enter username:")
if user=='Tamil':
    print("Username matched.")
    u_password=input("enter passwrod:")
    if u_password=='Tamil143':
        print("login Successfull")
    else:
        print("Invalid passwrod")
else:
    print("Invalid username.")'''

# WAPTC the given integer number is positive or not 
# if the given int is positive check the number is even or odd number
'''print("Program started")
n=int(input("Enter here:"))
if n>0:
    print("Positive number")
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")'''

# WAPTC the given character is alphabet or not 
# if given char is alphabet check it is a vowel or consonant.
#Wrong
'''n=input("Enter here:")
if len(n)==1:
    if 'A'<=n<='Z' or 'a'<=n<='z':
        print("The character is alphabet.")
        if n in 'AEIOUaeiou':
            print("The character is a vowel")
        else:
            print("The character is not a vowel")
else:
    print("The given character is not an alphabet")'''

#Correct
'''n=input("Enter here:")
if len(n)==1:
    if 'A'<=n<='Z' or 'a'<=n<='z':
        print('Alphabet')
        if n in 'AEIOUaeiou':
            print("The given char is vowel")
        else:
            print("The given character is consonant")
    else:
        print('Not alphabet')
else:
    print('Pls enter one char')'''

# WAPTC the given integer number is triple digit or not.
# If it is a triple digit check it is divisible by 2 or not.
'''n=int(input("Enter here:"))
if n>99 and n<100 or n<-99 and n>-1000:
    print("The given number is triple digit")
    if n%2==0:
        print("Divisible by 2")
    else:
        print('Not divisible')
else:
    print("Please enter 3 digits")'''

#WAPTC You’re building a tiny access-control system for a college event. Nothing fancy,
# just a Python script acting all self-important like it’s guarding the gates of heaven.

'''First check if the person has a valid entry pass.

If they do, check their category: student, volunteer, or guest.

If they’re a student, then check if they’ve paid the event fee.

If they’re a volunteer, allow free entry.

If they’re a guest, check if their host student is present.

If they fail any of these checks, the gatekeeper (your code) throws a polite digital tantrum: access denied.'''

'''n=input("Enter here:")
if n=='student':
    print("Valid entry pass")
    if n=='volunteer':
        print("Fees paid or not")
    elif n=='guest':
        print("Skip extra checks")
    else:
        print("give your host name")
else:
    print("Not allowed")'''

'''n=input("Enter here:")
if len(n)==1:
    match n:
        case'+':
            n1=int(input("Enter here:"))
            n2=int(input("Enter number"))
            print(n1+n2)
        case _:
            print("invalid symbol:")
'''
'''for i in range(0,10,2):
    print(i)'''
    
'''for i in range(50,2,-1):
    print(i)'''

'''for i in range(2,30):
    print(i)'''
'''for i in range(20):
    print(i)'''
# WAPT print ten even numbers by using for loop
'''for i in range(0,20,2):
    print(i)'''
# WAPT print first ten odd numbers by using for loop
''''for i in range(0,22,3):
    print(i)'''
# WAPT print first ten even numbers by using for loop without updating step value
'''for i in range(23):
    if i%2==0:
        print(i)'''
# WAPT print *
#            **
#            ***
'''n= int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(i*'*')'''
'''
for i in range(1,6):
    print(i)'''

'''n=int(input("Enter here:"))
for i in range(1,n):
    if i !=n-1:
        print(i,'*',end=" ")
    else:
        print(i)'''
#WAP to print all the numbers from the exisiting list by using range function
'''l=[10,20,30,40,50,60,70,80,90]
for i in range(len(l)):
    print(l[i])'''
#WAP to print each element of the list in a single line
'''l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    if i !=len(l)-1:
        print(i,'*',end=" ")
    else:
        print(i)'''
    
#WAP to print only integer elements in the existing list  
'''l=(0,'Chennai',20.10,(1+2j),20,{1:20},('Rcb','Csk'),30)
for i in l:
    if type(i)==int:
        print(i)
'''
#WAP to print all numeric datatype elements in the existing string
'''l=(0,'Chennai',20.10,(1+2j),20,{1:20},('Rcb','Csk'),30)
for i in l:
    if type(i)==int or type(i)==float or type(i)==complex:
        print(i)
'''
#WAPTP all the even numbers in the existing string
'''n=[1,2,3,4,5,6,7,8,9,10]
for i in n:
    if i%2==0:
        print(i)
'''
#WAPT count how many odd numbers and how many even numbers are present in the existing list.
'''n=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(n)):
    if i%2==0:
        print(i)'''
'''l=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for i in l:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)
'''
                #OR
'''l=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for i in l:
    if type(i)==int:
        if i%2==0:
            even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)
'''

#WAPT print square of each number in the existing list
'''l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i**2)'''
#WAPTP sum of n natural numbers
'''n=int(input("Enter here:"))
sum_n=0
for i in range(1,n+1):
    sum_n+=i'''

#WAPTP factorial of a given integer number
'''n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
    print("Factorial of", n, "is", fact)'''

#WAPTP each element from the existing collection by using range function.
'''l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    if i !=len(l):
        print(i)
    else:
        print("Invalid input")'''

#WAPTP the string in reverse order without using slicing or reverse only using range.
'''l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)-1,-1,1):
    print(l[i])'''

# WAPTP each element from the existing tuple collection by using range function.
'''T=(10,'python','sython','ajay',30.10)
for i in range(len(T)):
    print(T[i])'''
#WAPTP
'''st=(100,200,'sql',('sam','rakul'),(1+2j))
for i in st:
    print(i)'''
#DICTIONARY
'''d={'name':'gowtham','age':32,'DOB':'20-11-2004','phone':98348239876}
for i in d:
    print(i)'''
#WAPTP only values from the existing dictionary collection by using built in method.
'''d={'name':'gowtham','age':32,'DOB':'20-11-2004','phone':98348239876}
for i in d.values():
    print(i)
'''
#WAPTP only values from the existing dictionary collection without using built in method.
'''d={'name':'gowtham','age':32,'DOB':'20-11-2004','phone':98348239876}
for i in d:
    print(d[i])'''
#WAPTP each key value pair from the existing dictionary in the format of "name=gowtham"
'''d={'name':'gowtham','age':32,'DOB':'20-11-2004','phone':98348239876}
for i in d:
    print(i,'=',d[i])'''
#Looping through string.
'''s='Python'
for i in s:
    print(i)'''
#WAPTP each character from the existing string data type by using range function.
'''s='PYTHON'
for i in range(len(s)):
    print(s[i])'''
#WAPTP while loop
'''i=1
while i<=10:
    print(i)
    i+=1'''
#WAPTP first ten even numbers using while loop
'''i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1
'''
#OR
'''i=2
while i<=20:
    print(i)
    i+=2'''
#WAPTP reverse of a number(Assignment 1-50)
'''i=50
while i>=1:
    print(i)
    i-=1'''

'''s1={1,2,3,4,5,6}
s2={23,4,5,6,78,9,0}
s3=s1.union(s2)
print(s3)'''
'''keys = ["name", "age", "city"]
d = dict.fromkeys(keys)
print(d)'''
#Create a txt file to get user integer value and fetch data accordung to the input if user = 1 fetch the first line etc
'''n=int(input("Enter here:"))
if n>0:
    print("The number is greater than 0")
    new=input("The number is greater than 20")
    if new=='The number is greater than 20':
        print("The number is one")
else:
    print("The number is not one")'''
#WAPT fetch first ten even numbers by using range function and store ten even numbers in a new list.
'''x=[]
for i in range(2,21,2):
    x.append(i)
print(x)'''
'''n=[]
for i in range(2,21):
    if i%2==0:
       n.append(i)
    print(i)'''
#Nested for loop
'''for i in range(5):
    for j in range(5):
         print(i,j)'''
#nested while loop
'''i=0
while i<=5:
    j=0
    while j<=5:
        print(i,j)
        j+=1
    i+=1'''
'''for i in range(6):
    if i==4:
        break
    print(i)'''
'''for i in range(6):
    for j in range(6):
        if j==3:
            break
        print(i,j)'''
'''i=0
while i<=5:
    if i==2:
        break
    print(i)
    j=0
    while j<=5:
        if j==2:
            break
        print(j)
        j+=1
    i+=1
    break'''
'''for i in range(6):
    if i==3:
        print("Condition true")
    print(i)
    print("If condition ended")'''

'''for i in range(6):
    if i==3:
         print("Condition true")
         continue
    print(i)
    print("If condition ended")
'''
#28.11.25
'''row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
for i in range(1,row+1):
    for j in range(col):
        print(i)
    print( )'''

'''row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=" ")
    print()
    val+=1
    if val>9:
        val=1'''

'''n=int(input("Enter number of rows:"))
for i in range(n):
    val=1
    for j in range(n):
        print(val,end=" ")
        val+=1
    print()'''

'''n=int(input("Enter number of rows:"))
val=1
for i in range(n):
    for j in range(n):
        print(val,end=" ")
        val+=1
        if val>9:
            val=1
    print()'''

'''n=int((input("Enter value:")))
val=65
for i in range(n):
    for j in range(n):    
        print(chr(val),end=" ")
    print()
    val+=1
    if val>90:
        val=65'''

'''n=int((input("Enter value:")))
for i in range(n-1):
    val=65
    for j in range(n):    
        print(chr(val),end=" ")
        val+=1
        if val>90:
            val=65
    print()'''
#29.11.25
'''rows=int(input("Enter here:"))
val=4
x=val       
for i in range(rows):    
    for j in range(rows-1):
        print(val+x, end=" ")
    print()
    val-= 1  '''   

'''rows=int(input("Enter here:"))
cols=int(input("Enter here:"))
for i in range(rows): 
    val =4 
    x=val-1  
    for j in range(cols):
        print(val+x, end=" ")
        val -= 1
    print()'''
    
'''rows=int(input("Enter here:"))
cols=int(input("Enter here:"))
val =68 
x=val-1       
for i in range(rows):    
    for j in range(cols):
        print(chr(val+x), end=" ")
    print()
    val -= 1'''

'''rows=int(input("Enter here:"))
cols=int(input("Enter here:"))
for i in range(rows): 
    val =68   
    x=val-1
    for j in range(cols):
        print(chr(val)+x, end=" ")
        val -= 1
    print()'''

'''n=int(input("Enter here:"))
val=n
if val>9:
    val=9
for i in range(n):
    for j in range(n):
        print(val,end=" ")
    print()
    val-=1
    if val<1:
        val=9'''

'''n=int(input("Enter here"))
for i in range(n):
    val=65+n-1
    for j in range(n):
        print(chr(val),end=" ")
        val-=1
    print()'''

'''n=int(input("Enter here"))
for i in range(1,n+1):
    for j in range(n):
        print(i,end=" ")
    print( )
    print("* "*n)'''
#OR
'''n=int(input("Enter the rows and col:"))
val=1
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(val,end=" ")
        else:
            print("*",end=" ")
    print()
    if i%2==0:
        val+=1'''

'''n=int(input("Enter the rows and col: "))
for i in range(n):
    val=1
    for j in range(n):
        if j%2==0:
            print(val,end=" ")
            if j%2==0:
                val+=1
        else:
            print("*",end=" ")
    print()
    '''
#02-12-2025
#14 right angle triangle pattern
'''print('\n\t\t\t14 -> right angle triangle pattern program\n') 
n=4 
for i in range(n): 
    for j in range(n): 
        if i>=j: 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
    print() '''
#15 single middle line pattern
'''print('\n\t\t\t15 -> single middle line pattern \n') 
n=5 
for i in range(n): 
    for j in range(n): 
        if i==j: 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
    print()'''

#16 single middle line pattern in reverse
'''print('\n\t\t\t16 -> single middle line pattern in reverse\n')
n=5
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()'''

#17 x pattern
'''print('\n\t\t\t17 -> x pattern\n')
n=5
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()
'''
'''n = int(input("Enter size of square: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or (i==n//2 and j==n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

'''n = int(input("Enter size of square: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or (i==n//2 and j==n//2) or i+j==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

'''n = int(input("Enter number: "))
for i in range(1,11):
    print(5, "x", i, "=", 5 * i)'''

'''n=int(input("Enter here:"))
i=1
while i<=10:
    print(n, "x", i, "=", n * i)
    i+=1'''
#4.12.25
'''n=5 
for i in range(n): 
    for j in range(n): 
        if i+j<=n-1: 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
    print()'''


'''n=5 
for i in range(n):
    for j in range(n): 
        if i+j>=n-1: 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
    print()'''

'''n=5 
for i in range(n): 
    for j in range(n): 
        if i<=j: 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
    print()'''
'''
n=5
for i in range(n):
    for j in range(n):
        if i==j or i==n-1 or j==0:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()'''

'''n=5
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==0 or j==0:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()'''

'''rows=int(input("Enter here:"))
cols=int(input("Enter here:"))
for i in range(rows):
    for j in range(cols):
        if j==0 or i==j or i+j==rows-1:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()'''
#OR
'''n=int(input("enter here:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or i+j==n*2-2:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()'''

'''n=int(input("Enter here:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i*2):
        print("*",end=" ")
    print()'''

'''n=int(input("enter here:"))
for i in range(n):
    for j in range(n*2-1):
        if i+j==n-1 or j-i==n-1 or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()'''
#Practice
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==n-1 or j==0:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()'''
#Example using single for loop
'''n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        # Print the full top or bottom row
        print("* " * n) 
    else:
        # Print the hollow middle rows
        # 1 star, then (n-2) double-spaces, then 1 star
        print("* " + "  " * (n - 2) + "* ")'''
#Diamond

'''n=5 
for i in range(n):
    for j in range(n):
        if (i+j==n-1 and i<=2) or (i<n-1 and j<n-3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#5.12.25

'''n=int(input("Enter here:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i*2):
        print("*",end=" ")
    print()'''

'''n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))'''

'''n = int(input("Enter here:"))
# top half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        if k == 1 or k == i * 2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# bottom half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        if k == 1 or k == i * 2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
#6.12.25
#WRAP to check the given integer number is prime number or not
'''n=int(input("Enter here:"))
count=0
for i in range(2,n//2+1):
    if n%i==0:
        count+=1
        break
if count==0:
    print("Prime number")
else:
    print("Not a prime number:")'''

#WAPTP all the prime numbers between 1 to n
'''n = int(input("Enter here:"))
for num in range(2, n + 1):
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)'''
#WAPT find the nth prime number
'''n=int(input("Enter here:"))
prime_count = 0
for i in range(2,100000):
    count = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
    if count == 0:
        prime_count+=1
        if prime_count==n:
            print(i)
            break'''
#8.12.25
#WAPT convert decimal number to binary number.
'''n=int(input("Enter here:"))
binary=0
temp=1
while n!=0:
    remainder=n%2
    binary=binary+remainder*temp
    temp=temp*10
    n=n//2
print(binary)'''
#WAPT convert binary number to decimal number.
'''n=int(input("Enter here:"))
decimal=0
temp=1
while n!=0:
    remainder=n%10
    decimal=decimal+remainder*temp
    temp=temp*2
    n=n//10
print(decimal)'''
#WAPT count number of digits present in the given integer number without converting into string.
'''n=int(input("Enter here:"))
count=0
while n!=0:
    count+=1
    n=n//10
print(count)'''
#WAPTC the given integer number is perfect number or not.
'''n=int(input("Enter here:"))
count=0
for i in range(1,n):
    if n%i==0:
        count+=i
if count==n:
    print("Perfect value")
else:
    print("Not perfect value")'''
#WAPTP perfect numbers between the one to n range.
'''n=int(input("Enter here:"))
for i in range(1, n + 1):
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += j
    if count == i:
        print(i)'''
#9.12.25
#WAPTC the given integer number is a armstrong ex:153 must be equal to 1^3+5^3+3^3 number or not.
'''
n = int(input("Enter here: "))

temp = n
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** 3
    temp //= 10

if sum_val == n:
    print("Armstrong value")
else:
    print("Not Armstrong")'''

#WAPTP even numbers count and odd numbers count from the given integer number.

'''
n = int(input("Enter here: "))

even_count = 0
odd_count = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)'''

#WAPTC the given integer number is strong number or not.

'''
n = int(input("Enter here: "))
temp = n
total = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    total += fact
    temp //= 10

if total == n:
    print("Strong number")
else:
    print("Not strong")
'''
#10.12.25
#WAPT extract each element from the existing list
'''l=(input("Enter here:"))
for i in l:
    print(i)
'''
#WAPT extract even values seperately and odd values seperately from the existing list data type
'''l=[input("enter here:")]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)'''
#WAPT extract sum of even numbers and sum of odd numbers from the existing list
'''l=['a',10,3.5,(3+1j),2,3,[1,2],13]
even=0
odd=0
for i in l:
    if type(i)==int:
        if i%2==0:
            even+=i
        else:
            odd+=i
print(even)
print(odd)'''
#WAPT remove duplicate values from the existing list
'''l=[1,2,3,4,5,6,3,4,2,4,2]
print(list(set(l)))'''
#WAPT remove duplicate values from the existing list without type casting into set data type
'''l=[1,2,3,4,5,6,3,4,2,4,2,'mahi','mahi','sython']
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)'''
#WAPT print minimum element in the existing list
'''l=[1,2,3,3,3,4,4,5,3,3,4,5,5,9]
l.sort()
print(l[0])'''
#WAPTP maximum integer element in the existing list
'''l=[1,2,3,3,3,4,4,5,3,3,4,5,5,9]
l.sort()
print(l[-1])'''
#WAPTP minimum and maximum element in the existing list
'''l=[1,2,3,3,3,4,4,5,3,3,4,5,5,9]
l.sort()
print(l[0],l[-1])'''
#WAPTP second minimum element from the exisiting list
'''l=[1,1,1,2,3,3,3,4,4,5,3,3,4,5,5,9]
l2=list(set(l))
l2.sort()
print(l2[1])'''
#assignment write the above program in another method.
#WAPT arrange all the elements in ascending order without using sort built in method.
'''l=[1,3,2,9,7,2,3,9,0,82]
for i in range(len(l)):
    for j in range(1+i,len(l)):
        if l[j]<l[i]:
            l[j],l[i]=l[i],l[j]
print(l)'''
