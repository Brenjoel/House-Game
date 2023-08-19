# import pronouncing as p
# res=p.rhymes("Shine")
# print(res)

# Import the required module for text
# to speech conversion
from turtle import delay
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os


import random,time
from colorama import Fore,Style,Back
l=[i for i in range(1,101)]
m=[]
while (len(l)):
    try:
        print(Style.RESET_ALL)
        a=int(random.choice(l))
        l.remove(a)
        m.append(a)
        # print(sorted(m))

    # if ch=='s':
        print(Fore.GREEN)


        mytext = "   "+str(a)+"    "
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=True)
        myobj.save("number.mp3")
        os.system("number.mp3")

        print(a)
        print(Style.RESET_ALL)
        time.sleep(5)
        # delay(5000)

        # if ch=='e' or ch=='E':
        #     print(Fore.YELLOW+"You ended the game")
        #     print(Style.RESET_ALL)
        #     break
    except :
        print(Style.RESET_ALL)
        print("-----------\n1.Print previous elements\n2.Print Remaining elements\n0.Exit")
        ch=int(input())
        if ch==1:
            print(sorted(m))
            input("press any Key to continue: ")
            continue
        elif ch==0:
            break
        elif ch==2:
            print(sorted(l))
            input("Press anu key to continue: ")
            continue
        else:
            continue
        
        

    




           
