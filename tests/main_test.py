import unittest
import sys
import os
import io
from unittest.mock import patch
sys.path.append(os.path.abspath('../source'))
from source import main

class Testcase_main(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_end(self, mock_stdout, mock_input):
        main.main()
        output = mock_stdout.getvalue()
        self.assertIn('終了が選ばれました。', output)
    
    @patch('builtins.input', side_effect=['u', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_error(self, mock_stdout, mock_input):
        main.main()
        output = mock_stdout.getvalue()
        self.assertIn('数字を入力してください。', output)