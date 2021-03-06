import tkinter as tk
from ctypes import *


class Interface:
    def __init__(self, master):
        self.master = master  # инициализируем основное окно
        self.photo = tk.PhotoImage(file='logo.png')  # загрузка иконки приложения
        master.iconphoto(False, self.photo)  # установка иконки
        master.title('Задача Коши для ОДУ')  # заголовок
        master.configure(bg='#ececec')  # фон
        master.minsize(1110, 700)  # минимальный размер окна

        self.x0 = tk.DoubleVar(master, 1)  # x0
        self.u0 = tk.DoubleVar(master, 2)  # u0
        self.a1 = tk.DoubleVar(master, 12)  # a1
        self.a3 = tk.DoubleVar(master, 21)  # a3
        self.m = tk.DoubleVar(master, 123)  # m
        self.accuracy = tk.DoubleVar(master, 0.0001)  # точность выхода на границу
        self.error = tk.DoubleVar(master, 0.001)  # контроль лок. поргрешности
        self.max_step = tk.DoubleVar(master, 10000000)  # макс. число шагов
        self.step = tk.DoubleVar(master, 0.01)  # начальный шаг
        self.rb_var = tk.IntVar(master)  # хранит 0 или 1 (выход на границу x или u)
        self.rb_var.set(0)  # значение по умолчанию
        self.cb_var = tk.BooleanVar(master)  # хранит True или False (включен ли контроль погр-ти)
        self.cb_var.set(1)  # значение по умолчанию

        self.create_widgets()  # создание виджетов

    def create_widgets(self):
        # место для задачи (открытие по кнопке)
        exec_b = tk.Button(text='Задача', bg='#ececec', highlightbackground='#ececec', command=self.execute).grid(
            row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='we')

        # начальные условия
        cond_l = tk.Label(text='Начальные условия', bg='#ececec').grid(row=1, column=0, columnspan=2)
        cond_xl = tk.Label(text='x0', bg='#ececec').grid(row=2, column=0, padx=(10, 0), sticky='w')
        cond_xe = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.x0).grid(row=2, column=1, padx=(0, 10))
        cond_ul = tk.Label(text='u0', bg='#ececec').grid(row=3, column=0, padx=(10, 0), sticky='w')
        cond_ue = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.u0).grid(row=3, column=1, padx=(0, 10))
        cond_a1l = tk.Label(text='a1', bg='#ececec').grid(row=5, column=0, padx=(10, 0), sticky='w')
        cond_a1e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.a1).grid(row=5, column=1, padx=(0, 10))
        cond_a3l = tk.Label(text='a3', bg='#ececec').grid(row=6, column=0, padx=(10, 0), sticky='w')
        cond_a3e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.a3).grid(row=6, column=1, padx=(0, 10))
        cond_ml = tk.Label(text='m', bg='#ececec').grid(row=7, column=0, padx=(10, 0), sticky='w')
        cond_me = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.m).grid(row=7, column=1, padx=(0, 10))
        # кнопка Вычислить
        exec_b = tk.Button(text='Вычислить', bg='#ececec', highlightbackground='#ececec', command=self.execute).grid(
            row=8, column=0, columnspan=5, padx=10, pady=10, sticky='we')

        # параметры програмы
        accuracy_l = tk.Label(text='Точность выхода на границу', bg='#ececec').grid(row=0, column=2, padx=10,
                                                                                    pady=(10, 0), sticky='w')
        rb1 = tk.Radiobutton(text='x', variable=self.rb_var, value=0, bg='#ececec').grid(row=0, column=3, pady=(10, 0),
                                                                                         sticky='e')
        rb2 = tk.Radiobutton(text='u', variable=self.rb_var, value=1, bg='#ececec').grid(row=0, column=4, pady=(10, 0),
                                                                                         sticky='e')
        accuracy_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.accuracy).grid(row=1, column=2,
                                                                                              columnspan=3,
                                                                                              padx=(10, 0), sticky='we')
        error_cb = tk.Checkbutton(bg='#ececec', variable=self.cb_var).grid(row=2, column=3, columnspan=2)
        error_l = tk.Label(text='Контроль лок. погрешности', bg='#ececec').grid(row=2, column=2, padx=10, sticky='w')
        error_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.error).grid(row=3, column=2, columnspan=3,
                                                                                        padx=(10, 0), sticky='we')
        max_steps_l = tk.Label(text='Максимальное число шагов', bg='#ececec').grid(row=4, column=2, padx=10, sticky='w')
        max_steps_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.max_step).grid(row=5, column=2,
                                                                                               columnspan=3,
                                                                                               padx=(10, 0),
                                                                                               sticky='we')
        step_l = tk.Label(text='Начальный шаг', bg='#ececec').grid(row=6, column=2, padx=10, sticky='w')
        step_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.step).grid(row=7, column=2, columnspan=3,
                                                                                      padx=(10, 0), sticky='we')

        # справка (реализовать заполнение в функции execute)
        reference_l = tk.Label(text='Справка', bg='#ececec').grid(row=0, column=5, pady=10, sticky='we')
        reference_t = tk.Text(height=14, highlightbackground='#cbcbcb').grid(row=1, column=5, rowspan=7, padx=(10, 0),
                                                                             sticky='we')

        # таблица

        # график

    #  выполняется при нажатии кнопки "Вычислить"
    def execute(self):
        # записываем начальные условия задачи
        init_params = (c_double*7)()
        init_params[0] = self.x0.get()
        init_params[1] = self.u0.get()
        init_params[2] = self.step.get()
        init_params[3] = self.a1.get()
        init_params[4] = self.a3.get()
        init_params[5] = self.m.get()
        init_params[6] = self.max_step.get()
        # записываем параметры чм
        method_params = (c_double*2)()
        method_params[0] = self.accuracy.get()  # точность выхода на границу
        method_params[1] = self.error.get()  # контроль погрешности
        # записываем данные с кнопок (выбор границы / контроль лп)
        button_data = (c_int*2)()
        button_data[0] = self.rb_var.get()  # выбор границы 0 - x, 1 - u
        button_data[1] = self.cb_var.get()  # контроль ЛП True/False

root = tk.Tk()
gui = Interface(root)
root.mainloop()
