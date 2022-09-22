class Queue:

    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0, item)
    def dequeue(self):
        try:
            return self.items.pop()
        except:
            return "The list is empty"
    def size(self):
        return len(self.items)
    def elements(self):
        return self.items

q = Queue()
q.enqueue(4)
q.enqueue(True)
q.enqueue("Esmael")
q.dequeue()
q.dequeue()
q.dequeue()
print(q.elements())

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()
print(hot_potato(["ali","ahmed","mohamed"], 4))