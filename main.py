#2 class Solution():
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n == 3:
#             return 3
#         if n == 4:
#             return 5
#         if n == 5:
#             return 8
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
#
# n = int(input("enter the number of steps: "))
# print(Solution().climbStairs(n))



#3class Solution():
#     def replaceWords(self, dictionary, sentence):
#         word_list = sentence.split()
#         root_set = set(dictionary)
#         result = []
#         for word in word_list:
#             prefix = ''
#             for letter in word:
#                 prefix += letter
#                 if prefix in root_set:
#                     result.append(prefix)
#                     break
#             else:
#                 result.append(word)
#         return ' '.join(result)
#
# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
# print(Solution().replaceWords(dictionary, sentence))


#5 class Solution(object):
#     def maxSatisfied(self, customers, grumpy, minutes):
#         if not grumpy:
#             return sum(customers)
#         else:
#             total_without_tech = 0
#             for i in range(len(customers) - minutes):
#                 if grumpy[i] == 0:
#                     total_without_tech += customers[i]
#             return total_without_tech + sum(customers[-minutes:])
# customers = [1,0,1,2,1,1,7,5]
# grumpy =    [0,1,0,1,0,1,0,1]
# minutes = 3
# print(Solution().maxSatisfied(customers, grumpy, minutes))


#6 class Solution:
#     def maxSumDivThree(self, nums):
#         sums = [0, -1000, -1000]
#
#         for num in nums:
#             nm = [i for i in sums]
#             for r in range(3):
#                 nm[r] = max(sums[r], sums[(r - num) % 3] + num)
#             sums = nm
#         return sums[0]
#
#
# sol = Solution()
#
# print(sol.maxSumDivThree([3, 6, 5, 1, 8]))


#7 class Solution:
#     def closestCost(self, baseCosts, toppingCosts, target):
#         m = -1000
#         for ice in baseCosts:
#             for top in toppingCosts:
#                 t1 = ice + top
#                 t2 = ice + 2 * top
#                 m = max(m, max(t1 if t1 <= target else 0, t2 if t2 <= target else 0))
#         return m
#
#
# sol = Solution()
#
# print(sol.closestCost([2, 3], [4, 5, 100], 18))



#8 class Solution:
#     def waysToBuyPensPencils(self, total, cost1, cost2):
#         s = 0
#         for i in range(total // cost1 + 1):
#             s += (total - cost1 * i) // cost2 + 1
#         return s
#
#
# sol = Solution()
# print(sol.waysToBuyPensPencils(20, 10, 5))
# print(sol.waysToBuyPensPencils(5, 10, 10))

















