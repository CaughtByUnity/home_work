class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square(self):
        print(self.width * self.height)
    def perimeter(self):
        print(2 * (self.width + self.height))

A = Rectangle(4, 5)

A.square()
A.perimeter()

B = Rectangle(10, 13.7)

B.square()
B.perimeter()

C = Rectangle(28, 15)

C.square()
C.perimeter()

class Math:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
    def addition(self, a, b):
        print(a + b)
    def multiplication(self, a, b):
        print(a * b)
    def division(self, a, b):
        print(a / b)
    def subtraction(self, a ,b):
        print(a - b)

numbers = Math()

numbers.addition(10, 5)
numbers.multiplication(50, 10)
numbers.division(100, 20)
numbers.subtraction(5, 3)

class Button:
    type: str = 'Кнопка'
    loc: str = ' '
    def __init__(self,text):
        self.text = text
    def click(self):
        print(f"Клик по кнопке {self.text}")

text_box = Button('Text Box')

print(text_box.text)
text_box.click()

check_box = Button('Check Box')

print(check_box.text)
check_box.click()

radio_button = Button('Radio Button')

print(radio_button.text)
radio_button.click()

web_tables = Button('Web Tables')

print(web_tables.text)
web_tables.click()

buttons = Button('Buttons')

print(buttons.text)
buttons.click()

links = Button('Links')

print(links.text)
links.click()

broken_links = Button('Broken Links - Images')

print(broken_links.text)
broken_links.click()

upload_and_download = Button('Upload and Download')

print(upload_and_download.text)
upload_and_download.click()

dynamic_properties = Button('Dynamic Properties')

print(dynamic_properties.text)
dynamic_properties.click()