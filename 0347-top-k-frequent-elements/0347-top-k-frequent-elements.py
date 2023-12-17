class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(lambda :0)
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n] += 1
            
        for key, value in count.items():
            freq[value].append(key)
       
        result = []
        index = len(freq)-1
        while k>0:
            if freq[index]:
                result.extend(freq[index])
                k-=len(freq[index])
            index -= 1
        return result
            
        
        # Time Complexit O(n)