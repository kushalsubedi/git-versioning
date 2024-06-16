
from typing import List
def twosum(Nums:List,Target:int)->List:
    n1= 0
    n2= len(Nums)-1 
    valid_pairs = []
    Nums.sort()
    for i in range (len(Nums)):
        if Nums[n1] + Nums[n2] == Target:
            valid_pairs.append([Nums[n1],Nums[n2]])
            n1 += 1
            n2 -= 1
        elif Nums[n1] + Nums[n2] < Target:
            n1 += 1
        elif Nums[n1] + Nums[n2] > Target:
            n2 -= 1
        
        else :
            print ("No valid pairs found")
    
    return valid_pairs,Target


print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print (twosum([1,2,3,4,5,6,7,8,9,10],10))

print (ord('A'))
       