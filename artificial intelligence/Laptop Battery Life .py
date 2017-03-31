import sys

def predict(x):
    if x>=4:
        return 8
    else:
        y=x*2
        return y

timeCharged = float(input().strip())
y=predict(timeCharged)
y=format(y,'.2f')
print(y)
