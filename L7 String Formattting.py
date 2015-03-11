# "{2}, {1}, and {0}".formathttps://github.com/MattR-GitHub/Python1-Repository/wiki("George", "Paul", "John")
#'John, Paul, and George'
#>>> "{who} is a smart {what}".format(what='cookie', who='Sylvia')
#'Sylvia is a smart cookie'
#>>> "The fifth element of the first argument is {0[5]}".format(
#...     ["Dallas", "Zorg", "Cornelius", "Ruby", "Billy", "Leelo"])
#'The fifth element of the first argument is Leelo'


#"Sonny's surname is Bono"
d = {'Cher': "Sarkisian", 'Sonny': "Bono"}
print "Sonny's surname is {0[Sonny]}".format(d)


print "Cher's surname is {lookup[Cher]}".format(lookup=d)
#"Cher's surname is Sarkisian"

for first, last in d.items():
 print("{0:10} {1:10}".format(first, last))

#Cher       Sarkisian
#Sonny      Bono



#fmt = "{0:>6} = {0:>#16b} = {0:#06x}"
#for i in 1, 23, 456, 7890:
 #print(fmt.format(i))

#     1 =              0b1 = 0x0001
#    23 =          0b10111 = 0x0017
#   456 =      0b111001000 = 0x01c8
#  7890 =  0b1111011010010 = 0x1ed2

# Good Answer OBJECTIVE Question one LESSON 7

# OBJECTIVE Question one LESSON 7

my_tuple =((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))
print (my_tuple)
format_results= "{0:>4} = {0:4} x {0:4}"
for (x, y) in my_tuple:
   z = (x*y)
   print(format_results.format(z,x,y))


This fails?

my_tuple =((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))
print (my_tuple)
format_results= "{0:>4} = {0:4} x {0:4}"
for (x, y) in my_tuple:
   
   print (x)
   print (y)
   z = (x*y)
   print(format_results.format(z,(x,y))



 



# End OBJECTIVE Question one LESSON 7
