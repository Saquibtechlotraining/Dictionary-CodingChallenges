# Write a program to sort a dictionary in ascending and descending both.
# use d = {'oil':230, 'clip':150, 'stud':175, 'Nut':35}

d = {
    "oil" : 230,
    "clip" : 150,
    "stud" : 175,
    "Nut" : 35
}

print("Original d:", d)
# In Ascending Order:-
print("In Ascending Order:", dict(sorted(d.items())))

# In Descending Order:-
print("In Descending Order:", dict(sorted(d.items(), reverse=True)))

# Explanation (Why we sort a dictionary according to the keys, if keys is a string):-

'''Sorting a dictionary according to the key means arranging the key-value pairs in the dictionary in 
ascending or descending order of the keys. When the keys in the dictionary are strings, the sorting is done 
based on the lexicographic order of the keys, which means the order in which the keys would appear in a dictionary.'''