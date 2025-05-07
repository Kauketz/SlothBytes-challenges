import re

def noYelling(string):
    return re.sub(r'([!?])\1+$', r'\1', string)


print(noYelling("What went wrong?????????"))
print(noYelling("Oh my goodness!!!"))
print(noYelling("I just!!! can!!! not!!! believe!!! it!!!"))
print(noYelling("Oh my goodness!"))
