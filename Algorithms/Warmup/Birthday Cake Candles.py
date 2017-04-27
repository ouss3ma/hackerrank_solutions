n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
i=0
a=0
s=0
while i< len(height):
    if height[i]>a:
        a=height[i]
    i+=1

j=0
while j< len(height):
    if height[j]==a:
        s=s+1
    j+=1
    
print(s)
