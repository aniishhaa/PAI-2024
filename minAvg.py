class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
    
        while nums:
            min_element = min(nums)
            max_element = max(nums)
            nums.remove(min_element)
            nums.remove(max_element)
            average = (min_element + max_element) / 2.0
            averages.append(average)
        return min(averages)
