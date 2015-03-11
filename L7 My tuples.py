   # OBJECTIVE Question one LESSON 7

my_tuple =((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))
print (my_tuple)
format_results= "{0:>6} = {0:6} x {0:6}"
for (x, y) in my_tuple:
       z = x * y
       print(format_results.format(z,x,y))
