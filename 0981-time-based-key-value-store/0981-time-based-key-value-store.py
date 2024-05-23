class TimeMap(object):

    def __init__(self):
        self.store = {} # Contains {key: [[value, timestamp],....]}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ''
        data = self.store.get(key, [])

        l, r = 0, len(data)-1
        while l<=r:
            mid = (l+r)//2
            # if data[mid][1] == timestamp:
            #     res = data[mid][0]
            if data[mid][1] <= timestamp:
                res = data[mid][0]
                l = mid + 1
            else:
                r = mid -1
            
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)