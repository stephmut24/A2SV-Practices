# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin= celsius + 273.15
        fahrenheit= celsius * 1.80 + 32.00
        return [Kelvin, fahrenheit]
