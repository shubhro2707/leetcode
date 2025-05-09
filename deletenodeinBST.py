from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:  # Base case: Tree is empty or node not found
            return root
        
        # Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # Search in left subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)  # Search in right subtree
        else:  # Found the node to delete
            if not root.left:  # Case 1 & 2: No left child or no children
                return root.right
            elif not root.right:  # Case 1 & 2: No right child
                return root.left
            
            # Case 3: Node has two children
            min_larger_node = self.findMin(root.right)  # Find inorder successor
            root.val = min_larger_node.val  # Replace value with inorder successor
            root.right = self.deleteNode(root.right, min_larger_node.val)  # Delete successor

        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:  # Smallest node is the leftmost node
            node = node.left
        return node