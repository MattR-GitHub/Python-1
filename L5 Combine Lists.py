#!/usr/local/bin/python3
words0 = input ("Please Enter a words:").strip().split()
#wordslength=len(words0)
lowerlst = []
upperlst = []

for word in words0:
    if word == word.lower():
      lowerlst.append(word)
      #print("in first if condition lwrlst")
    else:
      upperlst.append(word)
      #print("in elsif condition upperlst")

combinelst = upperlst + lowerlst
for word in combinelst:
   print(word)
   
