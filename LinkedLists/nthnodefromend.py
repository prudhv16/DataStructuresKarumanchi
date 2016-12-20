
class linkedlist():

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

a = linkedlist(1)
b = linkedlist(2,a)
c = linkedlist(3,b)
d = linkedlist(4,c)
e = linkedlist(5,d)
f = linkedlist(6,e)
g = linkedlist(7,f)


head = a
#using two pointers
'''
def nthNodeFromEnd(head,n=0):
    if n < 0:
        return
    temp1 = head
    temp2 = head
    while n:
        if temp2 == None:
            return
        n -= 1
        temp2 = temp2.next
    while temp2.next:
        temp1 = temp1.next
        temp2 = temp2.next
    return temp1
'''
#using hashtable
lookup = {}

def nthNodeFromEnd(head,n=0):
    length = 0
    temp1 = head
    while temp1:
        temp1 = temp1.next
        length += 1
    temp1 = head;length2 = length-1
    while temp1:
        lookup[length2] = temp1
        length2 -= 1
        temp1 = temp1.next
    if n < length:
        return lookup[n]
    return



print nthNodeFromEnd(g,1).data
