M=input()
C=""
for i in range (len(M)):
    n=(int(M[i])+1)%10
    C=C+str(n)
print(C)
