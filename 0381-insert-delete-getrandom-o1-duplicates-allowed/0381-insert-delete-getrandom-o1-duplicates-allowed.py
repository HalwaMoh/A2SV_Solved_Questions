import random
from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val):
        self.nums.append(val)
        self.idx[val].add(len(self.nums) - 1)
        return len(self.idx[val]) == 1

    def remove(self, val):
        if not self.idx[val]:
            return False
        
        remove_idx = self.idx[val].pop()
        last = self.nums[-1]

        self.nums[remove_idx] = last
        self.idx[last].add(remove_idx)
        self.idx[last].discard(len(self.nums) - 1)

        self.nums.pop()
        return True

    def getRandom(self):
        return random.choice(self.nums)
