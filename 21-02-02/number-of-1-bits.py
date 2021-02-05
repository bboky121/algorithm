# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
        return count


if __name__ == '__main__':
    print(Solution().hammingWeight(0b0000000000000000000000000001011))
