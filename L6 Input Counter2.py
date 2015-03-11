/usr/local/bin/python3

new_word_counter = 1
thewords = []                                  # thewords list
themasterlist = []
theset = set()                                 # theset set
mywordset2 = set()
mydict = {}
while True:
    text = input("Please enter a sentence or type nothing and select Enter to end: ") # intitalize set
    if not text:
        break
    for punc in ",?;.":
        text = text.replace(punc," ")       
    for word in text.lower().split():          # text to words
        mywordset2.add(word)                   #add words to set
        #print(wordset2)
        count =len(mywordset2)
        mydict[word] = count                   # adds both
        print (mydict)
        
   # for word in sorted(mydict.items()):      # print loop
    #    print(mydict)  
