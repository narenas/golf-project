import pygsheets

credentials = pygsheets.authorize(service_account_file='/Users/narenas/git/golf-project/lgagolf-golf-project-ca104c4d33e5.json')

class OM: 

    om = credentials.open("puntos_om")
    wks_om = sh.worksheet_by_title("om")
    
    def __init__(self) : 
        self.regular_om = wks_om.get_values(crange="B2:B65" , returnas="matrix")
    

    def calculate_ties (self, position , ties_numbers , tnmt_type ) :   
        if tnmt_type == "R": 
            first_element = position - 1 
            last_element = first_element + ties_numbers
            ties_array = self.regular_om[first_element:last_element]
            sum = 0 
            for points in ties_array : 
                sum  = sum + points
        return sum 

    
