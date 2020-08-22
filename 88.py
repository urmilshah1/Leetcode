class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            nums1.append(i)
            nums1.remove(0)
        nums1.sort()
        
        
        #merge two sorted lists, append list nums1 by nums2 one element at a time. Then remove the zeros that are encountered. 