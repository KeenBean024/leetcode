class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(' ')
        for i in range(len(a)):
            a[i] = a[i][::-1]
            i+=1
        return ' '.join(a)