a = []
a.append(1)
a.append(2)
a.append(3)
a.insert(0,"4")
a.insert(1,"5")
a.insert(2,"6")
b=[4,5,6,7]
a.extend(b)
print(a)

print(a[0:1])