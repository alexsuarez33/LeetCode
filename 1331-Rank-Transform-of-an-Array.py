class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        myDict = {}
        rank = 1
        for element in sorted(arr):
            if element not in myDict:
                myDict[element] = rank
                rank += 1

        for i, element in enumerate(arr):
            arr[i] = myDict[element]
        
        return arr
