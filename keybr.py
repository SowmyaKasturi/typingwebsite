# 1.have a list of words
# 2.generate random word paragraph
# 3.move forward only when the correct character is input
# 4.repeat step 2 and 3 for 10 times

import random
from lorem import LoremIpsum

lorem = LoremIpsum()

#this is forge test
count=0
while count < 10:
    llist= lorem.get_sentence(count=10)
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

#     Consider adding a timer to measure typing speed (time module can help).
# Add an accuracy score (e.g., percentage of correctly typed characters).
# Handle edge cases like empty inputs or partial matches.
# Add a difficulty mode: Easy (short sentences), Medium (normal), Hard (long sentences).
# Allow the user to replay and save their best results in a file.
