from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=  defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.l[key].append((value,timestamp))
        return "null"

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        m=[]
        for i in self.l.keys():
            if i == key:
                for j in range(len(self.l[i])):
                    if self.l[i][j][1]<=timestamp:
                        m.append(self.l[i][j])
        d = sorted(m, key = lambda x: int(x[1]),reverse=True)
        if len(d)==0:
            return "null"
        else:
            return d[0][0]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
print(obj.set("love","high",10))
print(obj.set("love","low",20))
print(obj.get("love",5))
print(obj.get("love",10))
print(obj.get("love",15))
print(obj.get("love",20))
print(obj.get("love",25))
