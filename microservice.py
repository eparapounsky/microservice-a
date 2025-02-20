 # Pseudocode for requesting data from the microservice
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Requesting a specific recipe by ID
request_data = {"action": "get_recipe", "recipeID": "123"}
socket.send_json(request_data)
response = socket.recv_json()
print(response)

# Searching for recipes by keyword
request_data = {"action": "search_recipes", "searchQuery": "chicken"}
socket.send_json(request_data)
response = socket.recv_json()
print(response)