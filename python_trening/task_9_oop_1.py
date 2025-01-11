class Input :
    def __init__(self, text, loc):
        self.text=text
        self.loc=loc
class Button :
    def __init__(self, text,loc):
        self.text = text
        self.loc = loc
class Title :
    def __init__(self,text, loc):
        self.text = text
        self.loc = loc
class Link:
    def __init__(self,text, loc):
        self.text = text
        self.loc = loc

search=Input ('Текст 1','loc#two')
button=Button('Текст 2','loc#1')
title=Title('Текст 3', 'loc#2')
link=Link('Текст 4','loc#3')


print(search.text, search.loc)
print(button.text, button.loc)
print(title.text, title.loc)
print(link.text, link.loc)
