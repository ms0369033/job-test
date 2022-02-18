class ListNode(object):
    def __init__(self, val=0, next=None):
    	self.val = val         
    	self.next = next
 	
class Stack:
    index = None
    def pop(self):
        num = self.index.val
        self.index = self.index.next
        return num
    def push(self,num):
        if not self.index:
            list = ListNode()
            self.index = list
        else:
            list = ListNode()
            list.next = self.index
            self.index = list
        self.index.val = num
		
    def size(self):
        count = 0
        head = self.index
        while head:
            count += 1
            head = head.next
        return count
	
stack = Stack()
stack.push(1)
stack.push(2) 
stack.push(3) 
print(stack.pop())
print(stack.size())
