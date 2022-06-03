class Node():
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class Link():
    def __init__(self):
        self.head = None
    def insertdata(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print('empty')
            return
        itr = self.head
        llstr = ''


        while itr:
            llstr += str(itr.data) + '>'
            itr = itr.next
            #print(itr)
        print(llstr)

a = Link()
a.insertdata(5)
a.insertdata(10)
a.print()

        


        