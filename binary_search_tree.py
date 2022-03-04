class BinarySearchTree:
    def __init__(self,value):
        self.value=value
        self.children=[None,None]

    def add(self,node):
        if node.value<self.value:
            if self.children[0]==None:
                self.children[0]=node
            else:
                self.children[0].add(node)
        elif node.value>self.value:
            if self.children[1]==None:
                self.children[1]=node
            else:
                self.children[1].add(node)

    def search(self,val):
        if val==self.value:
            return True
        elif val<self.value:
            if self.children[0]==None:
                return False
            else:
                return self.children[0].search(val)
        elif val>self.value:
            if self.children[1]==None:
                return False
            else:
                return self.children[1].search(val)

lst=[39,23,70,19,35,64,97,15,22,31,38,42,69,76,98]
bst=BinarySearchTree(lst[0])
for i in range(1,len(lst)):
    n=BinarySearchTree(lst[i])
    bst.add(n)

print(bst.search(98))