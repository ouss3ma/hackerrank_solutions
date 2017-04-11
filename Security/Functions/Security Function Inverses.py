n = int(input())
s=[int(i) for i in input().strip().split(" ")]
ss=sorted(s)

for i in range (n):
    y=ss[i]
    j=s.index(y)
    print(j+1)
