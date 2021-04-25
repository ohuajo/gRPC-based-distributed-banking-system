import grpc
import example_pb2
import example_pb2_grpc
import ast
import json
import os, signal
from concurrent import futures
import subprocess


class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None

    # TODO: students are expected to create the Customer stub
    # TODO: students are expected to send out the events to the Bank
    
    def executeEvents(self):
        # open gRPC channel that is specific for branch-customer transactions.
        trans_spec = 50047 + self.id
        channel = grpc.insecure_channel('localhost:' + str(trans_spec))
        # create a stub (client)
        self.stub = example_pb2_grpc.RPCStub(channel)
        # create a valid request message
        validrequest = str([self.id, self.events])
        string = example_pb2.ExampleRequest(inmessage=validrequest)
        # make the call
        response = self.stub.MsgDelivery(string)
        return response.outmessage

        
if __name__ == "__main__":
    with open("input.json") as example_file:
        example_data = json.load(example_file)
        message_list = []              
        for i in range(len(example_data)):
            if example_data[i]['type'] == 'customer':
                customerrun = Customer(example_data[i]['id'], example_data[i]['events'])
                return_string = customerrun.executeEvents()
                message_list.append(ast.literal_eval(str(return_string)))
        # Creating of output file
        for x in  message_list:
            x[-1]['money'] = message_list[-1][-1]['money']
            if len(x) == 3:
                line_out = "{'id':" + str(x[0]) + ", 'recv':" + str([x[2]]) + "}"
            else:
                firstpart = x[2].pop('money')
                line_out = "{'id':" + str(x[0]) + ", 'recv':" + str([x[2], x[4]]) + "}"
            with open("output.json", "a") as file_object:
                file_object.write(str(line_out))
                file_object.write("\n")
            # Closing of approriate server after writing to output file. 
            pidX1 = 50047 + x[0]
            pidX2 = str(pidX1)+'/tcp'
            pidX3 = subprocess.run(['fuser', '-k', pidX2], capture_output=True)
    # move balance.txt to oldbank_balance.txt
    os.rename('balance.txt', 'old_balance.txt')