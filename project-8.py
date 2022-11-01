import os
from os import system
from tkinter import Y
system("clear")
import datetime

tday = datetime.date.today()
print(tday)

bday= datetime.date(2023, 4, 29)
gday=datetime.date(2023, 5, 19)
fb=datetime.date(2022, 11, 19)
wb=datetime.date(2022, 12, 17)

till_bday= bday - tday
till_gday= gday - tday
till_fb= fb - tday
till_wb= wb -tday

till_bday= str(till_bday)
till_gday=str(till_gday)
till_fb= str(till_fb)
till_wb= str(till_wb)

print(" There are " + till_bday + " days till your bday")
print(" There are " + till_gday + " days till your gday")
print(" There are " + till_fb + " days till your fall break")
print(" There are " + till_wb + " days till your winter break")
