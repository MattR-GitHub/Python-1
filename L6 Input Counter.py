#!/usr/lo#!/usr/local/bin/python3

mywordset2 = set()
mydict = {}
while True:
    text = input("Please enter a sentence or type nothing and select Enter to end: ") # intitalize set
    if not text:                                          # no data entry exit
        break
    for punc in ",?;.":                                   # punc out
        text = text.replace(punc," ")       
    for word in text.lower().split():                     # text to words
        mywordset2.add(word)                              #add words to set
        #print(wordset2)
        mycount =len(mywordset2)
        mydict[word] = mycount                              # adds both
        print (mydict)
        
