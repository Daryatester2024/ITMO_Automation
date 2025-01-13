from python_trening.task_9_oop_1 import search, button, title, link
from task_9_oop_1 import Input
from task_9_oop_1 import Button
from task_9_oop_1 import Title
from task_9_oop_1 import Link

class Checks:

    def __init__(self,loc):
        self.loc = loc

class Input (Checks):

    def __init__(self,loc):
        self.loc = loc

class Button(Checks):

    def __init__(self,loc):
        self.loc = loc

class Title (Checks):

    def __init__(self,loc):
        self.loc=loc

class Link (Checks):

    def __init__(self,loc):
        self.loc=loc

    def check_text(self, loc):

        print(search.check_text())

        print(button.check_text())

        print(title.check_text())

        print(link.check_text())
