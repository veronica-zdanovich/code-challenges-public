from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        index = 1
        merged_intervals_index = 0
        while index < len(intervals):
            if merged_intervals[merged_intervals_index][0] <= intervals[index][0] <= merged_intervals[merged_intervals_index][1] or merged_intervals[merged_intervals_index][0] <= intervals[index][1] <= merged_intervals[merged_intervals_index][1]:
                merged_intervals[merged_intervals_index] = [min(intervals[index][0], merged_intervals[merged_intervals_index][0]), max(intervals[index][1], merged_intervals[merged_intervals_index][1])]
            else:
                merged_intervals.append(intervals[index])
                merged_intervals_index += 1
            index += 1
        return merged_intervals
