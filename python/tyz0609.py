
n = 6
can = []
cannot = []
six_consecutive_n = False 

while six_consecutive_n == False:
    combination = [(x,y,z) for x in range(n//6+1) for y in range(n//9+1) for z in range(n//20+1)]

    for a in combination:
        sum = 6*a[0]+9*a[1]+20*a[2]
        purchase = False
        if sum == n:
            purchase = True
            can.append(n)
            n = n +1
            break

    if purchase == False:
        cannot.append(n)
        #print(cannot)
        n = n + 1
    end = len(can)

    if end > 5 and can[-1] - cannot[-1] > 5:
        print(cannot[-1])


    if end > 5:
        lastsix = can[end-6:]
        # print(lastsix)
        first = lastsix[0]
        continues = range(first,first+6)
        if list(continues) == lastsix:
            print(first-1)


    if can[end - 1] -1 == can[end - 2] and can[end - 2] -1 == can[end - 3] and can[end - 3] -1 == can[end - 4] and can[end - 4] -1 == can[end - 5] and can[end - 5] -1 == can[end - 6]:
        six_consecutive_n = True
        # print(can,cannot)
        endd = len(cannot)
        print(cannot[endd-1])
    

        
        
        
        
        
        
        
        
        
        
        
        
        

      