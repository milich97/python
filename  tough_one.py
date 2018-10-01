def isInCondition(value):
    count=0
    while(value>0):
        if value%2==1: count+=1
        value//=2
    if count%2==1: return True
    else: return False
    
    from random import randint
n=randint(40,61)
count1=0
count2=0
for i in range(n):
    l.append(randint(-100,102))
    value=l[i]
    if value % 4==3: count1+=1
    if isInCondition(value): count2+=1
    
print(count1)
print(count2)