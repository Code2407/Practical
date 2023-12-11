'''
This program is created by ATHARVA PAWAR

Experiment No. 9 : Write a Python Program to compute following computation on matrices :
                   a)Addition of two matrices
                   b)Subtraction of two matrices
                   c)Multiplication of two matrices
                   d)Transpose of a matix
'''

X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

Y = [[5,8,1],
[6,7,3],
[4,5,9]]

result = [[0,0,0],
[0,0,0],
[0,0,0]]

#addition of two matirx
for i in range(len(X)):
  for j in range(len(X[0])):
    result[i][j] = X[i][j] + Y[i][j]
print("Addition of two matrices is :")
for r in result:
   print(r)

#subtraction of matrix
for i in range(len(X)):
  for j in range(len(X[0])):
    result[i][j] = X[i][j] -  Y[i][j]
print("Subtraction of two matrices is :")
for r in result:
   print(r)
    
#multipication of matrix
for i in range(len(X)):
  for j in range(len(Y[0])):
      for k in range(len(Y)):
         result[i][j] = X[i][k] * Y[k][j]
print("Multipication of two matrices is :")
for r in result:
   print(r)
    
#transpose of matirix
for i in range(len(X)):
  for j in range(len(X[0])):
    result[i][j] = X[i][j] 
print("Transpose of a matrix is :")
for r in result:
   print(r)
