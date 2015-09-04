import sys

__author__ = 'zding'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        while True:

            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1

            l1 = len(nums1)
            l2 = len(nums2)

            if l1 == 0:
                return find_mid(nums2)

            nums1_mid = nums1[(l1 - 1) / 2]
            # print l1, 'l1 mid', nums1_mid

            index_of_2 = find_in_array(nums2, nums1_mid)

            if l1 == 1:
                print l1, l2
                print nums1,
                print nums2
                # temp = (l2 - 1) / 2
                # if l2 % 2 == 0:
                #     if nums1[0] <= nums2[temp]:
                #         return nums2[temp]
                #     elif nums1[0] <= nums2[temp + 1]:
                #         return nums1[0]
                #     else:
                #         return nums2[temp + 1]
                # else:
                #     print 'final 1', nums1, nums2
                #     if l2 == 1:
                #         return 1.*(nums1[0] + nums2[0]) / 2
                #     else:
                #         num2_mid = nums2[l2/2]
                #         if nums1[0] < num2_mid:
                #             return 1.*(max([num2_mid-1, nums1[0]]) + num2_mid) / 2
                #         else:
                #             return 1.*(min([num2_mid+1, nums1[0]]) + num2_mid) / 2

                insert_index = find_in_array(nums2, nums1[0])
                if l2 % 2 == 0:
                    return translate(nums1, nums2, insert_index, l2, l2/2)
                else:
                    left_index = l2/2
                    right_index = l2/2+1
                    left = translate(nums1, nums2, insert_index, l2, left_index)
                    right = translate(nums1, nums2, insert_index, l2, right_index)
                    return (left + right) * 1.0 / 2

            if l1 == 2:
                print nums1, nums2
                if l2 == 2:
                    a = max([nums1[0], nums2[0]])
                    b = min([nums1[1], nums2[1]])
                    return 1. * (a + b) / 2
                elif l2 % 2 == 0:
                    i1 = find_in_array(nums2, nums1[0])
                    i2 = find_in_array(nums2, nums1[1])

                    print 'i1', i1, 'i2', i2

                    left_mid = translate(nums1, nums2, i1, i2, (l2+2)/2-1)
                    right_mid = translate(nums1, nums2, i1, i2, (l2+2)/2)

                    print 'left_mid', left_mid, 'right_mid', right_mid

                    return 1.0 * (left_mid + right_mid) / 2

                else:
                    i1 = find_in_array(nums2, nums1[0])
                    i2 = find_in_array(nums2, nums1[1])

                    print 'i1', i1, 'i2', i2

                    right_mid = translate(nums1, nums2, i1, i2, (l2+2)/2)

                    print 'right_mid', right_mid

                    return right_mid

            print nums1,
            print nums2,
            print index_of_2,
            print real_mid(nums1, nums2)

            if index_of_2 < l2/ 2:
                t = l1 / 2
                print t
                nums1 = nums1[t:]
                nums2 = nums2[:l2 - t]

            elif index_of_2 == l2 / 2:
                if l1 % 2 == 0:
                    t = l1 / 2 - 1
                    print 't ', t
                    nums1 = nums1[t:]
                    nums2 = nums2[:l2 - t]
                else:
                    t = l1 / 2
                    print t
                    nums1 = nums1[: l1 - t]
                    nums2 = nums2[t : ]

            else:
                t = l1 / 2
                print 't ', t
                nums1 = nums1[:l1-t]
                nums2 = nums2[t:]


def find_in_array(array, target):
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

    print target, left
    return left

def real_mid(num1, num2):
    c = []
    c.extend(num1)
    c.extend(num2)
    return find_mid(sorted(c))


def find_mid(a):
    len_a = (len(a) - 1) / 2
    if len(a) % 2 == 0:
        return 1. * (a[len_a] + a[len_a + 1]) / 2
    else:
        return a[len_a]

def translate(num1, num2, a, b, target):
    if target < a :
        return num2[a]
    elif target == a:
        return num1[0]
    else:
        target -= 1
        if a != b:
            b = b-1

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
a.sort()

b = [11, 24, 1, 3, 64, 7, 457]
# b = [11, 24, 1, 3, 64, 7]
# b = [4,5,7,10]
b.sort()

fa = s.findMedianSortedArrays(a, b)
print 'answer ', fa

print sorted(a)
print find_in_array(a, 63)

c = []
c.extend(a)
c.extend(b)

print c
print sorted(c)
print len(c)
print find_mid(sorted(c))

d = [4, 45, 56]
print d
print find_in_array(d, 11)
print find_in_array(d, 5)