import json
from flask import Flask, jsonify, request, Response
from FootballRankingModel import *
from settings import *


def football_ranking_object_is_valid(football_ranking):
    print(football_ranking)
    if ("Wins" in football_ranking) and ("Coach" in football_ranking) and ("Name" in football_ranking):
        return True
    else:
        print("Error from main.football_ranking_object_is_valid")
        return False


# GET /football_ranking
@app.route('/football_ranking')
def get_football_ranking():
    return jsonify(FootballRanking.get_all_lines())

# POST /football_ranking
@app.route('/football_ranking', methods=['POST'])
def add_line():
    request_data = request.get_json()
    if football_ranking_object_is_valid(request_data):
        print (request_data['Name'])
        FootballRanking.add_line(
            request_data['Name'],
            request_data['Wins'],
            request_data['Coach'])
        response = Response("OK", 201, mimetype='application/json')
        return response
    else:
        invalid_football_ranking_object = {
            "error": "Invalid ns_cos object passed in the request!",
            "help_string": "Hello dear friend! Data passed should be a bit similar to the expected JSON!"
        }
        response = Response(json.dumps(invalid_ns_cos), status=400, mimetype='application/json')
        return response


app.run(port=4000, debug=True)
