class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        All = []
        All=nums1+nums2
        All.sort()
        index = len(All)//2
        if len(All)%2 == 1:
            return All[index]
        else:
            index2 = index +1
            answer = (All[index-1]+All[index2-1])/2
            return answer
a = Solution()
print(a.findMedianSortedArrays([1,2],[3,4]))