# class Solution():
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



# class Solution():
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



