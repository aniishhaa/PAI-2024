class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        n = len(hours)
        for i in range(n):
            for j in range(i + 1, n):
                m = hours[i] + hours[j]
                if m % 24 == 0:
                    count += 1
        
        return count


        
