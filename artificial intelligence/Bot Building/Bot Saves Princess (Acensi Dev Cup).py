def displayPathtoPrincess(n,grid):
    
    for i in range (n):
        a=grid[i]
        a=a.replace(" ","")
        for j in range (n):
            if a[j]=="m":
                me=j+i*n
            if a[j]=="p":
                pe=j+i*n


    ma,mb=divmod(me,n)
    pa,pb=divmod(pe,n)
    s=""
    while (ma!=pa) or (mb!=pb):
        if ma>pa:
            lig=ma-pa
            for i in range(lig):
                s=s+"UP"+"\n"
                ma=ma-1
        elif ma<pa:
            lig=pa-ma
            for i in range(lig):
                s=s+"DOWN"+"\n"
                ma=ma+1
        elif mb>pb:
            col=mb-pb
            for i in range(col):
                s=s+"LEFT"+"\n"
                mb=mb-1
                
        elif mb<pb:
            col=pb-mb
            for i in range(col):
                s=s+"RIGHT"+"\n"
                mb=mb+1

    print(s)
            
        
                  
 


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
