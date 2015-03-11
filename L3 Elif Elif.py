
countmax = 5
count = 0
while count != countmax: 
  count+=1
  uin = input("Please enter a sentence with a snake name in it:")
  if "python" in (uin):
    print (uin)
    print("At command line I could have inputted PYTHON as well as python drop into this code conditional.... ")
    print("Either upper case or lower case, because  ")
    print("we create a case-insensitive comparison using the lower method. ")
    
  elif uin in ['BOA', 'boa', 'CONSTRICTOR','constrictor']:
    print(uin)
    print (uin,"arghhh.  It's always good to have a professional can check the garden for WRAP U UP dangerious snakes")
  elif "cobra" in uin.lower():
    print("Luckily, cobras are only seen at the Zoo in the northeast")
  elif "rattle" in uin.lower() and "viper" in uin.lower():
    print("Rarily are Rattle Snakes and Vipers found in the northeast.")
  elif "garden" in uin.lower():
    print("Luckily, garden snakes are harmless because they are common in the northeast")
  elif uin.endswith("end"):
    count = 5
    print("Exiting")
  
  else:
    print("Guess Python, Cobras, or rattle snakes are better left unmentioned and unseen. I hate Snakes!")
    print("Try entering  garden snake..they are always at the end of my vegetables row.")
    print("If you wish to End this questioning,  enter the words:  time to end")
  
  if (count == 5):
      print("Going to exit at this count.  Did test this elif,  tested it alone it worked then added the else:, for no entries that match")
      print("The count is :",count, "we have completed asking snake questions")
      
   
   

