# Write a program to check whether the dictionary is empty or not:-

dict_1 = {}
size = int(input("Enter the size of dict_1:"))
if size != 0:
    for i in range(0, size):
        key = input("Enter the key:")
        if not key:
            print("dict_1 is empty because there is no key")
            break
        val = int(input("Enter the value:"))
        dict_1[key] = val
        print("dict_1 is not empty:", dict_1)
        break
else:
    print("dict_1 is empty because size of dict_1 is 0")
