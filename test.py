import zmq

# zeromq 'client'
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555") # connect to the remote socket

# get a recipe with a valid recipe id
print("Getting recipe with valid ID, '1' ")

# try to get a recipe without a valid recipe id
print("Getting recipe with invalid ID, '50' ")

# search for a recipe with a query that has matches
print("Searching for recipe with query that has matches, 'pasta' ")

# search for a recipe with a query that doesn't have matches
print("Searching for recipe with query that doesn't have matches, 'pizza' ")

# send an invalid request
print("Sending an invalid request, 'none' ")