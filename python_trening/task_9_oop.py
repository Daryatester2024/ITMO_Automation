from re import search
from symtable import Class


class Button:

    def __init__(self,text,link):
        self.text=text
        self.link=link

# создание экземпляров класса

home = Button( 'домой' , '/home' )
catalog_msk=Button('Каталог' , '/msk/catalog')
# получение доступа к атрибутам
print(home.text)
print('кнопка' + home.text + 'имеет ссылку' + home.link)

print('\n')

print(catalog_msk.text)
print(' Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text=text
        self.link=link
        self.loc=loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)
# создание экземпляров класса"
home_two = ButtonTwo (' домой ',' /home ', ' button#home ')
#вызов метода
print(home_two.click())

# class Input:
#     def __init__(self, text, loc):
#         self.text=text
#         self.loc=loc
# class Button:
#     def __init__(self, text,loc):
#         self.text = text
#         self.loc = loc
# class Title:
#     def __init__(self,text, loc):
#         self.text = text
#         self.loc = loc
# class Link:
#     def __init__(self,text, loc):
#         self.text = text
#         self.loc = loc
#
# search=Input ('Текст 1','loc#two')
# button=Button('Текст 2','loc#1')
# title=Title('Текст 3', 'loc#2')
# link=Link('Текст 4','loc#3')


print(search.text, search.loc)
print(button.text, button.loc)
print(title.text, title.loc)
print(link.text, link.loc)

class Page:
    def __init__(self, url):
        self.url=url

    def get (self):
        print(self.url)
home=Page ('http://pppppp.com')
home.get()

#Другое решение
# # class Soda:
# #     def __init__(self, syrup):
# #         self.syrup=syrup
# #     def show_my_drink(self):
# #         print(self.syrup)
# # Soda_syrup=Soda ('Газировка с добавкой')
# # Soda_not_syrup=Soda('Газировка без добавок')
# # print(Soda_syrup.syrup)
# # print(Soda_not_syrup.syrup)
#
class Soda:
    def __init__(self,ing=None):
        self.ing=ing
    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')
        else:
            print('Обычная газировка')
drink1=Soda ()
drink2=Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()