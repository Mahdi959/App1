from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class book(MDApp):
    def build(self):
        label = MDLabel(text = 'Hello World')
        return label

book().run()
