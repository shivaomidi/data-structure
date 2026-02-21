#node گره
class node :
    def __init__(self , d):
        self.Data = d
        self.next = None

class linkedlist :
    def __init__(self):
        self.head = None
        
    def insert_frist(self , x):
        a = node(x) 
        a.next = self.head
        self.head = a  

    def insert_last(self , x):
        if self.head is None:
            self.head = a
            return
        c = self.head
        while c.next:
            c = c.next 
        c.next = a 

    def insert_after(self , x, y):
        if self.head is None: 
            print("list is empty")
            return
        c = self.head
        while c:
         if c.Data == x:
            a = node(y)
            a.next = c.next
            c.next = a 
            return
        c = c.next
    print("not found")

def insert_befor(self , x, y):
    if self.head is None:
        print("list is empty")
        return
    if self.head.Data == x:
        self.insert_frist(y)
        return
    c = self.head
    while c.next:
        if c.next.Data == x:
            a = node(y)
            a.next = c.next
            c.next = a
            return
        c = c.next
        print("not found")
        # تابع نمایش لیست برای تست
    def display(self):
        c= self.head
        while c:
            print(c.Data, end='->')
            c = c.next
            print('None')

            #مثال
            l=linked_list()
            l.insert_frist(10)
            l.insert_last(20)
            l.insert_last(30)
            l.insert_after(20,25)
            l.insert_befor(10,5)
            l.insert_after(100,999)
            l.show()
