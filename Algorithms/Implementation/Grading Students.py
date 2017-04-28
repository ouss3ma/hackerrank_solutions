def solve(grades):
    # Complete this function
    l=[]
    for i in range (len(grades)):
        if grades[i]<38:
            l.append(grades[i])
        else:
            if grades[i] % 5 < 3:
                l.append(grades[i])
            else:
                l.append(grades[i]+5-grades[i]%5 )
    return l
        

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
for i in result:
    print (i)
