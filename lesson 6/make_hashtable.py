# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hash=[]
    i=0
    while i<nbuckets:
       hash.append([]) 
       i+=1

    return hash

print(make_hashtable(11))