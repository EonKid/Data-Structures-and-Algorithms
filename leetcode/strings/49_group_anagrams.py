# python3
# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        H = {}
        L = []
        for string in strs:
            str_key = "".join(sorted(string))
            if str_key not in H:
                H[str_key] = [string]
            else:
                data = H[str_key]
                data.append(string)
                H[str_key] = data
        for key in H:
            data = H[key]
            L.append(data)
        return L

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))