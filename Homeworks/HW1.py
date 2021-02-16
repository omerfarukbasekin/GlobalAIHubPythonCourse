import random
a=([1,2,3],[4,5,6],[7,8,9])
i=0
for i in range(3):
    j=0
    for j in range(3):
        a[i][j]=random.randint(0,9)
    
print(a)