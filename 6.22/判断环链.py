class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def is_circle(head):
    pre=head
    cur=head
    while cur and cur.next:
        pre=pre.next
        cur=cur.next.next
        if pre==cur:
            return True
    return False
if __name__ == '__main__':
    h=Node(0)
    a=Node(1)
    b=Node(2)
    c=Node(3)
    d=Node(4)
    e=Node(5)
    h.next=a
    a.next=b
    b.next=c
    c.next=e
    e.next=b
    print(is_circle(h))
