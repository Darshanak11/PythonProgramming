my_list=[5,3,8,6,7,2]

new_list=[1,4,9] #adding  new list
my_list.extend(new_list)
print("List after adding new list"my_list)

my_list.sort() #sorting the list
print("List after sorting",my_list)

my_list.reverse() #reversing the list
print("List after reversing",my_list)

element_to_remove=8
my_list.remove(element_to_remove) #removing the element
print("List after removing element:",my_list)
