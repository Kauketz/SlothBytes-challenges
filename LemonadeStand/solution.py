
def lemonade(bills):
    five = 0
    ten = 0
    
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0: 
                return False
            five -= 1
            ten += 1
        elif bill == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else: 
                return False
                
    return True

print(lemonade([5, 5, 5, 10, 20]))
print(lemonade([5, 5, 10, 10, 20]))
print(lemonade([10, 10]))
print(lemonade([5, 5, 10]))