class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort() #[1,1,2,2]
        nums2.sort() #[2,2]

        i = j = 0
        new = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                new.append(nums1[i])
                i += 1
                j += 1
                
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return new

        