from survey import Survey
import unittest

class TestSurvey(unittest.TestCase):
    def setUp(self):
        question = 'Why?'
        self.survey = Survey(question)

    def test_insert_response_single(self):
        self.survey.insert_response('English')
        self.assertIn('English', self.survey.responses)

    def test_insert_response_multi(self):
        response_sample = ['English', 'Chinese', 'Japanese']
        for item in response_sample:
            self.survey.insert_response(item)

        for response in response_sample:
            self.assertIn(response, self.survey.responses)

if __name__ == '__main__':
    unittest.main()
        