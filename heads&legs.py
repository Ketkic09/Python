''' 
input list will contain no. of total heads (dogs+chickens) and at the next postion contains sum of legs 
output should contain [no. of chickens, no. of dogs]
Example: 
input -> [5(heads),12(legs)] 
    output -> [4(chickens),1(dogs)]'''


h,l=map(int,input("Enter no. of heads & legs: ").split())
result=[]

for i in range(int(l/4)):
    if i*4+(h-i)*2 == l:
        result=[i,h-i]
print(result)


