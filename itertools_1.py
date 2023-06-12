# itertools: product, permutations, combinations, accumulate, groupby, and ifinite iterators
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))



# permutations
from itertools import permutations
c = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))



# combinations
from itertools import combinations, combinations_with_replacement
d = [1, 2, 3, 4]
comb = combinations(d, 2)
print(list(comb))
comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))



# accumulate
from itertools import accumulate
import operator
e = [1, 2, 5, 3, 4]
acc = accumulate(e, fun=max)
print(e)
print(list(acc))


# groupby
from itertools import groupby

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28} ]


group_obj = groupby(persons, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))


# infinite iterators
from itertools import count, cycle, repeat

y = [1, 2, 3, 4]
for i in repeat(1, 4):
    print(i)
    