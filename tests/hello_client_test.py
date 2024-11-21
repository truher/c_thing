import unittest

from hello_client import client


class HelloClientTest(unittest.TestCase):
    def test_hello(self) -> None:
        x = client.Client()
        x.run()
