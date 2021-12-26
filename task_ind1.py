n = 9
array = t = [ [0]*n for i in range(n)]
k=0
for i in range (n+1):
	for j in range (i):
		k+=1
		array[i-j-1][j] = k
for i in range (n+1,2*n):
	for j in range(i-n,n):
		k+=1
		array[i-j-1][j]=k
for i in range(n):
	for  j in range(n):
		print(str(array[i][j])+"\t", end="")
	print()