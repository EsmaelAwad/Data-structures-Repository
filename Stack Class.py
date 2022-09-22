l = [0,2,3,4]
print(l[len(l)-1])

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def elements(self):
        return self.items
s = Stack()
print(type(s))

def par_check(string):
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(string) and balanced:
        symbol = string[index]
        
        if symbol == "(" :
            s.push(symbol)
            
        else:
            
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        
        index = index + 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    

print(par_check(")("))

def go_back( history , interval = 0 ):
    
    try:
        s = Stack()
        for link in history:
            s.push(link)
        for i in range(interval):
            s.pop()
            return f"going back to {s.peek()}"
    except IndexError:
        return "you are out of pages."
        
print(go_back(["link 1", "link 2","link 3"],5))

def reverse_string(string):
    
    s = Stack()
    r = Stack()
    
    for i in range(len(string)):
        s.push(string[i])
    for i in range(len(string)):
        
        rev = s.pop()
        r.push(rev)
    
    return r.elements()

print(reverse_string("esmael maher"))