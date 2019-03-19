"""
	Types of conditional statements:-
comparision operators (==,!=,>,<,<=,>=)
logical operators (and,or,not)
identity operators (is, is not)
membership operators (in, not in)  """

x, y = 2,9
print("Adition", x + y)              
print("multiplication", x * y)  
print("subtraction", x - y)  
print("division", x/y) 
print("Modular", x%y)
print("floor division", x//y) 
print("power: ", x ** y)


# finding a 'number' is there in given list or not
list1 = [22,24,36,89,99]
if 24 in list1:
    print(True)
else:print(False)    

# examples on if elif and else conditions

if x>y:
    print("x is maximum")
elif y>x:
    print("y is maximum")
else:
    print("both are equal")

# Finding the odd and even numbers in given list
list1 = [1,2,3,5,6,33,24,67,4,22,90,99]
for num in range(len(list1)):
    if num % 2 == 0:
        print("Even Numbers are:", num,end=", ")
    else:
        print("The Odd Numbers are:", num)


# Dynamic list using loops

list2 = []
for number in range(10):
    if number % 2 == 0:   # finding Even numbers in given range
        list2.append(number)          
print("Even numbers are:", list2)


# finding all odd numbers within range 40
list1=[]
for num in range(40):
    if num % 2 != 0:
        list1.append(num)

print("odd numbers are", list1)


# Dynamic set

set1 = set()
for number in range(10):
    set1.add(number)
print("numbers in given range are:",set1)

# printing duplicate elements 
list1=[1,1,2,4,4,5,44,56,2,99,49,99]
l=sorted(set(list1))  # removing duplicate elements 
print(l)  
dup_list=[]

for number in range(len(l)):
    if (list1.count(l[number]) > 1):
        dup_list.append(l[number])

print("duplicate elements in a list are: ",dup_list)
