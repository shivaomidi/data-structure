class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.back = None
class dlinked_list :
    def __init__(self):
        self.head = None
    def insert_frist(self , x):
        a = dnode(x)
        if self.head is None: 
            self.head = a
            return
        a.next = self.head
        self.head.back = a
        a.next = a
    def insert_last(self , x):
        if self.head is None:
            self.insert_frist(x)
            return
        c = self.head
        while c.next:
            c = c.next
        a = dnode(x)
        c.next = a
        a.back = c
    def insert_after(self , x ,y):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c :
            if c.Data == x:
                if c.next is None:
                    self.insert_last(y)
                    return
                a = dnode(y)
                a.next = c.next
                a.back = c
                a.next.back = a
                c.next = a
                return
            c = c.next
            print("not found")
    def insert_befor(self , x , y):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.insert_frist(y)
                    return
                a = dnode(y)
                a.next = c
                c.back.next = a
                a.back = c.back
                c.back = a
                return
            c = c.next
            print("not found")
    def del_first(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        self.head = c.next
        if self.head:
            self.head.back = None
            del c
    def del_last(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.del_first()
            return
        c.back.next = None
        del c
    def del_befor(self , x):
        if self.head is None or self.head.Data==x:
            print("error")
            return
        c = self.head
        while c :
            if c.Data == x:
                a = c.back
                c.back = a.back
                if a.back:
                    a.back.next = c
                del a
                return
            c = c.next
            print("x not found")
                                                