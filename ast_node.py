class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value  # operator (AND/OR) or operand value
        self.left = left  # left child
        self.right = right  # right child

    def __repr__(self):
        if self.type == "operator":
            return f"({self.value} {self.left} {self.right})"
        else:
            return str(self.value)