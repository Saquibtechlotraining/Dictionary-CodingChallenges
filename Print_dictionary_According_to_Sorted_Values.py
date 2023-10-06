# Sort Dictionary According to the values:-

dict_1 = {
    "apple" : 2,
    "cherry" : 1,
    "banana" : 3
}
# here x[1] (i.e, [2, 1, 3] Sort according to values
print(sorted(dict_1.items(), key = lambda x : x[1]))         # [('cherry', 1), ('apple', 2), ('banana', 3)]
print(dict(sorted(dict_1.items(), key = lambda x : x[1])))   # {'cherry': 1, 'apple': 2, 'banana': 3}
print(dict(sorted(dict_1.items(), key = lambda x : x[1], reverse=True))) # {'banana': 3, 'apple': 2, 'cherry': 1}