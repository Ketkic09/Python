a=[[1,4,5],
[2,4,5],
[5,6,7]]
b=[[2,7,8],
[2,5,6],
[3,5,6]]
m=[[0,0,0,],
[0,0,0,],
[0,0,0,]]


for i in range(len(a)):
    print("\n")
    for j in range(len(b[0])):
        m[i][j]=0
        for k in range(len(b)):
            m[i][j]+= a[i][k] * b[k][j] 
            print(m[i][j],'\t')

 

