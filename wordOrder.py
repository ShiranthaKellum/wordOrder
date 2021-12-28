from collections import Counter

str = []
n = int (input ())
for i in range (n):
    str.append (input ())

print (len (Counter (str)))
# print (Counter(str).values ())
for i in Counter(str).values ():
    print (i, end=" ")