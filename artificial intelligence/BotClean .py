def nextMove(posr,posc,board):
    d=0
    #bot position
    bot=5*posr+posc

    #find the dirty cell
    for i in range (5):
        if d == 0:
            a=grid[i]
            a=a.replace(" ","")
            for j in range (5):
                if a[j]=="d" :
                    d=j+i*5
                    break
            

    bota,botb=divmod(bot,5)
    da,db=divmod(d,5)
    s=""
    
    if d==bot:
        s=s+"CLEAN"+"\n"
    if (bota!=da) or (botb!=db):
        if bota>da:
            lig=bota-da
            s=s+"UP"+"\n"
            bota=bota-1
        elif bota<da:
            lig=da-bota
            s=s+"DOWN"+"\n"
            bota=bota+1
        elif botb>db:
            col=botb-db
            s=s+"LEFT"+"\n"
            botb=botb-1
                
        elif botb<db:
            col=db-botb
            s=s+"RIGHT"+"\n"
            botb=botb+1
    return s



r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, 5):
    grid.append(input())

print(nextMove(r,c,grid))


