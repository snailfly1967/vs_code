
startP = 2
num = 1
nextP = 2
print(num,startP)
while(num < 100):
    factor = 2
    nextP += 1
    isP = True
    while(factor <= nextP/2):
        if(nextP % factor == 0):
            isP = False
            break
        else:
            factor += 1

        
    if(isP):
        num += 1
        print(num,nextP)
        
        

print(nextP)



