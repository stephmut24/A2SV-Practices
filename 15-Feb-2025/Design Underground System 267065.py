# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkInStore ={}
        self.records ={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkInStore:
            self.checkInStore[id] = [stationName, t]

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
          if id in self.checkInStore:
            startStation, startTime = self.checkInStore.pop(id)  
            travelTime = t - startTime  
            
           
            if (startStation, stationName) in self.records:
                total_time, count = self.records[(startStation, stationName)]
                self.records[(startStation, stationName)] = (total_time + travelTime, count + 1)
            else:
                self.records[(startStation, stationName)] = (travelTime, 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        total_time, count = self.records.get((startStation, endStation), (0, 1)) 
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)