class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def insertLevelOrder(arr, root, i, n):

    if i < n:
        tmp = TreeNode(arr[i])
        root = tmp

        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2*i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2*i + 2, n)

    return root


if __name__ == '__main__':
    arr = [1, 0, 2]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    print(root)
