 # Tupple = Array yang tidak bisa di rubah
 # list = array yang bisa di ubah


 #  Tupple menggunakan kurung
 #  Contoh

#            0       1     2
# Minuman = ("Teh", "Kopi","Soda")
#
# Minuman = ('Teh', 'Kopi','Soda')
# print(Minuman )
# print(Minuman [0])
#
# Makanan= ('Bubur',) # jika ingin menampilkan makanan 1 aja
# print(Makanan)
#
# Menu=(Minuman,1000) # Menampilkan Minuman dan 1000
# print (Menu)

#Pada Phyton Tupple tidak bisa Menambahkan dan mengganti data

# Contoh Penggunaan List

# minuman= ["Teh","Kopi","Soda"]
# print(minuman[0])
#
# minuman[1]="susu"
# print(minuman[1])
#
# minuman.append("Jeruk")# Menambah Satu
# minuman.extend(['Fanta','Pepsi','Cola'])#Menambah banyak data
#
# print(minuman)
# print(len(minuman))# Menghitung Panjang Data

## Looping Dalam Array Ada 2 Cara

# nilai=[10,8,4,9,5]
# # Cara 1
# for i in (nilai):
#     print(i)
# print()
#
# #Cara 2
# for i in range(len(nilai)):
#     print(nilai[i])
# print()
#
# #Buat Buble Short
#
# for i in (sorted(nilai)): # Cara Phyton
#     print(i)

# for i in  range(len(nilai)-1,0,-1):
#     for k in range (i):
#      if nilai[k] < nilai[k+1]:
#         temp = nilai[k]
#         nilai[k] = nilai[k+1]
#         nilai[k+1] = temp
#
#         print(nilai)
# print(nilai)

# Poker Playing Thrice

import random

kartu = ["2H","2S","2W","2K","3H","3S","3W","3K","4H","4S","4W","4K","5H","5S","5W","5K","6H","6S","6W","6K"
        , "7H", "7S", "7W", "7K","8H","8S","8W","8K","9H","9S","9W","9K","10H","10S","10W","10K","JH","JS","JW","JK"
        , "QH", "QS", "QW", "QK","KH","KS","KW","KK","AH","AS","AW","AK"]
# # Triace
# increment =0
# arr=[]
#
# for i in range (0,52,4):
#     for j in range(i,i+4):
#         arr.append(kartu[j])
#     for m in reversed(range(i,i+4)):
#         arr.remove(kartu[m])
#         for k in range(52):
#             if (arr[0][0] != kartu[k][0]):
#                 arr.append(kartu[k])
#                 for l in range((k*1),52):
#                     if ((arr[0][0] != kartu[l][0]) and (arr[3][0]!=kartu[l][0])):
#                         arr.append(kartu[l])
#                         print(arr)
#                         increment +=1
#                         arr.remove(kartu[l])
#                 arr.remove(kartu[k])
#         arr.append(kartu[m])
#     arr.clear()
# #
# print("Kombinasi :", increment)

# Array 2 Dimensi

# Minuman= ["kopi","capucino","flapucino"],\
#          ["jus apel","jus jeruk","jus alpukat"]
#
# print (Minuman [1][1])
#
# for i in Minuman :
#     for j in i :
#         print(j)

# Cara Membuat Function pada phyton

# Dengan cara menambahkan def
#
# def halo():
#  print("Selamat Pagi")
#
# halo()
#
# # Menggabungkan 2 variable
# def halo(variable):
#     print ("Selamat Pagi %s teman "%variable)
#
# halo("Teman")
#
#
# # Mencari Luas
#
# def luas (panjang,lebar):
#     l=panjang*lebar
#     return l
#
# l=luas(28,23)
# print(l)

# Tambah Komentar

# alur = [1,1,1,0,1,1,1,1],\
#        [1,1,0,0,0,1,1,0],\
#        [1,1,1,1,1,1,1,0],\
#        [1,1,1,1,1,1,1,0],\
#        [0,0,0,1,1,1,1,0],\
#        [1,1,1,0,0,1,1,0],\
#        [1,1,1,1,1,1,0,1],\
#        [1,1,1,1,0,0,1,1]
#

N=8
def printSolution(sol):
         for i in sol:
                 for j in i:
                         print(str(j) + " ", end="")
                 print("")


 # A utility function to check if x,y is valid
 # index for N*N Maze
def isSafe(maze, x, y):
         if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
                 return True

         return False


def solveMaze(maze):
         # Creating a 4 * 4 2-D list
         sol = [[0 for j in range(8)] for i in range(8)]

         if solveMazeUtil(maze, 0, 0, sol) == False:
                 print("Solution doesn't exist");
                 return False

         printSolution(sol)
         return True


 # A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
         # if (x,y is goal) return True
         if x == N - 2 and y == N - 4:
                 sol[x][y] = 1
                 return True

         # Check if maze[x][y] is valid
         if isSafe(maze, x, y) == True:
                 # mark x, y as part of solution path
                 sol[x][y] = 1

                 # Move forward in x direction
                 if solveMazeUtil(maze, x + 1, y, sol) == True:
                         return True

                 # If moving in x direction doesn't give solution
                 # then Move down in y direction
                 if solveMazeUtil(maze, x, y + 1, sol) == True:
                         return True

                 if solveMazeUtil(maze, x, y - 1, sol) == True:
                         return True
                 # If none of the above movements work then
                 # BACKTRACK: unmark x,y as part of solution path
                 sol[x][y] = 0
                 return False


if __name__ == "__main__":
         # Initialising the maze
         maze = [[1,1,1,0,1,1,1,1],\
       [1,1,0,0,0,1,1,0],\
       [1,1,1,1,1,1,1,0],\
       [1,1,1,1,1,1,1,0],\
       [0,0,0,1,1,1,1,0],\
       [1,1,1,0,0,1,1,0],\
       [1,1,1,1,1,1,0,1],\
       [1,1,1,1,0,0,1,1]]

         solveMaze(maze)