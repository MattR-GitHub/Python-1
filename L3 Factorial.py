#!/usr/local/bin/python3
1
2
3
4
5
6
7
8
9
10
11
12
13
#!/usr/local/bin/python3
"""Print all factorials less than 1000."""

c = 0
f = 1
while (f < 1000):
    print(f)
    c += 1
    f = 1
     
    for n in range(c, 0, -1):
      f = f * n
      print(n,f)
