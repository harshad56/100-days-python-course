from tkinter import *
from tkinter import messagebox
import random
from time import sleep
from threading import Thread
words = "is was are be have had were can said use do will would make like has " \
        "look write go see could been call am find did get come made may take know" \
        " live give think say help tell follow came want show set put does must ask went" \
        " read need move try change play spell found study learn should add keep start " \
        "thought saw turn might close seem open begin got run walk began grow took carry " \
        "hear stop miss eat watch let cut talk being leave word time number way people water day" \
        " part sound work place year back thing name sentence man line boy farm end men land home" \
        " hand picture air animal house page letter point mother answer America world food country plant" \
        " school father tree city earth eye head story example life paper group children side feet car " \
        "mile night sea river state book idea face Indian girl mountain list song family"

words_list = words.split(" ")

screen = Tk()
screen.config(padx=80, pady=80)
time = 60
score = 0


def chance_word(x):
    global print_list, time, score
    if time == 60:
        Thread(target=timer).start()
    if time < 0:
        mesage = messagebox.showinfo(title="Test is finished.", message=f"Your score is {score} words per minute."
                                                                        f"You wrote {score/60} words per second.")

    elif word_entry.get().replace(" ", "") == print_list[0]:
        print_list.remove(print_list[0])
        print_list.append(random.choice(words_list))
        word_label.config(text=" ".join(print_list))
        word_entry.delete(first=0, last='end')
        word_entry.bind(print_list[0], func=chance_word)
        score += 1
        score_label["text"] = score


def timer():
    global time
    time -= 1
    while time > -1:
        sleep(1)
        timer_label["text"] = time
        time -= 1


print_list = [random.choice(words_list) for i in range(5)]

timer_label = Label(text="60", fg="RED", font=("Times", 20, "bold"))
timer_label.grid(row=0, column=0)

word_label = Label(text=" ".join(print_list), font=("Times", 20, "bold"))
word_label.grid(row=1, column=0)


word_entry = Entry(width=30, font=("Calibra", 15))
word_entry.grid(row=3, column=0, columnspan=3, pady=15)
word_entry.bind("<space>", func=chance_word)

score_label = Label(text=f"{score} ", font=("Times", 25), pady=0, fg="Blue")
score_label.grid(row=4, column=0)

score_label1 = Label(text="Words written", font=("Times", 15))
score_label1.grid()

info_label = Label(
    text="You can start by writing first word and spacing.", pady=20)
info_label.grid()

screen.mainloop()
