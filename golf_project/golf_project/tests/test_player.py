import pygsheets
import unittest
import sys 

sys.path.append("../")

from rounds import player

gc = pygsheets.authorize(service_account_file='/Users/narenas/git/golf-project/lgagolf-golf-project-ca104c4d33e5.json')

class TestPlayer(unittest.TestCase):

    def test_player_init(self):
        
        test_player_1 = player.Player("xxxxxxxx" , "Nicolas" , "Arenas" , "M" , 123456 , 1 )
        self.assertEqual(test_player_1.license,"xxxxxxxx")
        self.assertEqual(test_player_1.name , "Nicolas Arenas" )
        self.assertEqual(test_player_1.gender , "M")
        self.assertEqual(test_player_1.ggb_id , 123456)
        self.assertEqual(test_player_1.category , 1)
        self.assertEqual(test_player_1.result , 180) 

        test_player_2 = player.Player("xxxxxxxx" , "Nicolas" , "Arenas" , "M" , 123456 , 2 )
        self.assertEqual(test_player_2.license,"xxxxxxxx")
        self.assertEqual(test_player_2.name , "Nicolas Arenas" )
        self.assertEqual(test_player_2.gender , "M")
        self.assertEqual(test_player_2.ggb_id , 123456)
        self.assertEqual(test_player_2.category , 2)
        self.assertEqual(test_player_2.result , 0) 


    def test_set_player_result(self): 
        
        test_player_1 = player.Player("xxxxxxxx" , "Nicolas" , "Arenas" , "M" , 123456 , 1 )
        test_player_1.set_player_result(72)
        self.assertEqual(test_player_1.result, 72 ) 
    
        

if __name__ == '__main__':
    unittest.main()