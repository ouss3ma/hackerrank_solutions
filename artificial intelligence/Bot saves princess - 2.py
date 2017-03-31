
def nextMove(n,r,c,grid):
    for i in range (n):
        a=grid[i]
        a=a.replace(" ","")
        for j in range (n):
            if a[j]=="p":
                pe=j+i*n
        me=n*r+c

    ma,mb=divmod(me,n)
    pa,pb=divmod(pe,n)
    s=""
    if (ma!=pa) or (mb!=pb):
        if ma>pa:
            lig=ma-pa
            s=s+"UP"+"\n"
            ma=ma-1
        elif ma<pa:
            lig=pa-ma
            s=s+"DOWN"+"\n"
            ma=ma+1
        elif mb>pb:
            col=mb-pb
            s=s+"LEFT"+"\n"
            mb=mb-1
                
        elif mb<pb:
            col=pb-mb
            s=s+"RIGHT"+"\n"
            mb=mb+1
    return s


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

