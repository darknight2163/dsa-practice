# Problem: Find the median of two sorted arrays.
# Approach: Binary search on the smaller array to find a partition
#           where every element on the left side is <= every element
#           on the right side. This allows us to determine the median
#           without actually merging the arrays.
# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2  # size of left half (handles odd/even)

    lo, hi = 0, m

    while lo <= hi:
        i = (lo + hi) // 2       # partition index in nums1
        j = total_left - i       # partition index in nums2

        # Boundary values around the partition
        left1  = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2  = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')

        if left1 <= right2 and left2 <= right1:
            # Correct partition found
            if (m + n) % 2 == 1:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0

        elif left1 > right2:
            hi = i - 1   # too far right in nums1, move left

        else:
            lo = i + 1   # too far left in nums1, move right

    raise ValueError("Input arrays are not sorted / invalid input")