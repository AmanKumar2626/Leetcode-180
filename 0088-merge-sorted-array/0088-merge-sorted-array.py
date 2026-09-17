class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j = m - 1
        k = n - 1
 
        if n == 0:
            return
        if m == 0:
            nums1[0:] = nums2[0:]
            return 
             
        for i in range(m + n -1, -1, -1):
            if j >= 0 and nums1[j] >= nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                 nums1[i] = nums2[k]
                 k -= 1
            if k == -1:
                break

