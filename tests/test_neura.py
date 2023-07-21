import unittest
import os
# os.chdir("tests")
import sys
sys.path.append('..')
from endToEnd import main

os.environ["TEST_MODE"] = "1"

class NeuraTest(unittest.TestCase):
    def test_neura(self):
        print('Start testing...')
        output = main("mix_bugs_1.py", [32,28,28,1], [32,10], "tf", "result")
        print(output)
        print('Testing completed.')

if __name__ == '__main__':
    unittest.main()