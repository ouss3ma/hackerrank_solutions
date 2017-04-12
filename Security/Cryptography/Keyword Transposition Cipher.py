def decrypt(k1,c):

#remove duplication
    k=""

    for el in k1:
        if el in k:
                pass
        else:
                k+=el

    n=len(k)
    
    
    d=k
    elements=26
    if 26%n!=0:
            elements=int(26/n)*n+n+1

    
    for i in range(elements):
        if (chr(i+65) in k)==False and i<26:
            d=d+chr(i+65)
        elif i>26:
                d=d+"1"
    


    

    T=[]
    if 26%n==0:
        l=int(26/n)
    else:
        l=int(26/n)+1

    m=0    
    for i in range(l):
        t=[]
        for j in range(n):
                t.append(d[j+m])       
        m=m+n
        T.append(t)
        
    



    

    x=[]
    for i in range(n):
            x.append(k[i])
    x.sort()
    


    


    diff=[]
    for i in range (n):
            T1=T[0][i]
            
            diff.append(T[0].index(T1)-x.index(T1))
    
    



    
    
    T[0].sort()
    for i in range(1,l):
            y=T[i][:]
            for j in range(len(y)):
                    T[i][j-diff[j]]=y[j]
    
    
    


    
    key_chaine=""
    for i in range (n):
            for j in range (l):
                    if T[j][i] !="1":
                            key_chaine=key_chaine+T[j][i]
    

    
    m=""

    for i in range (len(c)):
	    if c[i]==" ":
		    m=m+" "
	    else:
		    
		    o=key_chaine.index(c[i])
		    m=m+chr(o+65)
		    
    print(m)
    
N=int(input())
for i in range(N):
    K=input()
    C=input()
    decrypt(K,C)
