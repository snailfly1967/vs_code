startnumber = 6

# wanted =  int(input("please input number you wanted:\n"))
wanted = 6
cannotbuy = 7

while True:
    comb = [(x,y,z) for x in range(wanted//6+1) 
        for y in range(wanted//9+1) 
        for z in range(wanted//20+1) 
        if 6*x + 9*y + z*20 == wanted]

    if len(comb) == 0:
        cannotbuy = wanted
    elif wanted - cannotbuy > 5:
        print(cannotbuy)
        break

    wanted +=1