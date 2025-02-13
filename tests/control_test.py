import unittest
import sys
import os
import io
from unittest.mock import patch
sys.path.append(os.path.abspath('../source'))
from source import control

class Testcase_control(unittest.TestCase):
        
    @patch('builtins.input', side_effect=['1','3'])
    def test_reset(self, mock_input):
        expected_result = [1000, 800, 700, 600], [0, 0, 0, 0]
        result = control.control_process([1000, 800, 700, 600], [1, 1, 1, 1])
        self.assertEqual(expected_result, result)
    
    @patch('builtins.input', side_effect=['5', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_reset_error(self, mock_stdout, mock_input):
        control.control_process([1000, 900, 800, 700], [1, 1, 1, 1])
        output = mock_stdout.getvalue()
        self.assertIn('不正な値です。', output)
        
    @patch('builtins.input', side_effect=['2', '1', '1500', 'y', '3'])
    def test_change_price(self, mock_input):
        expected_result = [1500, 900, 800, 700], [0, 0, 0, 0]
        result = control.control_process([1000, 900, 800, 700], [0, 0, 0, 0])
        self.assertEqual(expected_result, result)
        
    @patch('builtins.input', side_effect=['2', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_reset(self, mock_stdout, mock_input):
        control.control_process([1000, 900, 800, 700], [1, 0, 0, 0])
        output = mock_stdout.getvalue()
        self.assertIn('売上をリセットしてください。', output)
        
    @patch('builtins.input', side_effect=['2', '5', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_price_error(self, mock_stdout, mock_input):
        control.control_process([1000, 900, 800, 700], [0, 0, 0, 0])
        output = mock_stdout.getvalue()
        self.assertIn('不正な値です。', output)
        
    @patch('builtins.input', side_effect=['2', '1', 'f', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_price_string_error(self, mock_stdout, mock_input):
        control.control_process([1000, 900, 800, 700], [0, 0, 0, 0])
        output = mock_stdout.getvalue()
        self.assertIn('不正な値です。', output)
        
    @patch('builtins.input', side_effect=['2', '1', '100', 'n', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_price_cancel(self, mock_stdout, mock_input):
        control.control_process([1000, 900, 800, 700], [0, 0, 0, 0])
        output = mock_stdout.getvalue()
        self.assertIn('キャンセルしました。', output)
    
        
   