import os
import time
import random

roll = [ "    \n  * \n    ",
         "   *\n    \n *  ",
         "   *\n  * \n *  ",
         " * *\n    \n * *",
         " * *\n  * \n * *",
         " * *\n * *\n * *"]

c = ''
while c == '':
    c = input('Press enter to roll or type exit to terminate the program : ')
    os.system('cls')
    for j in range(2):
        for i in range(6):
            print(str(roll[i]))
            time.sleep(0.05)
            os.system('cls')
    print(roll[random.randint(0,5)])
    

