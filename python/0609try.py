startnumber = 6

# wanted =  int(input("please input number you wanted:\n"))
wanted = 1
cannotbuy = 0
cannotnumber = 0

while True:
    comb = [(x,y,z) for x in range(wanted//6+1) 
        for y in range(wanted//9+1) 
        for z in range(wanted//20+1) 
        if 6*x + 9*y + z*20 == wanted]

    if len(comb) == 0:
        # print(wanted)
        cannotnumber += 1
        cannotbuy = wanted
    elif wanted - cannotbuy > 6:
        print(f'total can not buy numbers is {cannotnumber}')
        print(f'the biggest cannot buy number is {cannotbuy}')
        break

    wanted +=1