def rabbits(n):
    L=[1, 1, 2, 3, 5]
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 2
    if n==4:
        return 3
    if n==5:
        return 5
    else:
        i=5
        while i<n:
            a=L[i-1]+L[i-2]-L[i-5]
            L.append(a)
            i=i+1
            
    return L[-1]
    
print rabbits(10)

s = ""
for i in range(1,12):
    s = s + str(rabbits(i)) + " "
print s
