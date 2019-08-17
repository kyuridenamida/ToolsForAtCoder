import os
import tempfile
import unittest
from logging import getLogger, DEBUG, Formatter, StreamHandler

from atcodertools.constprediction.constants_prediction import predict_constants, predict_modulo, \
    MultipleModCandidatesError, predict_yes_no, YesNoPredictionFailedError
from tests.utils.gzip_controller import make_html_data_controller

ANSWER_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    './resources/test_constpred/answer.txt')

logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler()
formatter = Formatter("%(asctime)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def _to_str(x):
    if x is None:
        return ""
    return str(x)


class TestConstantsPrediction(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.html_data_controller = make_html_data_controller(
            tempfile.mkdtemp())
        self.test_dir = self.html_data_controller.create_dir()

    def tearDown(self):
        self.html_data_controller.remove_dir()

    def test_predict_constants(self):
        with open(ANSWER_FILE, 'r') as f:
            answers = f.read().split("\n")

        agc_html_paths = [path for path in sorted(
            os.listdir(self.test_dir)) if "agc" in path]
        for html_path, answer_line in zip(agc_html_paths, answers):
            logger.debug("Testing {}".format(html_path))
            constants = predict_constants(self._load(html_path))
            output_line = "{:40} [mod]{:10} [yes]{:10} [no]{:10}".format(html_path.split(".")[0],
                                                                         _to_str(
                                                                             constants.mod),
                                                                         _to_str(
                                                                             constants.yes_str),
                                                                         _to_str(constants.no_str))
            self.assertEqual(answer_line.rstrip(), output_line.rstrip())

    def test_yes_no_prediction_fails_when_failing_to_parse_html(self):
        try:
            predict_yes_no("broken html")
            self.fail("Must not reach here")
        except YesNoPredictionFailedError:
            pass

    def test_modulo_prediction_fails_with_multi_mod_cands(self):
        try:
            predict_modulo(
                "<p>101で割った余りを出力してください。もしくは n modulo 103を出力してください。</p>")
            self.fail("Must not reach here")
        except MultipleModCandidatesError:
            pass

    def test_case_only_with_no_str(self):
        yes_str, no_str = predict_yes_no(self._load("agc001-D.html"))
        self.assertEqual(None, yes_str)
        self.assertEqual("Impossible", no_str)

    @unittest.expectedFailure
    def test_tricky_mod_case_that_can_raise_multi_cands_error(self):
        # This test exists in order to demonstrate the current wrong behavior that throws MultipleModCandidatesError.
        # None is the true answer for ABC103-C. This test shouldn't fail with a better prediction method.
        # Please remove @unittest.expectedFailure when predict_modulo() behaves
        # correctly.

        modulo = predict_modulo(self._load("abc103-C.html"))
        self.assertIsNone(modulo)

    @unittest.expectedFailure
    def test_tricky_yes_no_case_difficult_to_recognize(self):
        # This test exists in order to demonstrate the current wrong behavior that doesn't detect some yes/no strings.
        # Please remove @unittest.expectedFailure when predict_yes_no() behaves
        # correctly.

        yes_str, no_str = predict_yes_no(self._load("abc110-B.html"))
        self.assertEqual("War", yes_str)
        self.assertEqual("No War", no_str)

    def _load(self, html_path):
        with open(os.path.join(self.test_dir, html_path), 'r') as f:
            return f.read()


if __name__ == '__main__':
    unittest.main()
