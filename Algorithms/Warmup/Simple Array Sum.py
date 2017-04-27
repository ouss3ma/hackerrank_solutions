n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

s=0
i=0
while i<n:
    s=s+arr[i]
    i+=1


print (s)
