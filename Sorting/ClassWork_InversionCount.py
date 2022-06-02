#
# Created on Tue May 31 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array of N elements, count the no.of pairs (i,j) such that i < j and A[i] > A[j]

Approach:
[10, 3, 8, 15, 6, 12, 2, 18, 7, 1]
Total inversion pairs = inversion pairs of A [10, 3, 8, 15, 6] + inversion pairs of B [12, 2, 18, 7, 1] + inversion pairs between A & B

we will use divide and conquer approach
'''
class Solution:
    def countPairsAiGreaterThanBj(self, arrayA, arrayB):
        arrayA = sorted(arrayA)
        arrayB = sorted(arrayB)
        sizeOfarrayA = len(arrayA)
        count = 0
        ptrA = ptrB = 0 
        while(ptrA < len(arrayA) and ptrB < len(arrayB)):
            if arrayA[ptrA] > arrayB[ptrB]:
                count += (sizeOfarrayA-1 - ptrA + 1)
                ptrB += 1
            else:
                ptrA += 1
        
        return count

    def inversionCount(self, input_array, startPtr, endPtr):
        if abs(endPtr - startPtr) + 1 == 1:
            #if size of the sub-array is 1, then we cannot form a pair, so return 0
            return 0
        else:
            mid = (startPtr + endPtr)//2
            x = self.inversionCount(input_array, startPtr, mid)
            y = self.inversionCount(input_array, mid+1, endPtr)
            z = self.countPairsAiGreaterThanBj(input_array[startPtr:mid+1], input_array[mid+1:endPtr+1])
            return x + y + z
    
s = Solution()
#test cases:
#1
input_array = [10, 3, 8, 15, 6, 12, 2, 18, 7, 1]
ans = s.inversionCount(input_array, 0, 9)
print(ans)
assert ans == 26

#2
input_array = [3, 2, 1]
ans = s.inversionCount(input_array, 0, 2)
print(ans)
assert ans == 3

#3
input_array = [1, 2, 3]
ans = s.inversionCount(input_array, 0, 2)
print(ans)
assert ans == 0










