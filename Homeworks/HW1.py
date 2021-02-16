import random
a=([0,0,0],[0,0,0],[0,0,0])
i=0
for i in range(3):
    j=0
    for j in range(3):
        a[i][j]=random.randint(0,9)
    
print(a)
