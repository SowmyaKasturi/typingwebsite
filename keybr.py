# 1.have a list of words
# 2.generate random word paragraph
# 3.move forward only when the correct character is input
# 4.repeat step 2 and 3 for 10 times

import random
from string import ascii_lowercase

#this is forge test
count=0
while count < 10:
    llist=random.sample(ascii_lowercase,5)
    _str = "".join(llist)
    print(_str)
    i = 0
    while True:
        l = input()
        if l == _str[i]:
            i += 1
            if i == len(_str):
                break

    count += 1