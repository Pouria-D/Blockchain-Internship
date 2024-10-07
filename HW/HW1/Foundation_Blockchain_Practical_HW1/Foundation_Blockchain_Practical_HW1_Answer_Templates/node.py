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
            stream_in_buff = self.stream.read_in_buf()
            for message in stream_in_buff:
                self.handle_message(message)

    def handle_message(self, message):
        message = message.decode()
        message_buffer = []
        for i in range(len(message.split(','))):
            message_buffer.append(message.split(',')[i])
        print('node ', self.uid, " received: ", message)

    # step 1 to broadcast our message and leader understand he is leader!!!
        if len(message_buffer) == 1:


            if (int(message_buffer[0]) > int(self.uid)):
                sent_message = str(int(message_buffer[0])).encode()
                self.send_message(sent_message)



            elif (int(message_buffer[0]) == int(self.uid)):
                print(str(self.uid) +  ": I'm the leader")
                sent_message = str(self.uid) + "," + str(self.uid)
                self.send_message(sent_message)
    #step 2 others known who is leader
        elif len(message_buffer) == 2:


            if str(self.uid) != str(message_buffer[0]):
                print(str(self.uid) + ": " + str(message_buffer[0]) + " is the leader")
                sent_message = str(message_buffer[0]) + "," + str(message_buffer[0])
                self.send_message(sent_message)


            else:
                print("Algorithm terminated")


    def send_message(self, msg):
        self.stream.add_message_to_out_buff(msg)
        self.stream.send_messages()