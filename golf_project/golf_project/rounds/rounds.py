import requests

def get_round_data(round_id):
    base_url = "https://core.golfgamebook.com/online/1/leaderboard/gettournamentleaderboard/"
    json_url = base_url + round_id 
    r = requests.get(json_url)
    json_data = r.json()
    return json_data
    

def get_fixture_data(date): 
    print (date)
    pass
