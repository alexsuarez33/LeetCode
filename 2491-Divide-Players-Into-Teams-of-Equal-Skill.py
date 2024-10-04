class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill) - 1
        matching = sorted(skill)
        target = matching[left] + matching[right]
        output = matching[left] * matching[right]
        left += 1
        right -= 1
        while left < right:
            if matching[left] + matching[right] != target:
                return -1
            else:
                output += matching[left] * matching[right]
                left += 1
                right -= 1
        return output

        