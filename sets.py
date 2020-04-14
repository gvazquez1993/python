#SET is a collection of items where NO items are show twice.


s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3) # This one will not be shown. Because is added in the second line.
print(s)
