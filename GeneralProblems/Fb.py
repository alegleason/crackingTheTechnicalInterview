def CalculateTaxes(income, tax_brackets_table):  # 8,000
    if len(tax_brackets_table) == 0:
        raise Exception('Please check table')
    if income <= 0:
        return 0
    total_tax = 0
    # O(b) time complexity where b is the number of elements we have on the bracket table
    for tax_entree in tax_brackets_table:
        # We are on the last line
        if not tax_entree[0]:
            total_tax += income * tax_entree[1]
            return total_tax

        # Check if we can subtract
        new_income = income - tax_entree[0]  # -7,000
        if new_income >= 0:
            # Perform the tax calculation
            income = new_income  # 3,000
            total_tax += tax_entree[1] * tax_entree[0]
            # total_tax += tax_entree[1] * min(tax_entree[0], income)
        else:
            total_tax += tax_entree[1] * income  # 3,000 * .1
            break
    return total_tax


# CalculateTaxes(8000, [[5000, 0], [10000, .1], [20000, .2], [10000, .3], [None, .4]])

class Solution:
    # 39. Combination Sum LeetCode
    def combinationSum(self, candidates, target):
        # O(n^n) time and O(n*n) space complexity
        res = []
        self.combinationHelper(candidates, target, 0, [], res)
        return res

    def combinationHelper(self, candidates, target, idx, curr_candidates, res):
        # Base cases
        if target == 0:
            # Valid combination
            res.append(curr_candidates)
            return
        elif target < 0:
            # Invalid number
            return
        # Perform DFS
        for i in range(idx, len(candidates)):
            self.combinationHelper(candidates, target - candidates[i], i, curr_candidates + [candidates[i]],
                                   res)  # Same position

    # 22. Generate Parentheses LeetCode
    def generateParenthesis(self, n):
        # O(2^n) time and O(n*2) space complexity
        res = []
        self.generateParenthesisHelper(n, n, "", res)
        return res

    # Inside fx so res has same scope
    def generateParenthesisHelper(self, left, right, curr, res):
        # Base case
        if not left and not right:
            res.append(curr)
            return
        # Recursion - Depth First
        temp = curr + "("
        if left > 0:
            self.generateParenthesisHelper(left - 1, right, temp, res)
        if right > left:
            curr += ")"
            self.generateParenthesisHelper(left, right - 1, curr, res)

    # 50. Pow(x, n) LeetCode
    def myPow(self, x, n):
        # Lets use the idea that x^5 is the same as x^2 * x^2 * x^1 and save 50% of the time
        # O(logn) time and O(n) space complexity (call stack)
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            # Convert to fraction and positive, which is equivalent
            x = 1 / x
            n *= -1
        result = self.myPow(x, n // 2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result

    # 93. Restore IP Addresses LeetCode
    def restoreIpAddresses(self, s):
        # O(2^n) time and O(n^2) space complexity
        res = []
        # Actual DFS call
        self.restoreIPAddressesHelper(s, 0, "", res)
        return res

    def restoreIPAddressesHelper(self, s, idx, path, res):
        # We do not want to have combinations greater than 3 chars
        if idx > 4:
            return
        # Just add if there are no more numbers to look at
        if idx == 4 and not s:
            res.append(path[:-1])  # Remove the last '.'
            return
        # Advance at most 4 positions, or at the end of the total numbers
        for i in range(1, min(len(s) + 1, 4)):
            # Allowing alone, intermediate or final 0s, but blocking format '.0xx.' or IPs greater than 256
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                self.restoreIPAddressesHelper(s[i:], idx + 1, path + s[:i] + ".", res)

    # 121. Best Time to Buy and Sell Stock LeetCode
    def maxProfit(self, prices):
        # Using Kadane's algorithm so we can handle negative inputs
        max_cur, max_so_far = 0, 0
        for i in range(1, len(prices)):
            temp = max_cur + prices[i] - prices[i-1]
            max_cur = max(0, temp)
            max_so_far = max(max_cur, max_so_far)
        return max_so_far

    # 53. Maximum Subarray LeetCode
    def maxSubArray(self, nums):
        # Using DP
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i-1] > nums[i]:
                nums[i] += nums[i-1]
            if nums[i] > max_so_far: max_so_far = nums[i]
        return max_so_far




sol = Solution()
print(sol.generateParenthesis(3))
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.myPow(2.0, 10))
print(sol.restoreIpAddresses("101023"))
print(sol.maxProfit([7, 1, 5, 6]))
print(sol.maxSubArray([7, 1, 5, 6]))
print(sol.maxSubArray([-2, 1]))