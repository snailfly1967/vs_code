
startP = 2
num = 1
nextP = 2

while(num < 12):
    factor = 2
    nextP += 1
    isP = True
    while(factor < nextP):
        if(nextP % factor == 0):
            isP = False
            factor = 2
            break
        else:
            factor += 1

        
    if(isP):
        print(nextP)
        num += 1




