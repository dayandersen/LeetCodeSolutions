class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Do we just need to check that there is some combo where values at a,b,c 
        # are equal/less than the target values.
        trip = [0,0,0]
        for triple in triplets:
            all_less_or_equal = True
            for i in range(3):
                if triple[i] > target[i]:
                    all_less_or_equal = False
            if all_less_or_equal:
                for i in range(3):
                    trip[i] = max(trip[i], triple[i])
        
        return trip == target