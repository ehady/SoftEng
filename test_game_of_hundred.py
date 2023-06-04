
import unittest
import mock
from game_of_hundred import game_of_one_hundred
        
class Test_Game_Of_One_Hundred(unittest.TestCase):
    
    def test_is_win_state(self):
        self.assertFalse(game_of_one_hundred(goal=10, number_max_avail=3,\
                                            number_cur=2).is_win_state())
        self.assertTrue(game_of_one_hundred(goal=10, number_max_avail=3,\
                                            number_cur=3).is_win_state())

    def test_is_err_move(self):
        number_old = 2
        human_val = 2
        number_max_avail=3
        with mock.patch('builtins.input', return_value = human_val):
            number_cur, is_err_move = game_of_one_hundred(10, number_max_avail,\
                                                        number_old).human_move()
            self.assertFalse(is_err_move)
            self.assertEqual(number_cur, number_old+human_val)
        with mock.patch('builtins.input', return_value = 101):
            number_cur, is_err_move = game_of_one_hundred(10, number_max_avail, number_old).human_move()
            self.assertTrue(is_err_move)

#if __name__ == "__main__":
    #unittest.main()


