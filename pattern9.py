count=0
for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            if j==4 and i==4:
                count=count+1
                print(count, end='')
            elif j<=4:
                count=count+1
                print(count, end='')
            else:
                count=count-1
                print(count, end='')               
                    
        else:
            print(end=' ') 
    print()
    count=0           