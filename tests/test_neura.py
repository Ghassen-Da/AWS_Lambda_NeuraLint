import unittest
import os
os.chdir("tests")
import sys
sys.path.append('..')
from endToEnd import main

os.environ["TEST_MODE"] = "1"

class NeuraTest(unittest.TestCase):
    def test_neura(self):
        desired_output="""mix_bugs_1.py\n\rLayer 1 ==> A learning layer should no longer include a bias when it is followed by batchnorm., The local window size for spatial filtering should generally increase or stay the same throughout the convolutional layers.\n\rLayer 3 ==> Batchnorm layer should be before the dropout.\n\rLayer 6 ==> A learning layer should no longer include a bias when it is followed by batchnorm.\n\rLayer 8 ==> Batchnorm layer should be before the dropout.\n\rLayer 12 ==> A learning layer should no longer include a bias when it is followed by batchnorm.\n\rLayer 14 ==> Batchnorm layer should be before the dropout."""
        print('Start testing...')
        output = main("mix_bugs_1.py", [32,28,28,1], [32,10], "tf", "result")
        print('**',output,'**')
        print('**',desired_output,'**')
        find_first_different_character(output, desired_output)
        assert output==desired_output
        print('Testing completed.')


def find_first_different_character(str1, str2):
    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        if str1[i] != str2[i]:
            print(f"First different character: {str1[i+7]} from str1 and {str2[i+7]} from str2")
            return

    # If the loop completes without finding a difference and the lengths are different,
    # print the extra character from the longer string
    if len(str1) != len(str2):
        extra_char = str1[min_len:] if len(str1) > len(str2) else str2[min_len:]
        print(f"First different character: {extra_char} from the longer string")



if __name__ == '__main__':
    unittest.main()