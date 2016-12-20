

class linkedlist():

    def __init__(self,data,node=None):
        self.data = data
        self.next = node

a = linkedlist(1)
b = linkedlist(2,a)
c = linkedlist(3,b)
d = linkedlist(4,c)
e = linkedlist(5,d)
f = linkedlist(6,e)
g = linkedlist(7,f)

a.next = d
lookup = {}

'''
def hashCycleDetection(head):
    temp1 = head
    while temp1:
        try:
            lookup[temp1] = 1
            temp1 = temp1.next
        except:
            return "cycle detected"
    return "linked list does not have cycle"
'''

def FloydCycleDetection(head):
    if head and head.next:
        temp1 = head
        temp2 = head
    else:
        return None
    try:
        while temp1 and temp1.next and temp2 and temp2.next.next:
            if temp1 == temp2:
                return "cycle exists"
            temp1 = temp1.next
            temp2 = temp2.next.next
    except AttributeError:
        pass
    return "cycle does not exist"


#Below code is giving wierd error if temp1 is declared as just head
def FloydCycleStartDetection1(head):
    if head and head.next:
        temp1 = head
        temp2 = head
    else:
        return None
    try:
        temp1 = temp1.next
        temp2 = temp1.next
        while temp1 != temp2:
            try:
                temp1 = temp1.next
                temp2 = temp2.next.next
            except AttributeError:
                print "No cycle detected"
                break
        print temp1.data
        temp1 = head
        while temp1 != temp2:
            print temp1.data, temp2.data
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1
    except AttributeError:
        return "cycle does not exist"

def CycleLenght(head):
    temp1 = head.next
    temp2 = head.next.next
    try:

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next.next
        counter = 1
        temp1 = temp1.next
        while temp1 != temp2:
            temp1 = temp1.next
            counter += 1
        return counter
    except:
        return 0

print CycleLenght(g)