t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
t2 = [1, 2, 3
#[1, 2, 3, 1, 2, 5, 6, 7, 8]
x = list(set(t))
#[1, 2, 3, 5, 6, 7, 8]
s = [1, 2, 3]
list(set(t) - set(s))
z = list(set(t) - set(s))
print(z)
[8, 5, 6, 7]
print(set(t))
print(x)
