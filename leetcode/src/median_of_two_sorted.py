import sys

__author__ = 'zding'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1 = len(nums1)
        l2 = len(nums2)

        while True:
            if l1 == 0:
                return find_mid(nums2)

            nums1_mid = nums1[(l1 - 1) / 2]

            index_of_2 = binary_search_for_index(nums2, nums1_mid)

            if l1 == 1:
                insert_index = binary_search_for_index(nums2, nums1[0])
                if l2 % 2 == 0:
                    return translate(nums1, nums2, insert_index, l2, l2/2)
                else:
                    left = translate(nums1, nums2, insert_index, l2, l2/2)
                    right = translate(nums1, nums2, insert_index, l2, l2/2+1)
                    return 1. * (left + right) / 2

            if l1 == 2:
                i1 = binary_search_for_index(nums2, nums1[0])
                i2 = binary_search_for_index(nums2, nums1[1])

                if l2 % 2 == 0:
                    left = translate(nums1, nums2, i1, i2, (l2+2)/2-1)
                    right = translate(nums1, nums2, i1, i2, (l2+2)/2)
                    return 1. * (left + right) / 2
                else:
                    right = translate(nums1, nums2, i1, i2, (l2+2)/2)
                    return right

            if l1%2 == 0:
                t = l1 / 2 - 1
            else:
                t = l1 / 2

            if index_of_2 <= l2/ 2:
                nums1 = nums1[t:]
                nums2 = nums2[:l2 - t]
            else:
                nums1 = nums1[:l1-t]
                nums2 = nums2[t:]

            l1 -= t
            l2 -= t




def binary_search_for_index(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
    return left


def real_mid(num1, num2):
    return find_mid(sorted(num1 + num2))


def find_mid(array):
    len_a = (len(array) - 1) / 2
    if len(array) % 2 == 0:
        return 1. * (array[len_a] + array[len_a + 1]) / 2
    else:
        return array[len_a]


def translate(num1, num2, a, b, target):
    if target < a :
        return num2[target]
    elif target == a:
        return num1[0]
    else:
        target -= 1

    if target < b:
        return num2[target]
    elif target == b:
        return num1[1]
    else:
        return num2[target-1]





s = Solution()

a = [1, 2, 4, 45, 64, 57, 56, 865, 785]
# a = [1, 2, 4, 45, 64, 57, 56, 865]
# a = [1, 6]
# a=[100001]
# a=[1,2]
# a=[1,3,4]
# a = [1,2,6,7]

a.sort()

b = [11, 24, 1, 3, 64, 7, 457]
b = [11, 24, 1, 3, 64, 7]
# b = [4,5,7,10]
# b=[100000]
# b=[1,2,3]
# b=[2,5,6]
# b=[3,4,5,8]


b.sort()

fa = s.findMedianSortedArrays(a, b)
print 'answer ', fa

print sorted(a)
print binary_search_for_index(a, 63)

c = []
c.extend(a)
c.extend(b)

print c
print sorted(c)
print len(c)
print find_mid(sorted(c))

d = [4, 45, 56]
print d
print binary_search_for_index(d, 11)
print binary_search_for_index(d, 5)