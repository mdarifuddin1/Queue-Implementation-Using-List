# Code by Md Arif Uddin 
# ID 193207042

queue = []
def enqueue():
    element = input ("Enter the Element")
    queue.append(element)
    print("Added to queue", element)

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("Remeoved element: ",e)
        
def display():
    print(queue)

while True:
    print("select the operation 1.Push 2.Remeoved 3.size .4 exit")
    choice = int(input ()) 
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display ()
    elif choice == 4:
        break
    else:
        print("Enter the choice operation ")
