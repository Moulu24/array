l = [2,7,5]

m = []
i = 0
while i <= len(l): #i is the length of subarray
    for j in range(len(l)-i): #j is the upto which we need to iterate
        k = 0
        a = []
        while k <= i :
            a.append(l[j+k])
            k += 1
        m.append(a)
    i += 1
 
print(*m)