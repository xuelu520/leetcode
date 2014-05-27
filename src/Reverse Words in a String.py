__author__ = 'xuelu520'
#coding=utf-8
#题目
#Given an input string, reverse the string word by word.
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".
# 给定一段字符串，按照每个单词来倒转

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        #字符串按照空格来切割 split 成列表,然后切片倒转列表，最后用空格组合
        return ' '.join(s.split()[::-1])

