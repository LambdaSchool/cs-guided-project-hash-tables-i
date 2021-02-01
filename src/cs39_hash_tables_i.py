# -*- coding: utf-8 -*-
"""CS39: Hash tables I

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HSFxWbtWFPZGkjRwAjQgkbhyDZCBi6Ms

Hash tables
-----------

Why are they awesome?
* O(1) lookups over the number of items stored in the hash table
* Maps key to value
* Python dict is a hash table


Applications:
* Any time you're doing linear search
* Any time you perform an "expensive" operation, save the result in a hash table
"""

words = ["a", "b", "x", "d", "t", "x", "b", "s", "b"]

# what does the key represent (should be the data you already have)
# what does the value represent (should be the data you want to know)


d = {}

# Sometimes it's worth it up front to spend O(n) time loading a hash table

for w in words:  # O(n) over the number of words
    if w not in d:
        d[w] = 0
    d[w] += 1
    #print(f"We've seen {w} this many times: {d[w]}")


for k in d:  # O(n) over the number of keys in the dictionary, over the number of words
    if d[k] > 1:
        print(f"We found {d[k]} '{k}'s")

# Deduplicate
#
# Return a list of words with no duplicates

words = ["a", "b", "x", "d", "t", "x", "b", "s", "b"]

d = {}

for w in words:
    d[w] = True   # value can be anything


no_dup_words = []

for k in d:
    no_dup_words.append(k)

print(no_dup_words)

words = ["a", "b", "x", "d", "t", "x", "b", "s", "b"]


print(set(words))

cache = {}

def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    if n in cache:
        return cache[n]

    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

for i in range(300):
    print(fib(i))

# Mapping
#['v', 'a', 'd', 'j', 'u', 's', 'k', 'z', 'e', 'g', 'h', 'm', 'n', 'i', 'w', 'r', 'c', 'l', 'q', 'p', 't', 'f', 'y', 'x', 'o', 'b']

encrypt_map = {
    "a": "v",
    "b": "a",
    "c": "d",
    "d": "j",
    "e": "u",
    "f": "s",
    "g": "k",
    # TODO keep going to z
}

def encrypt(word):  # Caesar cipher, crack with "frequency analysis"
    result = ""
    for letter in word:
        result += encrypt_map[letter]

    return result

# challenge: generate the decrypt_map from the encrypt_map

print(encrypt("abc"))  # "vad"
print(encrypt("feeee"))  # "suuu"

# Hash table operations
#   GET - retrieve a value from the hash table, O(1)
#   PUT - store (or replace) a value in the hash table, O(1)

class HashTable:
    def __init__(self):
        self.table = [None] * 32  # where we store values

    def key_to_index(self, key):
        """Hashing function"""
        total = sum(str(key).encode()) 
        index = total % 32

        return index

    def fnv1(self, key):  # O(1) _over the number of items in the hash table_
        fnv_offset_basis = 14695981039346656037
        fnv_prime = 1099511628211

        hash = fnv_offset_basis

        for b in str(key).encode():  # O(n) over the length of the key, O(1) over the number of items in the hash table
            hash *= fnv_prime
            hash &= 0xffffffff
            hash ^= b

        index = hash % 32

        return index

    def put(self, key, value):
        index = self.fnv1(key)
        self.table[index] = value

    def get(self, key):
        index = self.fnv1(key)
        return self.table[index]

ht = HashTable()

ht.put("beej", 3490)   # analogous to d["beej"] = 3490
ht.put("goats", 37)
ht.put("goast", 100)   # collision--goats and goast map to the same index (no collision with fnv1)

print(ht.get("goats"))
print(ht.get("beej"))  # analogous to print(d["beej"])

n = 100
x = 100000000000000

# O(n) _over the value of n_
# O(1) _over the value of x_
for i in range(n):
    print(i)