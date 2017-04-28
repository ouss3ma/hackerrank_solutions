n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
z=p=ne=0
for i in range (len(arr)):
    if arr[i]==0:z+=1
    elif arr[i]>0:p+=1
    else:ne+=1
print((p/n).__round__(6))
print((ne/n).__round__(6))
print((z/n).__round__(6))
