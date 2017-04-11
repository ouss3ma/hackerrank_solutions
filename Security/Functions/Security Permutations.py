n = int(input())
s=[int(i) for i in input().strip().split(" ")]

for i in range (n):
    y=s[i]
    x=s[y-1]
    print(x)
