#Two Sum

class Solution:
    def twoSum(self, nums, target):
        seen = {}  # এখানে আমরা সংখ্যা আর তার index রাখব
        for i, num in enumerate(nums):
            complement = target - num  # target এ পৌছাতে আর কত দরকার
            
            if complement in seen:
                # যদি complement আগে দেখা থাকে, তাহলে উত্তর পাওয়া গেছে
                return [seen[complement], i]
            
            # না থাকলে, এই সংখ্যাটা map এ রাখি
            seen[num] = i
