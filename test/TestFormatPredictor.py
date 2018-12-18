import tempfile
import unittest
import os

from test.utils.TestDataUtil import TestDataUtil
from test.utils.TestFormatPredictorRunner import TestFormatPredictorRunner

ANSWER_FILE = "./resources/TestFormatPredictor/answer.txt"


class TestFormatPredictor(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_data_util = TestDataUtil(tempfile.mkdtemp())
        self.test_dir = self.test_data_util.create_dir()

    def tearDown(self):
        self.test_data_util.remove_dir()

    def test_overall(self):
        runner = TestFormatPredictorRunner(self.test_dir)
        case_names = sorted([cand for cand in os.listdir(self.test_dir) if runner.is_valid_case(cand)])
        output_text = ""
        for case in case_names:
            response = runner.run(case)
            if response.status == "OK":
                output_text += "{:40} {:20} {} {}\n".format(case, response.status, response.simple_format,
                                                            response.types)
            else:
                output_text += "{:40} {}\n".format(case, response.status)

        with open(ANSWER_FILE, 'r') as f:
            answer = f.read()
        self.assertEqual(answer, output_text)


if __name__ == "__main__":
    unittest.main()
