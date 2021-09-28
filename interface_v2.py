import tkinter as tk
import table
from tkinter import ttk
#def get_data():

# initialize window
window = tk.Tk()  # инициализируем основное окно
window.title("Задача Коши для ОДУ")  # название программы
window.configure(bg='#ececec')  # задаем цвет фона
logo = tk.PhotoImage(file='logo.png')  # задаем иконку приложения
window.iconphoto(False, logo)
window.minsize(1220, 700)  # задаем минимальный размер окна
# task and conditions frame
task_l = tk.Label(text='Задача', bg='#ececec').grid(row=0, column=0, columnspan=2, sticky='sw', padx=10)
task_types = ['Тестовая', 'Реальная']
task_c = ttk.Combobox(values=task_types).grid(row=1, column=0, columnspan=2, sticky='news', padx=10)
method_l = tk.Label(text='Метод', bg='#ececec').grid(row=2, column=0, columnspan=2, sticky='sw', padx=10)
method_types = ['first', 'second']
method_c = ttk.Combobox(values=method_types).grid(row=3, column=0, columnspan=2, sticky='news', padx=10)
cond_l = tk.Label(text='Начальные условия', bg='#ececec').grid(row=4, column=0, columnspan=2, sticky='sw', padx=10)
rb_var = tk.IntVar()
rb1 = tk.Radiobutton(text='1', variable=rb_var, value=1, bg='#ececec').grid(row=5, column=0, sticky='nw', padx=10)
rb2 = tk.Radiobutton(text='-1', variable=rb_var, value=-1, bg='#ececec').grid(row=5, column=1, sticky='nw', padx=10)
exec_b = tk.Button(text='Вычислить', bg='#ececec', highlightbackground='#ececec').grid(row=6, column=0, columnspan=2,rowspan = 2, sticky='news',
                                                                                       padx=10, pady=10)
# input frame
accuracy_l = tk.Label(text='Точность выхода на границу', bg='#ececec').grid(row=0, column=2, sticky='ws', padx=10)
accuracy_e = tk.Entry(highlightbackground='#cbcbcb').grid(row=1, column=2, sticky='wen', padx=10)
error_l = tk.Label(text='Контроль лок. погрешности', bg='#ececec').grid(row=2, column=2, sticky='ws', padx=10)
error_e = tk.Entry(highlightbackground='#cbcbcb').grid(row=3, column=2, sticky='wen', padx=10)
max_steps_l = tk.Label(text='Максимальное число шагов', bg='#ececec').grid(row=4, column=2, sticky='ws', padx=10)
max_steps_e = tk.Entry(highlightbackground='#cbcbcb').grid(row=5, column=2, sticky='wen', padx=10)
step_l = tk.Label(text='Начальный шаг', bg='#ececec').grid(row=6, column=2, sticky='wn', padx=10)
step_e = tk.Entry(highlightbackground='#cbcbcb').grid(row=7, column=2, sticky='wen', padx=10)
# reference frame
reference_l = tk.Label(text='Справка', bg='#ececec').grid(row=0, padx=10, column=3)
reference_t = tk.Text(height=15, borderwidth=1, highlightbackground='#cbcbcb').grid(row=1, column=3, rowspan=7, padx=10)
# table frame
table_t = table.TestApp(window, filepath='example.csv').grid(row=8, column=0, columnspan=3, padx=10)
# graphic frame

window.mainloop()
