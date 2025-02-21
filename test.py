import zmq
import json

# zeromq 'client'
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555") # connect to the remote socket

# get a recipe with a valid recipe id
print("-"*100)
print("\nRequesting recipe with valid ID, '2' ")
socket.send_json({"recipeID": "2"})
response = socket.recv_json()
print(f"\nMicroservice's response: {json.dumps(response, indent=2)}")

# try to get a recipe without a valid recipe id
print("-"*100)
print("\nRequesting recipe with invalid ID, '50' ")
socket.send_json({"recipeID": "50"})
response = socket.recv_json()
print(f"\nMicroservice's response: {json.dumps(response, indent=2)}")

# search for a recipe with a query that has matches
print("-"*100)
print("\nSearching for recipe with query that has matches, 'pasta' ")
socket.send_json({"searchQuery": "pasta"})
response = socket.recv_json()
print(f"\nMicroservice's response: {json.dumps(response, indent=2)}")

# search for a recipe with a query that doesn't have matches
print("-"*100)
print("\nSearching for recipe with query that doesn't have matches, 'pizza' ")
socket.send_json({"searchQuery": "pizza"})
response = socket.recv_json()
print(f"\nMicroservice's response: {json.dumps(response, indent=2)}")

# send an invalid request
print("-"*100)
print("\nSending an invalid request, 'none' ")
socket.send_json({"none": "none"})
response = socket.recv_json()
print(f"\nMicroservice's response: {json.dumps(response, indent=2)}")

socket.close() # close socket
context.term() # close context
