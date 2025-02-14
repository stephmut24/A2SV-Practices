# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.occ = collections.defaultdict(int)
        self.freq = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.occ[number] +=1
        f = self.occ[number]
        self.freq[f] +=1
        self.freq[f-1] -=1

    def deleteOne(self, number: int) -> None:
         if self.occ[number] > 0:
            old_freq = self.occ[number]
            self.occ[number] -= 1
            new_freq = self.occ[number]

            self.freq[old_freq] -= 1
            if new_freq > 0:
                self.freq[new_freq] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)