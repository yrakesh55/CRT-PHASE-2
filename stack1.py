def enqueue(Q,ele):
    Q.append(ele)
    print(ele,"inserted into queue")
def dequeue(Q):
    if len(Q)==0:
        print("queue is empty")
        return
    print(Q[0],"is getting deleted")
    Q.pop(0)
Q=[]
enqueue(Q,10)
enqueue(Q,20)
enqueue(Q,30)
enqueue(Q,40)
dequeue(Q)
dequeue(Q)
dequeue(Q)
