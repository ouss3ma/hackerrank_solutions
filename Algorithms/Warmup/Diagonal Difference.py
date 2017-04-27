n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
d1=0
d2=0
for i in range (n):
    d1=d1+a[i][i]
    d2=d2+a[i][n-i-1]
s=abs(d1-d2)
print (s)
