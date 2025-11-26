# Problem Link: https://leetcode.com/problems/group-anagrams/
# Submission Link: https://leetcode.com/problems/group-anagrams/submissions/1839839972/
# Solution beats over 80% on runtime and 95% on memory
# Sorting has a complexity of O(m log m) making my solution O(n * m log m) or O(n * k log k)
# Uses the sorted string as the key with any anagrams being the values
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            # If it's already there add this string to the list
            if sorted_string in result:
                result[sorted_string].append(string)
            # If not, add a list with the item for the value
            else:
                result[sorted_string] = [string]
            
        result_list = []
        for key in result:
            result_list.append(result[key])
        
        return result_list
