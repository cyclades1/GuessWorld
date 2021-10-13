from pprint import pprint
import os
import json
import requests
import random

welcome =''' 
    ####  #   #   #>>>   #""~    #""~    |   #   #    #  ###   ####   ###                         
   #      #   #   #,,,   #,,     #,,     |   #  # #  #  #   #  #  #   #  #  
   #  ##  #   #   #```      #       #    |   # #  # #   #   #  ###    #  #
    ####   ###    #>>>   ">>"    ">>"    |   #     #     ###   #  #   ###    @ @ @                                         
'''

congrats = '''

 ####  ###   ##   #   ####   ####    ###   #####  #""~                           
#     #   #  # #  #  #       #  #   #   #    #    #,,           
#     #   #  #  # #  #   ##  ###    #####    #       #    
 ####  ###   #   ##   #####  #  #   #   #    #    ">>"   @ @ @       
'''


sorry = '''
Sorry... Wrong guess..

'''
print(welcome)
print()
print("Starting the game for you....")
print()

n = 0
while not(n in range(4,8)):
    word = requests.get(url= "https://random-word-api.herokuapp.com/word?number=1").json()[0]
    n = len(word)

word_data = requests.get(url= "https://api.dictionaryapi.dev/api/v2/entries/en/"+word ).json()
define = []

try:
    meaning = word_data[0]['meanings']
    deff = meaning[0]['definitions']

    for i in range(len(deff)):
        define.append(deff[i]['definition'])
except Exception as e:
    define.append('definition not found')


hide = (n+1)//2
hidden = ""
for i in range(n):
    if hide==n-i:
        hidden += "_"
        hide-=1
        continue

    if hide == 0:
        hidden += str(word[i])
        continue

    if random.randint(0, 1):
        hidden += word[i]

    else:
        hidden+="_"
        hide-=1

print("Your word is....")
print(hidden)

if define:
    print("definations: " )
    cnt = 1
    for d in define:
        print(str(cnt)+". "+d)
        cnt+=1
else:
    print("definations not found :/" )

print()

retry = (n+1)//2
success = False

while retry>0:
    user_word = input("Guess the word("+str(retry)+" retries left) : ")
    if user_word == word:
        print(congrats)
        success = True
        break
    else:
        print(sorry)
    retry-=1


if success == False:
    print("Your word is ...")
    print(word)

