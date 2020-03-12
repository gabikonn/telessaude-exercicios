a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 45, 55]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 29, 45]

c = []
c = list(set(a).intersection(b))
print(c)

import random

ale1 = random.sample(range(100), 10)
print(ale1)

ale2 = random.sample(range(100), 20)
print(ale2)

ale3 = []
ale3 = list(set(ale1).intersection(ale2))
print(ale3)
