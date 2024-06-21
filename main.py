import os
try:
    from art import *
    from art import FONT_NAMES as all
except Exception as e:
    os.system("pip install art ")


class make_logo():
    def __init__(self):
        self.name = input("[ - ] Enter Your Name : ")
        print("_"*65)
        self.LoL(self.name)
        print("_"*65)

    def LoL(self, text):
        with open("Logo.txt", 'w', encoding='utf-8') as file:
            for font in all:
                Logo = text2art(text, font=font)
                file.write(f"{Logo}\n\n")
                print(Logo)


end = make_logo()
