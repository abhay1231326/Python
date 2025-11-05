from array import array
arr=array('i',[1,2,3,4])
print(arr)

print(arr[0])  
print(arr[3])

arr.append(5)
print(arr)

arr.insert(5,34)
print(arr)

arr.remove(34)
print(arr)

for i in arr :
    print(i)
    
print(arr.index(1))

arr.reverse()
print(arr)   
        
    
    
    
    