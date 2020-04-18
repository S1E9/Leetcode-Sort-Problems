class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_nums1 = []
        for k in nums1:
            if k not in new_nums1:
                new_nums1.append(k)

        cross = []
        for i in new_nums1:
            if i in nums2:
                cross.append(i)
        
        return cross
