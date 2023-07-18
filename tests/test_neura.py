import unittest
import os
print(os.getcwd())
os.chdir("tests")
print(os.getcwd())
import sys
sys.path.append('..')
from endToEnd import main
# import shutil

# shutil.copyfile(src='tests/', dst='tests/endToEnd.py')

# from ..endToEnd import main

class NeuraSum(unittest.TestCase):
    def test_neura():
        print('Start testing...')
        output = main("mix_bugs_1", [32,28,28,1], [32,10], "tf", "result")
        print(output)
        print('Testing completed.')

