from ursina import *

class Main(object):
    """The Main Class that instantiates the other classes and starts the ursina main window."""
    def __init__(self):
        self.app = Ursina()
        self.app.run()

main = Main()