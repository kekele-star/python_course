''' The collectons module implements special counter types with additional functionality to 
 the general bits and containers like dictionaries, lists or tuples. 
 In this file, we'll focus on the following collections: '''
#** Counter, namedtuple, OrderDict, defaultdic and deque'''

# Counter
'''from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(1)[0][0])
print(my_counter.elements())
'''

# namedtuple
'''from collections import namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1, -4)
print(pt.x, pt.y)
'''

# OrderedDict
'''from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)
'''

# defaultdict
'''from collections import defaultdict
d = {}
d['a'] = 1
d['b'] = 2
print(d['c'])
'''


# deque
'''from collections import deque
d = deque() 

d.append(1)
d.append(2)


d.appendleft(3)
print(d)

d.extendleft([4,5,6])
print(d) 
d.rotate(2)
print(d)'''