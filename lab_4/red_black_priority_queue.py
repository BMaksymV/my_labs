class Color:
    RED = 1
    BLACK = 0


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority        
        self.color = Color.RED
        self.left = self.right = self.parent = None


class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, None)
        self.NIL.color = Color.BLACK
        self.NIL.left = self.NIL.right = self.NIL
        self.root = self.NIL

    def insert(self, value, priority):
        z = Node(value, priority)
        z.left = z.right = self.NIL

        y, x = None, self.root
        while x != self.NIL:
            y = x
            x = x.left if z.priority >= x.priority else x.right

        z.parent = y
        if not y:
            self.root = z
        elif z.priority >= y.priority:
            y.left = z
        else:
            y.right = z

        if not z.parent:
            z.color = Color.BLACK
        else:
            self.fix_insert(z)

    def fix_insert(self, z):
        while z.parent and z.parent.color == Color.RED:
            gp = z.parent.parent
            if z.parent == gp.left:
                u = gp.right
                if u.color == Color.RED:
                    z.parent.color = u.color = Color.BLACK
                    gp.color = Color.RED
                    z = gp
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.BLACK
                    gp.color = Color.RED
                    self.right_rotate(gp)
            else:
                u = gp.left
                if u.color == Color.RED:
                    z.parent.color = u.color = Color.BLACK
                    gp.color = Color.RED
                    z = gp
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.BLACK
                    gp.color = Color.RED
                    self.left_rotate(gp)
        self.root.color = Color.BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def max(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def peek(self):
        if self.root == self.NIL:
            return None
        n = self.max(self.root)
        return n.value, n.priority

    def pop(self):
        if self.root == self.NIL:
            return None
        z = self.max(self.root)
        res = (z.value, z.priority)
        self.delete(z)
        return res

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, z):
        y, y_color = z, z.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = z.right
            while y.left != self.NIL:
                y = y.left
            y_color = y.color
            x = y.right
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_color == Color.BLACK:
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK