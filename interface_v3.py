import tkinter as tk

class Interface:
    def __init__(self, master):
        self.master = master
        self.photo = tk.PhotoImage(file='logo.png')
        master.iconphoto(False, self.photo)
        master.title('Задача Коши для ОДУ')
        master.configure(bg='#ececec')
        master.minsize(1110, 700)
        self.x0 = tk.StringVar(master, '1')
        self.u0 = tk.StringVar(master, '2')
        self.accuracy = tk.StringVar(master, '0.00000001')
        self.error = tk.StringVar(master, '0.0001')
        self.max_step = tk.StringVar(master, '10000000')
        self.step = tk.StringVar(master, '0.01')
        self.rb_var = tk.IntVar(master)
        self.rb_var.set(0)
        self.cb_var = tk.BooleanVar(master)
        self.cb_var.set(1)
        self.create_widgets()

    def create_widgets(self):
        task_l = tk.Label(text='место место место\nдля для для\nзадачи задачи задачи\nура ура ура', bg='#ececec').grid(
            row=0, column=0, columnspan=2, rowspan=4, padx=(10, 0), pady=(10, 0))
        cond_l = tk.Label(text='Начальные условия', bg='#ececec').grid(row=4, column=0, columnspan=2)
        cond_xl = tk.Label(text='x0', bg='#ececec').grid(row=5, column=0, padx=(10, 0), sticky='w')
        cond_xe = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.x0).grid(row=5, column=1, padx=(0, 10))
        cond_ul = tk.Label(text='u0', bg='#ececec').grid(row=6, column=0, padx=(10, 0), sticky='w')
        cond_ue = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.u0).grid(row=6, column=1, padx=(0, 10))
        exec_b = tk.Button(text='Вычислить', bg='#ececec', highlightbackground='#ececec', command=self.execute).grid(
            row=8, column=0, columnspan=2, padx=10, sticky='we')
        accuracy_l = tk.Label(text='Точность выхода на границу', bg='#ececec').grid(row=0, column=2, padx=10,
                                                                                    pady=(10, 0), sticky='w')
        rb1 = tk.Radiobutton(text='x', variable=self.rb_var, value=0, bg='#ececec').grid(row=0, column=3, pady=(10, 0),
                                                                                         sticky='e')
        rb2 = tk.Radiobutton(text='u', variable=self.rb_var, value=1, bg='#ececec').grid(row=0, column=4, pady=(10, 0),
                                                                                         sticky='e')
        accuracy_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.accuracy).grid(row=2, column=2,
                                                                                              columnspan=3,
                                                                                              padx=(10, 0), sticky='we')
        error_cb = tk.Checkbutton(bg='#ececec', variable=self.cb_var).grid(row=3, column=3, columnspan=2)
        error_l = tk.Label(text='Контроль лок. погрешности', bg='#ececec').grid(row=3, column=2, padx=10, sticky='w')
        error_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.error).grid(row=4, column=2, columnspan=3,
                                                                                        padx=(10, 0), sticky='we')
        max_steps_l = tk.Label(text='Максимальное число шагов', bg='#ececec').grid(row=5, column=2, padx=10, sticky='w')
        max_steps_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.max_step).grid(row=6, column=2,
                                                                                               columnspan=3,
                                                                                               padx=(10, 0),
                                                                                               sticky='we')
        step_l = tk.Label(text='Начальный шаг', bg='#ececec').grid(row=7, column=2, padx=10, sticky='w')
        step_e = tk.Entry(highlightbackground='#cbcbcb', textvariable=self.step).grid(row=8, column=2, columnspan=3,
                                                                                      padx=(10, 0), sticky='we')
        # reference frame
        reference_l = tk.Label(text='Справка', bg='#ececec').grid(row=0, column=5, pady=10, sticky='we')
        reference_t = tk.Text(height=14, highlightbackground='#cbcbcb').grid(row=1, column=5, rowspan=9, padx=(10, 0),
                                                                             sticky='we')

    def execute(self):
        data = [
            self.x0.get(), self.u0.get(), self.accuracy.get(), self.error.get(), self.max_step.get(), self.step.get(),
            self.rb_var.get(), self.cb_var.get()]
        print(data)


root = tk.Tk()
gui = Interface(root)
root.mainloop()
