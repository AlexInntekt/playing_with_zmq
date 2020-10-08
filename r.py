import sys
import zmq
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
while(True):
    string = socket.recv()
    topic, messagedata = string.split()
    print(topic, messagedata)
    time.sleep(1)

print("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
