n = int(input())


s=[int(i) for i in input().strip().split(" ")]
test="YES"
for i in range(n):
    for j in range (i+1,n):
        if s[i]==s[j]:
            test="NO"
print (test)
