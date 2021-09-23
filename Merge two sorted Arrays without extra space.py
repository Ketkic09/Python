a= list(map(int,input().split(",")))
b=list(map(int,input().split(",")))

for i in range(len(b)):
    for j in range(len(a)):
        if b[i]<a[j]:
            temp=a[j]
            a[j]=b[i]
            b[i] = temp
            
# sorting b
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            temp=b[j]
            b[j]=b[i]
            b[i] = temp
            
print("a {}, b {}".format(a,b)) 

