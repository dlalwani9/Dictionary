import json
from difflib import get_close_matches
data=json.load(open("data.json",'r'))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
         yn=input("Did u mean %s Instead. Press 'y' for YES and 'n' for NO: " %get_close_matches(word,data.keys())[0])
         if yn=='y' or yn=='Y':
             return data[get_close_matches(word,data.keys())[0]]
         elif yn=='n' or yn=='N':
             return "The Word does not exist.Please Double Check it."
         else:
             return "We didn't Understand your Entry."

    else:
        return "The Word does not exist.Please Double Check it."

flag=0
while flag==0:
    word=input("Enter the word to be searched: ")
    output=translate(word.lower())
    if type(output)==list:
        print("Meaning/Meanings")
        for i in range(len(output)):
            print(i+1,output[i])
    else:
        print(output)
    more=input("Do u want to search again? Press 'y' for YES or 'n' for NO: ")
    if more=='n' or more=='N':
        print("Thank You for Using the Dictionary")
        flag=1
