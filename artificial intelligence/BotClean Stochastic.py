#!/bin/python3
def nextMove(posr,posc,board):
    
    bot=5*posr+posc

    d=0
    for i in range (5):
        a=board[i]
        for j in range (5):
            if a[j]=="d":
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
    
    print(s) 




if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
