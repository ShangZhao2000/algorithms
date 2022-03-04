class MinHeap:
    def __init__(self,value):
        self.value=value
        self.children=[None,None]
        self.next_node=None

    def link(self,next_node):
        self.next_node=next_node

    def next(self):
        return self.next_node

    def add(self,node):
        if self.children[0]==None:
            self.children[0]=node
        elif self.children[1]==None:
            self.children[1]=node
            self.children[0].link(self.children[1])
        else:
            if self.next==None:
                self.children[0].add(node)