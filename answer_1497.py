class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        # Step 1: Create an array to count remainders
        remainder_count = [0] * k
        
        # Step 2: Calculate remainders and update counts
        for num in arr:
            remainder = num % k
            if remainder < 0:  # Handling negative remainders
                remainder += k
            remainder_count[remainder] += 1
        
        # Step 3: Handle the special case for remainder 0
        if remainder_count[0] % 2 != 0:
            return False
        
        # Step 4: Check remainder pairing
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True
