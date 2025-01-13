class Rectangle:

    def __init__(self,height, width):
        self.height=height
        self.width=width

    def area_calculation (self):
        print (self.height * self.width)

    def perimeter_rectangle(self):
        print((self.height + self.width) * 2)

figure_1=Rectangle(3,20)

figure_2=Rectangle (5,15)

figure_3=Rectangle(1,3)


figure_1.area_calculation()

figure_2.area_calculation()

figure_3.area_calculation()

figure_1.perimeter_rectangle()

figure_2.perimeter_rectangle()

figure_3.perimeter_rectangle()

class Math:

    def __init__(self, a, b):
        self.a=a
        self.b=b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a/self.b)

    def subtraction(self):
        print(self.a-self.b)

num=Math(30,10)

num.addition()

num.multiplication()

num.division()

num.subtraction()

class Sidebar:

    type: str = 'Кнопка'

    def __init__(self,text,loc=None):
        self.text=text
        self.loc=loc

    def click(self):
        return 'Клик по кнопке - {}'.format(self.text)

text_box=Sidebar ('Text Box')
check_box=Sidebar ('Check box')
radio_button=Sidebar ('Radio Button')
web_tables=Sidebar ('webtables')
buttons=Sidebar ('Buttons')
links=Sidebar ('Links')
broken=Sidebar('Broken Links - Images')
upload=Sidebar('Upload and Download')
dynamic=Sidebar('Dynamic Properties')

print(text_box.text)

print(check_box.text)

print(radio_button.text)

print(web_tables.text)

print(buttons.text)

print(links.text)

print(broken.text)

print(upload.text)

print(dynamic.text)

print(text_box.click())

print(check_box.click())

print(radio_button.click())

print(web_tables.click())

print(buttons.click())

print(links.click())

print(broken.click())

print(upload.click())

print(dynamic.click())

