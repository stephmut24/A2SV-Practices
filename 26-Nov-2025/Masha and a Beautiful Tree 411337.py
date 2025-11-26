# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

# Problem D: Masha and a Beautiful Tree
# https://codeforces.com/problemset/problem/1741/D

def solve(nums, left, right):
    if right - left == 1:
        return 0

    swap = 0
    mid = (left + right) // 2

    left_max = max(nums[left:mid])
    right_max = max(nums[mid:right])

    if left_max > right_max:
        swap += 1

        for i in range(mid - left):
            nums[left + i], nums[mid + i] = nums[mid + i], nums[left + i]

    return solve(nums, left, mid) + solve(nums, mid, right) + swap


def min_swaps(nums):
    n = len(nums)
    ans = solve(nums, 0, n)

    if sorted(nums) == nums:
        return ans
    else:
        return -1


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        print(min_swaps(nums))