def py_triplets(arr):
    lst=[]
    arr.sort()
    
    for i in range(len(arr)):
       for j in range(i+2,len(arr)):
           if arr[i]**2 + arr[i+1]**2 == arr[j]**2 :
               lst.append([arr[i],arr[i+1],arr[j]])
           else :
               break
    

    return lst

lst=[]
arr=[1,3,6,4,2,5,8,10]
lst=py_triplets(arr)
print('Pythagorean Triplets: ',lst)