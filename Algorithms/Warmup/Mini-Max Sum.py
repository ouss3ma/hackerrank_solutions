a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

ma=max(a,b,c,d,e)
mi=min(a,b,c,d,e)

max_value=a+b+c+d+e-mi
min_value=a+b+c+d+e-ma
print(min_value,max_value)
