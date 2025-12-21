"""
Binary Tree Basics - CRUD Operations

1. create - Node class, build tree, from list/array
2. read - traversals (inorder, preorder, postorder, level-order), search, find
3. update - modify node values
4. delete - delete nodes (leaf, one child, two children)
"""

# ============================================================================
# 1. CREATE
# ============================================================================


# Node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


# Create nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Build tree from list (level-order, None for missing nodes)
def build_tree_from_list(vals):
    """Build binary tree from level-order list [1, 2, 3, 4, None, 5]"""
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = [root]
    i = 1

    while queue and i < len(vals):
        node = queue.pop(0)

        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1

        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1

    return root


# Example: [1, 2, 3, 4, None, 5, 6]
#        1
#       / \
#      2   3
#     /   / \
#    4   5   6
tree = build_tree_from_list([1, 2, 3, 4, None, 5, 6])


# Build tree recursively
def build_tree_recursive(vals, idx=0):
    """Build tree from list using recursive approach"""
    if idx >= len(vals) or vals[idx] is None:
        return None

    node = TreeNode(vals[idx])
    node.left = build_tree_recursive(vals, 2 * idx + 1)
    node.right = build_tree_recursive(vals, 2 * idx + 2)
    return node


# ============================================================================
# 2. READ - TRAVERSALS
# ============================================================================


# Inorder: Left -> Root -> Right
def inorder_traversal(root):
    """Inorder traversal: returns list"""
    result = []

    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

    dfs(root)
    return result


# Iterative inorder
def inorder_iterative(root):
    """Inorder traversal using stack"""
    result = []
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


# Preorder: Root -> Left -> Right
def preorder_traversal(root):
    """Preorder traversal: returns list"""
    result = []

    def dfs(node):
        if node:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return result


# Iterative preorder
def preorder_iterative(root):
    """Preorder traversal using stack"""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# Postorder: Left -> Right -> Root
def postorder_traversal(root):
    """Postorder traversal: returns list"""
    result = []

    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

    dfs(root)
    return result


# Iterative postorder
def postorder_iterative(root):
    """Postorder traversal using two stacks"""
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    return [node.val for node in reversed(stack2)]


# Level-order (BFS)
def levelorder_traversal(root):
    """Level-order traversal: returns list of lists"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Level-order (flat list)
def levelorder_flat(root):
    """Level-order traversal: returns flat list"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# ============================================================================
# 2. READ - SEARCH & FIND
# ============================================================================


# Search for value
def search(root, val):
    """Search for value in tree, returns node if found"""
    if not root or root.val == val:
        return root

    left = search(root.left, val)
    if left:
        return left

    return search(root.right, val)


# Search in BST (Binary Search Tree)
def search_bst(root, val):
    """Search in BST - O(log n) average"""
    if not root or root.val == val:
        return root

    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)


# Find minimum value
def find_min(root):
    """Find minimum value in tree"""
    if not root:
        return None

    min_val = root.val
    if root.left:
        min_val = min(min_val, find_min(root.left))
    if root.right:
        min_val = min(min_val, find_min(root.right))

    return min_val


# Find minimum in BST
def find_min_bst(root):
    """Find minimum in BST - leftmost node"""
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val


# Find maximum value
def find_max(root):
    """Find maximum value in tree"""
    if not root:
        return None

    max_val = root.val
    if root.left:
        max_val = max(max_val, find_max(root.left))
    if root.right:
        max_val = max(max_val, find_max(root.right))

    return max_val


# Find maximum in BST
def find_max_bst(root):
    """Find maximum in BST - rightmost node"""
    if not root:
        return None
    while root.right:
        root = root.right
    return root.val


# Find path to node
def find_path(root, val):
    """Find path from root to node with value val"""
    path = []

    def dfs(node, target):
        if not node:
            return False

        path.append(node.val)

        if node.val == target:
            return True

        if dfs(node.left, target) or dfs(node.right, target):
            return True

        path.pop()
        return False

    dfs(root, val)
    return path if path and path[-1] == val else []


# ============================================================================
# 3. UPDATE
# ============================================================================


# Update node value
def update_node(root, old_val, new_val):
    """Update node value from old_val to new_val"""
    node = search(root, old_val)
    if node:
        node.val = new_val
        return True
    return False


# Update all occurrences
def update_all(root, old_val, new_val):
    """Update all nodes with old_val to new_val"""
    if not root:
        return

    if root.val == old_val:
        root.val = new_val

    update_all(root.left, old_val, new_val)
    update_all(root.right, old_val, new_val)


# Update node by path
def update_by_path(root, path, new_val):
    """Update node at given path (list of 'L' or 'R')"""
    node = root
    for direction in path:
        if direction == "L":
            node = node.left
        elif direction == "R":
            node = node.right
        else:
            return False

        if not node:
            return False

    node.val = new_val
    return True


# ============================================================================
# 4. DELETE
# ============================================================================


# Delete node by value (general tree)
def delete_node(root, val):
    """Delete node with given value, returns new root"""
    if not root:
        return None

    if root.val == val:
        # Case 1: Leaf node
        if not root.left and not root.right:
            return None

        # Case 2: One child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Two children - find inorder successor
        successor = find_min_node(root.right)
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)
        return root

    root.left = delete_node(root.left, val)
    root.right = delete_node(root.right, val)
    return root


# Helper: Find minimum node
def find_min_node(root):
    """Find node with minimum value"""
    while root.left:
        root = root.left
    return root


# Delete in BST
def delete_bst(root, val):
    """Delete node in BST, returns new root"""
    if not root:
        return None

    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # Found node to delete
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Two children: find inorder successor (min in right subtree)
        successor = find_min_node(root.right)
        root.val = successor.val
        root.right = delete_bst(root.right, successor.val)

    return root


# Delete subtree
def delete_subtree(root, val):
    """Delete entire subtree rooted at node with value val"""
    if not root:
        return None

    if root.val == val:
        return None

    root.left = delete_subtree(root.left, val)
    root.right = delete_subtree(root.right, val)
    return root


# Clear entire tree
def clear_tree(root):
    """Delete all nodes in tree"""
    if root:
        clear_tree(root.left)
        clear_tree(root.right)
        root.left = None
        root.right = None
    return None


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


# Tree height/depth
def height(root):
    """Calculate tree height"""
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


# Tree size (number of nodes)
def size(root):
    """Count number of nodes"""
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


# Check if tree is empty
def is_empty(root):
    """Check if tree is empty"""
    return root is None


# Check if node is leaf
def is_leaf(node):
    """Check if node is a leaf"""
    return node and not node.left and not node.right


# Count leaves
def count_leaves(root):
    """Count number of leaf nodes"""
    if not root:
        return 0
    if is_leaf(root):
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


# Visualize tree (simple string representation)
def visualize(root, prefix="", is_left=True):
    """Print tree structure"""
    if not root:
        return

    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))

    if root.left or root.right:
        if root.left:
            visualize(root.left, prefix + ("    " if is_left else "│   "), True)
        else:
            print(prefix + ("    " if is_left else "│   ") + "└── None")

        if root.right:
            visualize(root.right, prefix + ("    " if is_left else "│   "), False)
        else:
            print(prefix + ("    " if is_left else "│   ") + "└── None")


# Example usage
if __name__ == "__main__":
    # Create tree
    root = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])

    # Read
    print("Inorder:", inorder_traversal(root))
    print("Preorder:", preorder_traversal(root))
    print("Postorder:", postorder_traversal(root))
    print("Level-order:", levelorder_traversal(root))

    # Search
    node = search(root, 5)
    print("Found node:", node)

    # Update
    update_node(root, 5, 50)
    print("After update:", inorder_traversal(root))

    # Delete
    root = delete_node(root, 2)
    print("After delete:", inorder_traversal(root))

    # Utility
    print("Height:", height(root))
    print("Size:", size(root))
    print("Leaves:", count_leaves(root))
