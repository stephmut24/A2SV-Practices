# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.list =[]
        

    def insert(self, val: int) -> bool:
        if val in self.list:
            return False
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.list:
            self.list.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.list)-1)
        return self.list[randomIndex]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()