''' The collectons module implements special counter types with additional functionality to 
 the general bits and containers like dictionaries, lists or tuples. 
 In this file, we'll focus on the following collections: '''
#** Counter, namedtuple, OrderDict, defaultdic and deque'''

# Counter
from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(1)[0][0])
print(my_counter.elements())

