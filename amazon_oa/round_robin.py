# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 1. not changing the structure
        nodes = []
        stack = []
        node = root
        while node:
            stack += node,
            node = node.left
            
        while len(nodes) < k:
            n = stack.pop()
            nodes += node,
            if n.right:
                t = n.right
                while t.left:
                    stack += t.left,
                    t = t.left
        return nodes[-1].val

s = Solution()

                
            


def cpu(arr, ela, q):

    queue = []
    cur = 0

    queue += (0, 0),
    total = 0
    added = 1

    while queue:

        i, run = queue.pop()

        nextcpu = run + q
        if nextcpu >= ela[i]:
            cur += ela[i] - run
            total += cur - arr[i] - ela[i]
        else:
            cur += q

        while added < len(arr):
            if arr[added] <= cur:
                queue.insert(0, (added, 0))
                added += 1
            else:
                break

        if nextcpu < ela[i]:
            queue.insert(0, (i, run+q))
            
    return total * 1.0 / len(arr)



print cpu([0, 1, 4], [5, 2, 3], 3)

# print cpu([])

print cpu([0,1,3,9], [2,1,7,5], 2)

print cpu([0,2,4,5], [7,4,1,4], 3)









        


