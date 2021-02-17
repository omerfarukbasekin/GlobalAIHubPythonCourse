import random
a=([0,0,0],[0,0,0],[0,0,0])
i=0

for i in range(3):
    j=0
    for j in range(3):
        asalmi = False
        while asalmi == False: 
            sayi=random.randint(1,100)
            kalan = 0
            sayac = 0
            for n in range (1,(sayi + 1)):
                kalan=sayi % n  # sayı=17 ise 17/1,17/2,17/3,....,17/17 işlemlerini yapar.
                if kalan == 0: #sadece 17/1 ve 17/17 bu if e girer.
                    sayac = sayac + 1
            if sayac == 2:
                a[i][j]=sayi
                asalmi = True   # while döngüsünü sonlanırarak matrix in bir sonraki indisine geçmesini sağlar 
    
print(a)
