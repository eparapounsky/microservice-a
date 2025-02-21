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
    # empty string is default value to return if key is not found in dictionary
    recipe_id = request.get("recipeID", "")
    search_query = request.get("searchQuery", "").lower()

    # get recipe by recipe id
    if recipe_id:
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                socket.send_json(recipe)

        continue # skip to next iteration of while loop

    # search recipes by search query
    if search_query:
        search_results = []

        # for recipe in recipes:
        #     if search_query in recipe["name"].lower():
        #         search_results.append(recipe)

        for recipe in recipes:
            matching_names = search_query in recipe["name"].lower()

            if matching_names:
                search_results.append(recipe)

        socket.send_json(search_results)
