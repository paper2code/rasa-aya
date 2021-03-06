import unittest

import os
import src_main.call_webhook

import src_main.config


class TestRasaAvailability(unittest.TestCase):
    ## test that sending of messages is possible
    def test_communicating_with_rasa(self):
        sending = src_main.call_webhook(os.environ.get("TEST_USER"), 'hi')
        self.assertEqual(sending, 'success')


if __name__ == '__main__':
    unittest.main()