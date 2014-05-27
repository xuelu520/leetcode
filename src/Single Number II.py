__author__ = 'xuelu520'
#coding=utf-8

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0
        two = 0
        three = 0
        for i in range(len(A)):
            two |= A[i] & one
            one = A[i] ^ one
            three = ~(one & two)
            one &= three
            two &= three
        return one
s = Solution()
print s.singleNumber([3,3,3,5])