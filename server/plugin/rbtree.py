#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from random import randint

RED = 'R'
BLACK = 'B'

class RBTree():
    class __RBTreeNode():
        '''''节点类型'''

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.parent = None
            self.color = '*'

        def paint(self, color):
            self.color = color

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            if (self.val != None):
                yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem

                    # 迭代的是Node类型，用于删除结点

        def iternodes(self):
            if self.left != None:
                for elem in self.left.iternodes():
                    yield elem

            if self != None and self.val != None:
                yield self

            if self.right != None:
                for elem in self.right.iternodes():
                    yield elem

        def info(self):
            s = 'Key=' + str(self.val) + ', ' + \
                'LChild=' + str(self.left) + ', ' + \
                'RChild=' + str(self.right) + ', ' + \
                'parent=' + str(self.parent) + ', ' + \
                'Color=' + str(self.color)

            print(s)

        def __str__(self):
            return str(self.val)

        def __repr__(self):
            if self != None:
                s_1 = str(self.val)
            else:
                s_1 = 'None'

            if self.left != None:
                s_2 = str(self.left.val)
            else:
                s_2 = 'None'

            if self.right != None:
                s_3 = str(self.right.val)
            else:
                s_3 = 'None'

            s_4 = str(self.parent)
            s_5 = str(self.color)

            return '__RBTreeNode(' + s_1 + ', ' + s_2 + ', ' + s_3 + ', ' + s_4 + ', ' + s_5 + ')'

    def __init__(self):
        # self.items = []
        self.root = None
        self.zlist = []

    def LRotate(self, x):
        # x是一个RBTree.__RBTreeNode
        y = x.right
        if y is None:
            # 右节点为空，不旋转
            pass
        else:
            beta = y.left
            x.right = beta
            if beta is not None:
                beta.parent = x

            p = x.parent
            y.parent = p
            if p is None:
                # x原来是root
                self.root = y
            elif x == p.left:
                p.left = y
            else:
                p.right = y
            y.left = x
            x.parent = y

    def RRotate(self, y):
        # y是一个节点
        x = y.left
        if x is None:
            # 左节点为空，不旋转
            pass
        else:
            beta = x.right
            y.left = beta
            if beta is not None:
                beta.parent = y

            p = y.parent
            x.parent = p
            if p is None:
                # y原来是root
                self.root = x
            elif y == p.left:
                p.left = x
            else:
                p.right = x
            x.right = y
            y.parent = x


            # 插入

    def insert(self, val):
        z = RBTree.__RBTreeNode(val)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right

        z.paint(RED)
        z.parent = y

        if y is None:
            # 插入z之前为空的RBTree
            self.root = z
            self.insert_Fixup(z)
            return

        if z.val < y.val:
            y.left = z
        else:
            y.right = z

        if y.color == RED:
            # z的父节点y为红色，需要fixup。
            # 如果z的父节点y为黑色，则不用调整
            self.insert_Fixup(z)

        else:
            return

    def insert_Fixup(self, z):
        # case 1:z为root节点
        if z.parent is None:
            z.paint(BLACK)
            self.root = z
            return

            # case 2:z的父节点为黑色
        if z.parent.color == BLACK:
            # 包括了z处于第二层的情况
            # 这里感觉不必要啊。。似乎z.parent为黑色则不会进入fixup阶段
            return

            # 下面的几种情况，都是z.parent.color == RED:
        # 节点y为z的uncle
        p = z.parent
        g = p.parent  # g为x的grandpa
        if g is None:
            return
            #   return 这里不能return的。。。
        if g.right == p:
            y = g.left
        else:
            y = g.right

            # case 3-0:z没有叔叔。即：y为NIL节点
        # 注意，此时z的父节点一定是RED
        if y == None:
            if z == p.right and p == p.parent.left:
                # 3-0-0:z为右儿子,且p为左儿子，则把p左旋
                # 转化为3-0-1或3-0-2的情况
                self.LRotate(p)
                p, z = z, p
                g = p.parent
            elif z == p.left and p == p.parent.right:
                self.RRotate(p)
                p, z = z, p

            g.paint(RED)
            p.paint(BLACK)
            if p == g.left:
                # 3-0-1:p为g的左儿子
                self.RRotate(g)
            else:
                # 3-0-2:p为g的右儿子
                self.LRotate(g)

            return

            # case 3-1:z有黑叔
        elif y.color == BLACK:
            if p.right == z and p.parent.left == p:
                # 3-1-0:z为右儿子,且p为左儿子,则左旋p
                # 转化为3-1-1或3-1-2
                self.LRotate(p)
                p, z = z, p
            elif p.left == z and p.parent.right == p:
                self.RRotate(p)
                p, z = z, p

            p = z.parent
            g = p.parent

            p.paint(BLACK)
            g.paint(RED)
            if p == g.left:
                # 3-1-1:p为g的左儿子，则右旋g
                self.RRotate(g)
            else:
                # 3-1-2:p为g的右儿子，则左旋g
                self.LRotate(g)

            return

            # case 3-2:z有红叔
        # 则涂黑父和叔，涂红爷，g作为新的z，递归调用
        else:
            y.paint(BLACK)
            p.paint(BLACK)
            g.paint(RED)
            new_z = g
            self.insert_Fixup(new_z)

            # 删除

    def delete(self, val):
        curNode = self.root
        while curNode is not None:
            if val < curNode.val:
                curNode = curNode.left
            elif val > curNode.val:
                curNode = curNode.right
            else:
                # 找到了值为val的元素,正式开始删除
                if curNode.left is None and curNode.right is None:
                    # case1:curNode为叶子节点：直接删除即可
                    if curNode == self.root:
                        self.root = None
                    else:
                        p = curNode.parent
                        if curNode == p.left:
                            p.left = None
                        else:
                            p.right = None

                elif curNode.left is not None and curNode.right is not None:
                    sucNode = self.SUCCESOR(curNode)
                    curNode.val, sucNode.val = sucNode.val, curNode.val
                    self.delete(sucNode.val)

                else:
                    p = curNode.parent
                    if curNode.left is None:
                        x = curNode.right
                    else:
                        x = curNode.left
                    if curNode == p.left:
                        p.left = x
                    else:
                        p.right = x
                    x.parent = p
                    if curNode.color == BLACK:
                        self.delete_Fixup(x)
                curNode = None
        return False

    def delete_Fixup(self, x):
        p = x.parent
        # w:x的兄弟结点
        if x == p.left:
            w = x.right
        else:
            w = x.left

            # case1:x的兄弟w是红色的
        if w.color == RED:
            p.paint(RED)
            w.paint(BLACK)
            if w == p.right:
                self.LRotate(p)
            else:
                self.RRotate(p)

        if w.color == BLACK:
            # case2:x的兄弟w是黑色的，而且w的两个孩子都是黑色的
            if w.left.color == BLACK and w.right.color == BLACK:
                w.paint(RED)
                if p.color == BLACK:
                    return
                else:
                    p.color = BLACK
                    self.delete_Fixup(p)

                    # case3:x的兄弟w是黑色的，而且w的左儿子是红色的，右儿子是黑色的
            if w.left.color == RED and w.color == BLACK:
                w.left.paint(BLACK)
                w.paint(RED)
                self.RRotate(w)

                # case4:x的兄弟w是黑色的，而且w的右儿子是红
            if w.right.color == RED:
                p.paint(BLACK)
                w.paint(RED)
                if w == p.right:
                    self.LRotate(p)
                else:
                    self.RRotate(p)

                    # 红黑树信息查询

    def info(self):
        a = []
        for x in self:
            a.append(x)

        print(a)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

            # 传回结点的原始信息

    def iternodes(self):
        if self.root != None:
            return self.root.iternodes()
        else:
            return [None]


            # 查找，返回的是结点

    def find(self, key):
        def _find(key, node):
            if node is None:
                return None
            elif key < node.val:
                return _find(key, node.left)
            elif key > node.val:
                return _find(key, node.right)
            else:
                return node

        if self.root is None:
            return None
        else:
            return _find(key, self.root)

            # 找最小元素

    def findAll(self,key):
        pass

    def findMin(self):
        def _findMin(node):
            if node.left:
                return _findMin(node.left)
            else:
                return node

        if self.root is None:
            return None
        else:
            return _findMin(self.root)



            # 找最大元素

    def findMax(self):
        def _findMax(node):
            if node.right:
                return _findMax(node.right)
            else:
                return node

        if self.root is None:
            return None
        else:
            return _findMax(self.root)

            # 求结点高度

    def height(self, node):
        if (node == None):
            return 0
        else:
            m = self.height(node.left)
            n = self.height(node.right)
            return max(m, n) + 1

            # 寻找节点路径

    def findNodePath(self, root, node):
        path = []
        if root == None or root.val == None:
            path = []
            return path

        while (root != node):
            if node.val < root.val:
                path.append(root)
                root = root.left
            elif node.val >= root.val:
                path.append(root)
                root = root.right
            else:
                break

        path.append(root)
        return path

        # 寻找父结点

    def parent(self, root, node):
        path = self.findNodePath(root, node)
        if (len(path) > 1):
            return path[-2]
        else:
            return None

            # 求某元素是在树的第几层

    # 约定根为0层
    # 这个计算和求结点的Height是不一样的
    def level(self, elem):
        if self.root != None:
            node = self.root
            lev = 0

            while (node != None):
                if elem < node.val:
                    node = node.left
                    lev += 1
                elif elem > node.val:
                    node = node.right
                    lev += 1
                else:
                    return lev

            return -1

        else:
            return -1

    def __len__(self):
        a = []
        for x in self:
            a.append(x)

        return len(a)

    def __contains__(self, val):
        if self.find(val) != None:
            return True

        return False


if __name__ == '__main__':
    rbt = RBTree()
    b = []
    N = 100

    data = [0, 24, 26, 79, 93, 99, 335, 378, 440, 494]
    data2 = [90, 115, 168, 236, 270, 271, 300, 393, 465, 489]

    # 生成随机原始数据
    for i in range(N):
        m = randint(22, 24)
        rbt.insert(m)
        b.append(m)

    print b
    x =rbt.find(23)
    if not x:
        print "not found"
    else:
        x.info()

    #     # 插入
    # for x in data2:
    #     rbt.insert(x)
    #
    # for node in rbt.iternodes():
    #     node.info()
    #
    # print('root:')
    # rbt.root.info()
    #
    # # 删除
    # rbt.delete(236)
    # rbt.delete(233)
    # print('root:')
    # rbt.root.info()
    # print(len(rbt))
    #
    # # 查找
    # p = rbt.find(168)
    # if (p != None):
    #     p.info()
    #
    #     #
    # print('max:')
    # rbt.findMax().info()
    # print('min:')
    # rbt.findMin().info()
    # print('height:', rbt.height(rbt.root))
    # print(168 in rbt)
    # print(1002 in rbt)
    #
    # #
    # for x in rbt.iternodes():
    #     print(rbt.findNodePath(rbt.root, x))
    #     print(rbt.level(x.val))

