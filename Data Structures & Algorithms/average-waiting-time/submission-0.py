class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        wait_times = []
        for arr, prep in customers:
            curr_time = max(curr_time, arr)
            curr_time += prep

            wait = curr_time - arr
            wait_times.append(wait)
        
        return sum(wait_times)/len(wait_times)            
