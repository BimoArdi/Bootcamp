# Bilangan Prima Phyton

def prime (p):
    count=0
    for i in range (1,p+1):
        if (p%i==0):
            count+=1
    if (count==2):
        return "prime"
    else:
        return "flase"

p=int(input("Masukkan Angka :"))
tes= prime(p)
print(tes)

# Tak Kasih komentar