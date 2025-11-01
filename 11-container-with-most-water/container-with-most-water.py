class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right : #Continue looping until left pointer is not equal to or exceeds the right pointer
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
# Multiple width of the container and minimum of the heights of the two lines.
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return max_area
        