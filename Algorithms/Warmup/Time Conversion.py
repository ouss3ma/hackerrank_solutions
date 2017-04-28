time = input().strip()
h=time[:2]
am_pm=time[8:]

if am_pm=="AM":
    if h=="12":time="00"+time[2:8]
    else:time=time[:8]
else:
    if h=="12":time=time[:8]
    else:time=str(int(h)+12)+time[2:8]

print(time)
