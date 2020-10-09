import sys
import zmq
import time

port = "5557"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    topic =  sys.argv[2]
    topic = str(topic)
    
    
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)


socket.connect ("tcp://localhost:%s" % port)



socket.setsockopt_string(zmq.SUBSCRIBE, topic)

# Process 5 updates
while(True):
    string = socket.recv()
    topic, messagedata = string.split()
    print(topic, messagedata)
    time.sleep(1)


