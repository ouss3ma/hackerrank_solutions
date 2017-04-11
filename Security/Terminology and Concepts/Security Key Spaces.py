M=input()
e=int(input())
C=""

for i in  M:
    n=(int(i)+e)%10
    C=C+str(n)
print(C)
