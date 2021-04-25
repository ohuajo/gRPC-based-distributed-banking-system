import example_pb2
import example_pb2_grpc
import example
import ast
from concurrent import futures
from threading import Thread, Lock
import os
import json
import grpc


class Branch(example_pb2_grpc.RPCServicer):
    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        response = example_pb2.ExampleReply()
        response.outmessage = example.branchupdate(request.inmessage)
        breakdown = ast.literal_eval(str(response.outmessage))
        # unique ID of the Branch
        #self.id = breakdown[0]
        # replica of the Branch's balance
        #self.balance = breakdown[-1]['money']
        # the list of process IDs of the branches
        if len(breakdown) == 3:
            x = [breakdown[1]]
        else:
            x = [breakdown[1], breakdown[3]]
        #self.branches = x
        # the list of Client stubs to communicate with the branches
        #self.stubList = list()
        # a list of received messages used for debugging purpose
        #self.recvMsg = list()
                # iterate the processID of the branches
        # TODO: students are expected to store the processID of the branches
        processIDs = "Branch" + str(breakdown[0]) + " processID(s) are : " + str(x)
        branchfile = "Branch" + str(breakdown[0]) + "_IDs.txt"
        with open(branchfile, "w") as g:
                g.write(processIDs)
        return response


if __name__ == "__main__":
    lock = Lock()
    if os.path.exists('balance.txt'):
        pass
    else:
        lock.acquire()
        with open("balance.txt", "a+") as g:
            with open("input.json") as example_file:
                example_data = json.load(example_file)
                counter = set()
                for i in range(len(example_data)):
                    if example_data[i]['type'] == 'branch':
                        if example_data[i]['balance'] not in counter:
                            g.write(str(example_data[i]['balance']))
                            counter.add(example_data[i]['balance'])
                            lock.release()
    # Section for getting servers actively listening to the appropriate port.
    print('id:')
    idno = input()
    with open("input.json") as example_file:
        example_data = json.load(example_file)
        for i in range(len(example_data)):
            if example_data[i]['type'] == 'branch' and example_data[i]['id'] == int(idno):
                server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
                example_pb2_grpc.add_RPCServicer_to_server(Branch(), server)
                trans_spec = 50047 + int(example_data[i]['id'])
                server.add_insecure_port('[::]:'+ str(trans_spec))
                server.start()
                server.wait_for_termination()