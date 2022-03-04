def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n//10)

def digital_root(n):
    if 0 <= n <= 9:
        return n
    else:
        return digital_root(digit_sum(n))

print(digit_sum(979853562951413))
print(digital_root(979853562951413))

class TreeNode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def get_height(self):
        if self.root is None:
            return -1
        else:
            return 1 + max(self.get_height(self.root.left), self.get_height(self.root.right))

    def sum_leaves_aux(self, curr):
        if curr.left is None and curr.right is None:
            return curr.item
        else:
            return self.sum_leaves(curr.left) + self.sum_leaves(curr.right)

    def sum_leaves(self):
        if self.root is None:
            return 0
        else:
            return self.sum_leaves_aux(self.root)

    def find_min_aux(self, node):
        if node.left is None:
            return node.item
        else:
            return self.find_min_aux(node.left)

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self.find_min_aux(self.root)

    def find_between_aux(self, curr, num1, num2, res):
        if curr is None:
            return
        elif num1 < curr.item < num2:
            res.append(curr.item)
            self.find_between_aux(curr.left, num1, num2, res)
            self.find_between_aux(curr.right, num1, num2, res)
        elif curr.item <= num1:
            self.find_between_aux(curr.right, num1, num2, res)
        elif num2 <= curr.item:
            self.find_between_aux(curr.left, num1, num2, res)

    def find_between(self, a, b):
        res = []
        self.find_between_aux(self.root, min(a,b), max(a,b), res)
        return res

    def inorder_traversal_recursive(self, curr = self.root):
        if curr is None:
            return []
        else:
            return self.inorder_traversal_recursive(curr.left) + [curr.item] + self.inorder_traversal_recursive(curr.right)

    def nth_largest_element_aux(self, n, curr, res = []):
        stack = [curr]
        while stack:
            curr = curr.right
            if curr is not None:
                stack.append(curr)
            else:
                curr = stack.pop()
                res.append(curr.item)
                curr = curr.left
            if len(res) == n:
                return res[-1]

    
    def nth_largest_element(self, n):
        return self.nth_largest_element_aux(n, self.root)

    def preorder_traversal_iterative(self):
        res = []
        curr = self.root
        if curr is None:
            return res
        else:
            stack = [curr.right, curr.left]
            while stack:
                res.append(curr.item)
                curr = stack.pop()
                if curr.right is not None:
                    stack.append(curr.right)
                if curr.left is not None:
                    stack.append(curr.left)
            return res

    def postorder_traversal_iterative(self):
        