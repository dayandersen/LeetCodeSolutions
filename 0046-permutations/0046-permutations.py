class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        def permute(arr, path):
            if arr:
                for i in range(len(arr)):
                    permute(arr[:i] + arr[i+1:], path + [arr[i]])
            else:
                ret.append(path)

        permute(nums, [])
        return ret