# check_string.py

    
countmax = 5
count = 0

while count != countmax:
   count+=1
   uin = input(" Enter an uppercase word followed by a period. Or enter " "end" " to exit. ")
   upperltrs = uin.upper()
        
   if uin.endswith("end"): 
     print("Exiting")
     count = 5    
   #Upper Letters
   elif uin.isupper() and uin.endswith("."): 
     print("Very good job following directions with your input: ", uin)
   elif uin.isupper()and not uin.endswith("."): 
     print("Upper case is good but missing the period . at the end: ", uin)
   #Lower Letters
   elif uin.islower() and uin.endswith(".") :
     print("Please capitalize your letters.  Having period at the end is good: ", uin)
   elif uin.islower() and not uin.endswith(".") :
     print("Please capitalize your letters.  A period at the end is needed: ", uin)
   #Mixed Upper and Lower Letters   
   elif uin not in upperltrs and uin.endswith(".") :
     print("Please capitalize all of the letters.  Ending with a period is correct.: ", uin) 
   elif uin not in upperltrs and not uin.endswith(".") :
     print("Please capitalize all of the letters.  And add a period at the end.: ", uin)
   
   
   #Numbers  
   elif uin.isdigit() and not uin.endswith(".") :
       print("Please enter letters not numbers followed by a period.  ", uin)
    
    # Figured this was fun to figure out but its odd since the above check operates but the below ck does not.  Dont know how to get below ck to operate. Tried everything for 1.5 hours.
   elif uin.isdigit() and uin.endswith(".") :
       print("Please enter letters not numbers. Having period at the end is good  ", uin)
