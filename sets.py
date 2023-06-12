# Sets: unordered, mutable, no duplicates
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

#display the union of sets
u = odds.union(evens)
print(u)

#display the intersection of sets
i = odds.intersection(evens)
print(i)


print()

# difference of two sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff= setA.difference(setB)
print(diff)

# symmetric difference
diff= setA.symmetric_difference(setB)
print(diff)

setA.intersection_update(setB)
print(setA)