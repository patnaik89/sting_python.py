#create list
fruits = ['apple', 'banana', 'cherry']
fruit1 = ['Pine apple', 'Graps', 'Orange']

# extend list
fruits.extend(fruit1)
print(fruits)

# sort list
fruit1.sort()
print(fruit1)

# find dublicate element

my_list = [20,30,20,30,40,50,15,11,20,40,50,15,6,7]
my_list.sort()
print(my_list)

new_list = sorted(set(my_list))
dup_list =[]
for i in range(len(new_list)):
	if (my_list.count(new_list[i]) > 1 ):
		dup_list.append(new_list[i])
print(dup_list)
