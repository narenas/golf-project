import unittest

from golf_project.rounds import rounds


class TestRoundSettings(unittest.TestCase):

    def test_get_json(self): 
        array_right = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'meta']
        json_data = rounds.get_round_data("2up-ldh2")
        self.assertListEqual(array_right , list(json_data["data"]["primary"].keys()))


if __name__ == '__main__':
    unittest.main()