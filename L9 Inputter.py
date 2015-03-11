#inputter.py
f= open('Inputter_DataFile.txt','a')              # open file,  
                                     
while True:
     f = open('Inputter_DataFile.txt','r')        # Display previous content.
     print (f.read())                         
     uin = input("Enter text: ")                  # User input
     f = open('Inputter_DataFile.txt','a')        # open file, to append data 
     f.write(uin)                                 # User input written to file
     #f.close()                                    # close file
     
     if uin == "":                                # break out of loop     
        break
