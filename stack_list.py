class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        if len(Stack)==0:
            return True
        else:
            return False
st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.pop()
print(st.peek())