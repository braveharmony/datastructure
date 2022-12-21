
class mydeque:
    class node:
        def __init__(self,val):
            self.front=0
            self.rest=0
            self.val=val
    def __init__(self):
        self.head=self.node(0)
        self.head.front=self.head
        self.head.rest=self.head
    def add_first(self,val):
        x=self.node(val)
        x.front=self.head
        x.rest=self.head.rest
        x.front.rest=x
        x.rest.front=x
        self.head.val+=1
    def add_rest(self,val):
        x=self.node(val)
        x.rest=self.head
        x.front=self.head.front
        x.rest.front=x
        x.front.rest=x
        self.head.val += 1
    def remove_first(self):
        if len(self) >0:
            x=self.head.rest
            x.front.rest=x.rest
            x.rest.front=x.front
            self.head.val -= 1
            return x.val
        else:raise Exception("deque is empty")
    def remove_rest(self):
        if len(self) > 0:
            x = self.head.front
            x.front.rest = x.rest
            x.rest.front = x.front
            self.head.val -= 1
            return x.val
        else:raise Exception("deque is empty")
    def __str__(self):
        a=str()
        for i in self:
            a+=str(i)+" "
        a.rstrip(" ")
        return a
    def __len__(self):
        return self.head.val
    def __iter__(self):
        self.currentnode=self.head
        return self
    def __next__(self):
        if self.currentnode.rest!=self.head:
            self.currentnode=self.currentnode.rest
            return self.currentnode.val
        else: raise StopIteration
    def __getitem__(self, item):
        if item >= len(self) or -item > len(self):
            raise Exception("IndexError: index out of range")
        else:
            if item >= 0:
                currentnode = self.head.rest
                for _ in range(item):
                    currentnode = currentnode.rest
            else:
                currentnode = self.head
                for _ in range(-item):
                    currentnode = currentnode.front
            return currentnode.val
