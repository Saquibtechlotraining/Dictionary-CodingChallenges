# Write a program to count the frequency of each word in the given sentence:
# "the quick brown fox jumps over the lazy dog".

sentence = "the quick brown fox jumps over the lazy dog"
list_string = sentence.split()    # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
from collections import Counter
result = Counter(list_string)
print("Frequency of each word:", dict(result))