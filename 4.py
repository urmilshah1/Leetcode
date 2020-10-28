    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        for i in range(len(nums1)):
            a.append(nums1[i])
        for j in range(len(nums2)):
            a.append(nums2[j])
        a.sort()
        mid = len(a) // 2
        res = (a[mid]+ a[~mid])/ 2
        return res