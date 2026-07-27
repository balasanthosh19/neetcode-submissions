class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        maxi=0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        for i,j in dic.items():
            if j>len(nums)/2:
                maxi=i
        return maxi    

        