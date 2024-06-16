

from typing import List

def thsum(Arr:List,Target):
    n1=0
    n2 = len(Arr)-1
    n3 = len(Arr)-2
    valid_pairs = []
    Arr.sort()
    for i in range(len(Arr)):
        if Arr[n1] + Arr[n2] + Arr[n3] == Target:
            valid_pairs.append([Arr[n1],Arr[n2],Arr[n3]])
            n1 += 1
            n2 -= 1
            n3 -= 1
        elif Arr[n1] + Arr[n2] + Arr[n3] < Target:
            n1 += 1
        elif Arr[n1] + Arr[n2] + Arr[n3] > Target:
            n3 -= 1
        else:
            print("No valid pairs found")

    return valid_pairs,Target

print(thsum([2,7,11,15],18))
print(thsum([3,2,4],9))
print(thsum([1,2,3,4,5,6,7,8,9,10],10))
