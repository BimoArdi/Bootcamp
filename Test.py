# p = int (input("Masukkan Nilai P"))
# r = int (input("Masukkan Nilai R"))
# n = int (input("Masukkan Nilai N"))
# b = int (input("Masukkan Nilai B"))
# Nilai = r/n
# Nilai+= 1
# Nilai**=b
# Nilai*= p
#
# nilai = p*((1+(r/n))**b)
#
# print Nilai, nilai

# a = 10
# if (a>0) and (a<10):
#     print("Ciee Ciee")
# else:
#     print ("Week :P")
#


# if((a > 0) and (a < 10)):
#      print("Ciee Ciee")
# elif (a == 5):

#     print ("Week :P")
# else:
#     print ("Minus")


# def serahgue(p):
#     if (p.upper() == "BIMO"):
#         print ("Sama")
#     else:
#         print ("Tidak Sama")
#
# p = str(input("Masukkan Nilai P"))

# print(serahgue(p))

# Perulangan For
# for i in range(10):
#     print(i)

# kalimat= "Hellow Word"
# for i in kalimat:
#     print(i)

# Perulangan while
# i=0
# while i<10:
#     print(i)
#     i+=1
#

b= int(input("Masukkan Angka"))
# Tugas 1 Setengah Wajik
for r in range (b):
    r+= 1
    print("*" * (r))
for r in reversed(range(b)):#Buat 5 sampai 1
    r-=0
    print("*" * (r))

# Tugas Jam Pasir
for x in range(b):
    for k in reversed(range(x + 1)):
        print(" ", end= "")
    for j in range( b -x):
        print("*", end= "")
    for m in reversed(range(b-(x+1))):
        print("*", end= "")
    print("*"*(r))

for x in reversed(range(b)):
    for k in range(x + 1):
        print(" ", end= "")
    for j in reversed(range( b - (x+1))):
        print("*", end= "")
    for m in range(b-x):
        print("*", end= "")
    print()
print()

# Wajik
for x in reversed(range(b)):
    for k in range(x + 1):
        print(" ", end= "")
    for j in reversed(range( b - (x+1))):
        print("*", end= "")
# Buat Balik
    for m in range(b-x):
        print("*", end= "")
    print()
# Buat yang segitiga

for x in range(b):
    for k in reversed(range(x + 1)):
        print(" ", end= "")
    for l in range( b - x):
        print("*", end= "")
    for m in reversed(range(b-(x+1))):
        print("*", end= "")
    print()
print()
# Buat Yang Bawah

for i in range (b):
    for k in range (b):
        print("* ",end= "")
        if (1==i%2):
            print("# ",end="")
        elif(0==i%2):
            print("# ",end="")
    print()
    for k in range (b):
        print("# ",end= "")
        if (1==i%2):
            print("* ",end="")
        elif(0==i%2):
            print("* ",end="")
    print()
print()

    # Buat Papan Catur

for i in range (b):
    for k in range (b):
        print("** ",end= "")
        if (1==i%2):
            print("## ",end="")
        elif(0==i%2):
            print("## ",end="")
    print()

    for k in range (b):
        print("** ",end= "")
        if (1==i%2):
            print("## ",end="")
        elif(0==i%2):
            print("## ",end="")
    print()

    for k in range (b):
        print("## ",end= "")
        if (1==i%2):
            print("** ",end="")
        elif(0==i%2):
            print("** ",end="")
    print()

    for k in range (b):
        print("## ",end= "")
        if (1==i%2):
            print("** ",end="")
        elif(0==i%2):
            print("** ",end="")
    print()