# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

 skill.sort()
        p1 = 0
        p2 = len(skill) - 1
        tSkill = set()
        res = 0

        while p1 < p2:
            tSkill.add(skill[p1]+skill[p2])
            res += skill[p1]*skill[p2]
            p1 += 1
            p2 -= 1

        return res if len(tSkill) == 1 else -1