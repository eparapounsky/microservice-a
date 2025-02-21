import zmq
import json

# get recipes from recipes.json
filepath = "./recipes.json"

def get_recipes(filepath):
    with open(filepath, 'r') as recipe_file:
        return json.load(recipe_file) # returns list of recipes as dictionaries

recipes = get_recipes(filepath)

# zeromq server
context = zmq.Context()
socket = context.socket(zmq.REP) # reply socket
socket.bind("tcp://*:5555") # the socket will listen on network port 5555

# main server loop
while True:
    request = socket.recv_json() # wait for requests from client in json format

    # get parameters from request
    recipe_id = request.get("recipeID")
    search_query = request.get("searchQuery")

    # get recipe by recipe id

    # search recipes by search query