# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def get_prime_factors(number):
            prime_fact = []
            while number % 2 == 0:
                prime_fact.append(2)
                number //=2

            for i in range(3, int(number ** 0.5)+ 1, 2):
                while number % i == 0:
                    prime_fact.append(i)
                    number //=i
            if number > 2:
                prime_fact.append(number)
            return prime_fact, sum(prime_fact)
        while get_prime_factors(n)[1] !=n:
            n = get_prime_factors(n)[1]
        return n
