import requests

class Rounds: 


    base_url = "https://core.golfgamebook.com/online/1/leaderboard/gettournamentleaderboard/"

    def __init__(self , round_id , round_type ): 
        self.round_id = round_id 
        self.round_type = round_type 
        if self.round_type == 'R': 
            self.first_game = "side"
            self.second_game = "primary"
        else: 
            self.first_game = "primary"
            self.second_game = "side"


    def get_round_data(self):
        json_url = base_url + self.round_id 
        r = requests.get(json_url)
        json_data = r.json()
        return json_data
    

    def get_results( self ,  category , json_data , round_type ):
        division_result = {}
        if category == 1:  
            for result in json_data: 
                player_id = ["data"][self.first_game][result]["player"]["id"]
                score = ["data"][self.first_game][result]["player"]["score"]
                division_result[player_id] = score
        if category == 2: 
            for result in json_data: 
                player_id = ["data"][self.second_game][result]["player"]["id"]
                score = ["data"][self.second_game][result]["player"]["score"]
                division_result[player_id] = score
        return division_result