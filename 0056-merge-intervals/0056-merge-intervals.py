class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = []
        lst = intervals[0]
        for i in range(1, len(intervals)):
            if lst[1] >= intervals[i][0]:
                if lst[1] < intervals[i][1]:
                    lst[1] = intervals[i][1]

            else:
                result.append(lst)
                lst = intervals[i] 
        result.append(lst)
        return result