import unittest
import os
import sys
sys.path.append('..')
import endToEnd

class NeuraSum(unittest.TestCase):
    def test_neura():
        print('Start testing...')
        output = endToEnd.main("mix_bugs_1", [32,28,28,1], [32,10], "tf", "result")
        print(output)
        print('Testing completed.')