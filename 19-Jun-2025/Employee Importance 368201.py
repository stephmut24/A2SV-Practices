# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['employee'], id: int) -> int:

        def dfs(id):
            result = emImportance[id]
            for sub in subImportance[id]:
                result += dfs(sub)
            return result

        emImportance = {}
        subImportance = {}

        for employee in employees:
            emImportance[employee.id] = employee.importance
            subImportance[employee.id] = employee.subordinates
        return dfs(id)

        