""" This does not work. """

import hello


class Client:
    def __init__(self):
        self.x = hello.Speaker()

    def run(self):
        self.x.sayHello()
