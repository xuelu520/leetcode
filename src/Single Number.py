__author__ = 'xuelu520'
#coding=utf-8

#Given an array of integers, every element appears twice except for one. Find that single one.

#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#解法就是用 异或。 2个相同数字异或就为0 这样最终的结果就是出现一次的数字
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        B = 0
        for  i in A:
            B = B^i
        return B
