n = int(input())
s=[int(i) for i in input().strip().split(" ")]
test="YES"

for i in range (n):
    y=s[i]
    x=s[y-1]
    if x != (i+1):
        test="NO"
    break
print(test)  
