# Find the majority element:-

# Find the majority element:-

list = [4, 83, 2, 5, 93, 4, 5, 3, 93, 4]
from collections import Counter
data = dict(Counter(list))        # {4: 3, 83: 1, 2: 1, 5: 2, 93: 2, 3: 1}


for key, value in data.items():
    max_key = max(data, key = data.get)
print(max_key)