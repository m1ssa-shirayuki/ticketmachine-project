import unittest
import sys
import os
import io
from unittest.mock import patch
sys.path.append(os.path.abspath('../source'))
# from source import main
from source import buy

class Testcase_buy(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', '3', '4', 'c', '10000'])
    def test_buy(self, mock_input):
        expected_cart = [1, 1, 1, 1]
        result_cart = buy.buy_process([1000, 800, 700, 600], [0, 0, 0, 0])
        self.assertEqual(result_cart, expected_cart)
    
    @patch('builtins.input', side_effect=['1', 'f', 'c', '10000'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_cart_error(self, mock_stdout, mock_input):
       buy.buy_process([1000, 900, 800, 700], [0, 0, 0, 0])
       output = mock_stdout.getvalue()
       self.assertIn('商品番号を指定してください。', output)
       
    @patch('builtins.input', side_effect=['1', 'c', '900', '1000'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_money_error(self, mock_stdout, mock_input):
        buy.buy_process([1000, 900, 800, 700], [0, 0, 0, 0])
        output = mock_stdout.getvalue()
        self.assertIn('金額が不足しています。', output)
        
    @patch('builtins.input', side_effect=['c', '2', 'c', '1000'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_choose(self, mock_stdout, mock_input):
        buy.buy_process([1000, 900, 800, 700], [0, 0, 0, 0])
        output = mock_stdout.getvalue()
        self.assertIn('商品が選ばれていません。', output)