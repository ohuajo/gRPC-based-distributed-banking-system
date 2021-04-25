import ast
from threading import Thread, Lock
import time

                              
# This function takes a subset of request and update the balance in a "balance.txt" file, 
# if a withdrawal or deposit is made. This essentially does the work of Branch to Branch interface, 
# by updating the balance through a file lock system to avoid concurrent update. 
# This file serves as the "database" of the balance which is accessible and updateable by each Branch.
# The function also generates part of what will ultimately be the message returned to the client.
def eventdict(x):
    events = x
    lock = Lock()
    if events["interface"] == 'deposit':
        lock.acquire()
        with open("balance.txt", "r") as g:
            q = g.read()
            l = events["money"] + int(q)
            with open("balance.txt", "w") as g:
                g.write(str(l))
                lock.release()
                branchmessage = [events["id"], {'interface':'deposit', 'result':'success', 'money':l}]
    elif events["interface"] == 'withdraw':
        lock.acquire()
        with open("balance.txt", "r") as g:
            q = g.read()
            l = int(q) - events["money"]
            with open("balance.txt", "w") as g:
                g.write(str(l))
                lock.release()
                branchmessage = [events["id"], {'interface':'deposit', 'result':'success', 'money':l}]
    else:
        with open("balance.txt", "r") as g:
            q = g.read()
            l = int(q)
            branchmessage = [events["id"], {'interface':'deposit', 'result':'success', 'money':l}]
    return branchmessage

# This function accepts the request from the client, split the "events" part into each dictionary 
# and pass the dictionary to the eventdict function for processing. 
# The returns from eventdict is processed into the final message that is returned to the client
def branchupdate(x):
    w = ast.literal_eval(x)
    finalmessage = [w[0]]
    events = w[1]
    for y in range(len(events)):
        z = eventdict(events[y])
        finalmessage.append(z[0])
        finalmessage.append(z[1])
    finalmessage1 = str(finalmessage)
    return finalmessage1