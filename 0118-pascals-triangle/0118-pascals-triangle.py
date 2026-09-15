class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            list = []
            list.append(1)
            last = result[-1]
            prev = last[0]
            for j in range(1, len(last)):
                sum = prev + last[j]
                list.append(sum)
                prev = last[j]
            list.append(1)
            result.append(list) 
        return result
