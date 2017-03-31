ph=[15,12,8,8,7,7,7,6,5,3]
hi=[10,25,17,11,13,17,20,13,9,15]
arg_p=float(sum(ph)/len(ph))
arg_h=float(sum(hi)/len(hi))

a=0
b=0
c=0
for i in range (0,len(ph)):
    a=a+(ph[i]-arg_p)*(hi[i]-arg_h)
    b=b+(ph[i]-arg_p)**2
    c=c+(hi[i]-arg_h)**2
    
r=a/((b**(0.5))*(c**(0.5)))

print(r.__round__ (3))
