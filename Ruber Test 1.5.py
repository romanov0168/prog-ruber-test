import pandas as pd
import random as rnd
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ruber Test")
root.geometry("800x600")
root.resizable(width=False, height=False)
root.configure(background="black")
background_image = PhotoImage(file="76YM.gif")
background = Label(root, image=background_image, bd=0)
background.pack()
root.style = ttk.Style()
root.style.theme_use("vista")
s = ttk.Style()
s.configure('TButton', background='black', foreground='black', font=('Courier', '12'), relief=FLAT)
s.map('TButton', foreground=[('active', 'black')])
s.map('TButton', background=[('active', 'darkblue')])

rate_list = []
score = []
# r_answers = 0
# percent = 0
num_of_question = int(28)
rate = rnd.randint(1, num_of_question)

def finish():
    # percent = r_answers / num_of_question * 100
    # print(name.get() + ' ' + surname.get() + '\n' + str(score) + '\n' + str(percent)[:2] + '%')
    print(name.get() + ' ' + surname.get() + '\n' + str(score))
    f = open('PC №1.txt', 'w')
    # f.write(name.get() + ' ' + surname.get() + '\n' + str(score) + '\n' + str(percent)[:2] + '%')
    f.write(name.get() + ' ' + surname.get() + '\n' + str(score))
    root.destroy()

def destroy():
    question_label.place_forget()
    if question_type == "options":
        btn_var_1.place_forget()
        btn_var_2.place_forget()
        btn_var_3.place_forget()
        btn_var_4.place_forget()
    elif question_type == "enter":
        form_answer.place_forget()
        btn_give_answer.place_forget()
    if len(score) <= (num_of_question-1):
        question_choice()
    else:
        finish()

def validation_1():
    # global r_answers
    if str(a_1) == str(right_v):
        score.append(id + "+")
        # r_answers += 1
        destroy()
    else:
        score.append(id + "-")
        destroy()

def validation_2():
    # global r_answers
    if str(a_2) == str(right_v):
        score.append(id + "+")
        # r_answers += 1
        destroy()
    else:
        score.append(id + "-")
        destroy()

def validation_3():
    # global r_answers
    if str(a_3) == str(right_v):
        score.append(id + "+")
        # r_answers += 1
        destroy()
    else:
        score.append(id + "-")
        destroy()

def validation_4():
    # global r_answers
    if str(a_4) == str(right_v):
        score.append(id + "+")
        # r_answers += 1
        destroy()
    else:
        score.append(id + "-")
        destroy()

def test_answer():
    global right_v
    answer = enter_answer.get()
    answer = answer[:].lower()
    right_v = right_v[:].lower()
    if answer == right_v:
        score.append(id + "+")
        destroy()
    else:
        score.append(id + "-")
        destroy()

def enter_question():
    global form_answer
    global question_label
    global enter_answer
    global form_answer
    global btn_give_answer
    question_label = Label(root, text=question, bd=1, relief=SOLID, font='Courier 12')
    question_label.place(x=25, y=0, width=750)
    enter_answer = StringVar()
    form_answer = Entry(root, bd=1, relief=SOLID, textvariable=enter_answer, font='Courier 14')
    form_answer.place(x=300, y=275, width=200, height=50)
    btn_give_answer = ttk.Button(root, text="Принять", command = test_answer)
    btn_give_answer.place(x=300, y=350, width=200, height=50)

def option_question():
    global a_1
    global a_2
    global a_3
    global a_4
    global right_v
    global rate
    global btn_var_1
    global btn_var_2
    global btn_var_3
    global btn_var_4
    global question_label
    a_1 = fun['1'].iloc[0]
    a_2 = fun['2'].iloc[0]
    a_3 = fun['3'].iloc[0]
    a_4 = fun['4'].iloc[0]
    question_label = Label(root, text=question, bd=1, relief=SOLID, font='Courier 12')
    question_label.place(x=25, y=0, width=750)
    btn_var_1 = ttk.Button(root, text=a_1, command=validation_1)
    btn_var_1.place(x=25, y=450, width=350, height=50)
    btn_var_2 = ttk.Button(root, text=a_2, command=validation_2)
    btn_var_2.place(x=425, y=450, width=350, height=50)
    btn_var_3 = ttk.Button(root, text=a_3, command=validation_3)
    btn_var_3.place(x=25, y=525, width=350, height=50)
    btn_var_4 = ttk.Button(root, text=a_4, command=validation_4)
    btn_var_4.place(x=425, y=525, width=350, height=50)

def question_choice():
    global id
    global fun
    global question
    global right_v
    global question_type
    global rate
    if len(score) <= (num_of_question-1):
        while (rate in rate_list) == True:
            rate = rnd.randint(1,num_of_question)
        rate_list.append(rate)
        btn_start.place_forget()
        form_name.place_forget()
        form_surname.place_forget()
        form_name_label.place_forget()
        form_surname_label.place_forget()
        df = pd.read_csv('a_first3.csv', encoding='cp1251', sep='|')
        cur_df = df[df['rating'] == rate]
        count = int(cur_df['question'].count())
        if count == 0:
            count = 1
        r = rnd.randint(1, count)
        fun = cur_df[r - 1:r]
        question_type = fun['q_type'].iloc[0]
        question = fun['question'].iloc[0]
        id = str(fun['id'].iloc[0])  # Бывший question_slice2
        question = question.replace("~", "\n")
        right_v = fun['right_v'].iloc[0]
        if question_type == "options":
            option_question()
        elif question_type == "enter":
            enter_question()


def hello():
    global name
    global surname
    global form_name
    global form_surname
    global form_name_label
    global form_surname_label
    global btn_start
    name = StringVar()
    surname = StringVar()
    btn_go.place_forget()
    form_name_label = Label(root, text="Имя", font='Courier 14')
    form_name_label.place(x=200, y=200, width=100, height=50)
    form_surname_label = Label(root, text="Фамилия", font='Courier 14')
    form_surname_label.place(x=200, y=275, width=100, height=50)
    form_name = Entry(root, bd=1, relief=SOLID, textvariable=name, font='Courier 14')
    form_name.place(x=300, y=200, width=200, height=50)
    form_surname = Entry(root, bd=1, relief=SOLID, textvariable=surname, font='Courier 14')
    form_surname.place(x=300, y=275, width=200, height=50)
    btn_start = ttk.Button(root, text="Принять", command=question_choice)
    btn_start.place(x=300, y=350, width=200, height=50)

def intro():
    global btn_go
    btn_go = ttk.Button(root, text="Начать", command=hello)
    btn_go.place(x=300, y=275, width=200, height=50)

intro()
root.mainloop()
