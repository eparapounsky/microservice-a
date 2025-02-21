import zmq

# zeromq 'client'
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555") # connect to the remote socket

# get a recipe with a valid recipe id
print("Getting recipe with valid ID, '1' ")
socket.send_json({"recipeID": "1"})
response = socket.recv_json()
print(f"Microservice's response: {response}")

# try to get a recipe without a valid recipe id
print("Getting recipe with invalid ID, '50' ")
socket.send_json({"recipeID": "50"})
response = socket.recv_json()
print(f"Microservice's response: {response}")

# search for a recipe with a query that has matches
print("Searching for recipe with query that has matches, 'pasta' ")
socket.send_json({"searchQuery": "pasta"})
response = socket.recv_json()
print(f"Microservice's response: {response}")

# search for a recipe with a query that doesn't have matches
print("Searching for recipe with query that doesn't have matches, 'pizza' ")
socket.send_json({"searchQuery": "pizza"})
response = socket.recv_json()
print(f"Microservice's response: {response}")

# send an invalid request
print("Sending an invalid request, 'none' ")
socket.send_json({"none": "none"})
response = socket.recv_json()
print(f"Microservice's response: {response}")

socket.close() # close socket
context.term() # close context