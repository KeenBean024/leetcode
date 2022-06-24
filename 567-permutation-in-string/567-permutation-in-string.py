class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)> len(s2): return False
        
        #Initialize empty count arrays
        s1Count = [0]*26
        s2Count = [0]*26
        
        #Create base count value
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')]+=1
            s2Count[ord(s2[i]) - ord('a')]+=1
        
        #Create match count:
        matches=0
        for i in range(26):
            if s1Count[i]==s2Count[i]:
                matches+=1
        
        l=0 #left pointer
        
        for r in range(len(s1), len(s2)):
            if matches==26: return True # Found match
            
            index = ord(s2[r]) - ord('a')
            s2Count[index]+=1
            #Update matches for right pointer
            if s1Count[index]==s2Count[index]:
                matches +=1
            
            elif s1Count[index]+1 == s2Count[index]:
                matches -=1
                
            #Update matches for left pointer
            index = ord(s2[l]) - ord('a')
            s2Count[index]-=1
            if s1Count[index]==s2Count[index]:
                matches +=1
            
            elif s1Count[index]-1 == s2Count[index]:
                matches -=1
            l+=1
        return matches==26