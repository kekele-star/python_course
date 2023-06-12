'''Lists: is a collection of objects
The .pop method is used to return the last element in a list.
other methods include: .remove, .append, .insert, .sort, .reverse, etc

In Python, arrays and lists are two types of data structures that can be used
to store collections of values. Although they are similar in some ways, they 
differ in several important aspects.
Lists can store values of different data types whereas an array can only store values of the same data type
Lists are mutable(can be modified after are created) but arrays are immutable.
LIsts are implemented as dynamic arrays(their size can be changed) but arrays have a fixed-size
'''

# Arrays are more memory-efficient than list when dealing with large collections of values of the same data type
# Arrays are accessed using integer indices, whereas lists can be accessed using integer indices, slices or even boolean arrays.


mylist = ["banana", "cherry", "apple"]
print(mylist)

if "banana" in mylist:
    print("yes")
else:
    print("no")

# appending a new item to a list
mylist.append("lemon")
print(mylist)

mylist.insert(2, "blueberry")
print(mylist)


names = ['Nana Esi', 'Kelvin', 'Hubert']
print(len(names))

# names.insert(0, 'Ella')
#scores = array('d')

#scores.append(97)
#scores.append(98)
#print(scores)
#print(scores[1])

