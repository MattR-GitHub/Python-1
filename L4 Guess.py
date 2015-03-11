# check_string.py
import random
countmax = 5
count = 0
secretnumber = random.randrange(1, 20, 1)
print (secretnumber)
guess = 0

while (guess != secretnumber) and (count!=5):
   count+=1
   guess = int(input(" Guess a number beween 1 and 20: "))  
   
   if (guess < secretnumber)and (count!=5):
     print("Guess Higher")
   if (guess > secretnumber)and (count!=5):
     print("Guess Lower")
   if (guess == secretnumber): 
     print("Very good job guessing correctly the number", guess)
     count = 5
   elif (count==5):
      print("Very good try guessing! The correct number was", guess)
 
