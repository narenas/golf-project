class Player: 
    
    def __init__(self , license , name , surname , gender , ggb_id, category  ) : 
        self.license = license
        self.name = name + " " + surname 
        self.gender = gender 
        self.ggb_id = ggb_id
        self.category = category 
        self.result = 180 if category == 1 else 0 


    def set_player_result (self,result) : 
        self.result = result 

    