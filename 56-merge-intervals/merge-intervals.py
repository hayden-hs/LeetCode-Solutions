class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

# Sort the intervals based on their start times. The lambda x: x[0] is used to extract the start time of each interval for comparison during sorting.

        intervals.sort(key=lambda x: x[0])

# Initialize prev with the first interval from the sorted list.

        prev = intervals[0]

# Iterate through the sorted intervals starting from the second intervl (index 1) to the last interval.

        for interval in intervals[1:]:

#If the start time of the current interval is less than or equal to the end time of the prev interval

            if interval[0] <= prev[1]:

#Update the end time of the prev interval to maximum end time between prev and the current interval.

                prev[1] = max(prev[1], interval[1])

            else:

#Intervals don't overlap, add the prev interval to the merged list

                merged.append(prev)

#Update prev to be the current interval, this interval will be used for further comparisons.

                prev = interval

#Adding the Last Interval

        merged.append(prev)

        return merged

