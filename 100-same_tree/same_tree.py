class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):

    if not p or not q:
        return p == q

    right = True
    left = True


    if q.val != p.val:
        return False
    else:
        right = isSameTree(p.right, q.right)
        left = isSameTree(p.left, q.left)

    if right != True or left != True:
        return False
    else:
        return True


p = TreeNode(1, TreeNode(2), TreeNode(3))

q = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTree(p, q))