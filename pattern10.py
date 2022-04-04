for i in range(1,6):
    for j in range(1,10):
        if j>=6-i and j<=4+i:
            if i%2!=0:
                if j%2!=0:
                    print("*", end='')
                else:
                    print(end=' ')
            elif j%2==0:
                print("*",end='')
            else:
                print(end=' ')                
        else:
            print(end=' ')    
            
    print()        