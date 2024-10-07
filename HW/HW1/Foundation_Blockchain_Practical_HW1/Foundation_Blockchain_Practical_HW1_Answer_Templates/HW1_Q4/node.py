import json
import threading
import sys
from stream import Stream


class Node:
    def __init__(self,
                 uid=None,
                 next=None):

        ''' Network Variables '''
        self.stream = Stream()
        self.address = (self.stream.ip, self.stream.port)
        
        ''' Algorithm Variables '''
        self.uid = uid
        print('node', uid, 'initialized successfully with address:', self.address)

    def run(self):
        self.send_message(str(self.uid).encode())
        while True:
            stream_in_msg = self.stream.read_in_buf()
            for message in stream_in_msg:
                self.handle_message(message)

    def handle_message(self, message):
        print('node', self.uid, "received: ", message)

        message = message.decode()
        # array of recieved messages from other nodes
        msg = []
        n = len(message.split(','))

        for i in range(0, n):
            msg.append(message.split(',')[i])
        print('node ', self.uid, " received: ", message)

        # when we recieved a message : choice what to send; there are 3 posibilities!
        if len(msg) == 1:
            # if the sender msg is beager than us ;send that:
            if int(msg[0]) > int(self.uid):
                out_msg = str(int(msg[0])).encode()
                self.send_message(out_msg)
            # if the input msg is equal to us ; we ar LEADER :))
            elif int(msg[0]) == int(self.uid):
                print(str(self.uid) + ": I am  LEADER")
                out_msg = str(self.uid) + "," + str(self.uid)
                self.send_message(out_msg)
        # in second round others will understand who the leader is...
        elif len(msg) == 2:
            # if our uid is not equal to the input we are not leader :(((
            if str(self.uid) != str(msg[0]):
                print(str(self.uid) + ": " + str(msg[0]) + " is LEADER")
                out_msg = str(msg[0]) + "," + str(msg[0])
                self.send_message(out_msg)
            # When all nodes understood the lesder everything has been finished.no msgs else
            else:
                print("Algorithm TERMINATED")
def send_message(self, msg):
        self.stream.add_message_to_out_msg(msg)
        self.stream.send_messages()