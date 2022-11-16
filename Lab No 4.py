from tkinter import *
from pygame import mixer
import string
import random

def key_generate(hex_input):
    """"генерирует случайный ключ из введенного шестнадцатеричного числа"""
    first_part = ''
    second_part = ''
    third_part = ''
    last_part = ''

    dec_num = str(int(hex_input, 16))
    if len(dec_num) < 5:
        dec_num = '0'*(5-len(dec_num))+dec_num

    options = string.ascii_uppercase+ string.digits

    first_part += f"{dec_num[0]}{''.join(random.choices(options, k=4))}"
    second_part += f"{dec_num[1]}{''.join(random.choices(options, k=4))}"
    third_part +=f"{dec_num[2]}{''.join(random.choices(options, k=4))}"
    last_part += dec_num[-2:]

    key = f"{first_part}-{second_part}-{third_part}-{last_part}"
    return key


#создать корневое окно
window = Tk()
window.title("Random Key Generator")
window.geometry('520x240')
window.resizable(False, False)

#определяет фоновое изображение
bg = PhotoImage(file='background.png')
my_label = Label(window, image=bg)
my_label.place(x=0, y=0)

#создает метку, поле ввода, отображение клавиш и кнопку "Старт"
Label(window, text="введите шестнадцатеричное число длиной в пять цифр:", font=("Arial", 15)).grid(row=0, column=2, columnspan=4)
Label(window, text="сгенерированный ключ:",font=("Arial", 12)).grid(row=12, column=2, columnspan=2)

entry = Entry(window,font=("Arial", 12))
entry.insert(0, '00000')
entry.grid(row=1, column=3, columnspan=2)

generated_key = Label(window, text = "XXXXX-XXXXX-XXXXX-XX", font=("Arial", 12))
generated_key.grid(row=12, column=4, columnspan=2)

def press():
    generated_key.config(text=key_generate(entry.get()))
b = Button(window,text = "старт", font=("Arial", 15), command=press)
b.grid(row=5, rowspan=2, column=3, columnspan=2)

#plays music
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()

window.mainloop()