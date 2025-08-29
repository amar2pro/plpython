#empty list
my_list = []
#append values in the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at the second position in a list
my_list.insert(2,15)
print(my_list)
#extend list with another list 
another_list = [50,60,70]
my_list.extend(another_list)
print(my_list)
#remove the last element from the list
del my_list[-1]
print(my_list)
#sorting the list in ascending order
my_list.sort()
print(my_list)
#the index of 30 in the list 
position = my_list.index(30)
print(position)