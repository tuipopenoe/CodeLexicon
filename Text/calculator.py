#!python2
# Tui Popenoe
# calculator.py

import Tkinter as Tk
from ttk import Style

class Calculator(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_UI()

    def init_UI(self):
        self.parent.title('Calculator 1.0')
        # Configure Grid layout
        Style().configure('TButton', font='serif 10')
        for i in range(5):
            self.columnconfigure(i, pad=3)
        for i in range(6):
            self.rowconfigure(i, pad=3)

        # Create the calculator display
        display = Tk.Entry(self.parent)
        display.grid(row=0, column=0, columnspan=5, sticky=Tk.W+Tk.E)
        # Create root menu
        menu_bar = Tk.Menu(self.parent)
        # Create the View menu
        view_menu = Tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label='Standard', command=self.standard_view)
        menu_bar.add_cascade(label='View', menu=view_menu)
        # Create Edit menu
        edit_menu = Tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label='Copy', command=self.copy_text)
        edit_menu.add_command(label='Paste', command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label='History', command=self.view_history)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)
        # Create Help Menu
        help_menu = Tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='View Help', command=self.display_help)
        help_menu.add_separator()
        help_menu.add_command(label='About', command=self.display_about)

        # Calculator Buttons
        # Row 1
        button_back = Tk.Button(self.parent, text='<-', command=self.back)
        button_back.grid(row=1, column=0, columnspan=1, sticky=Tk.W+Tk.E)
        button_clear = Tk.Button(self.parent, text='C', command=self.clear)
        button_clear.grid(row=1, column=1, columnspan=2, sticky=Tk.W+Tk.E)
        button_negate = Tk.Button(self.parent, text='+-', command=self.negate)
        button_negate.grid(row=1, column=3, columnspan=1)
        button_sqrt = Tk.Button(self.parent, text='sqrt', command=self.sqrt)
        button_sqrt.grid(row=1, column=4, columnspan=1, sticky=Tk.W+Tk.E)
        # Row 2
        button_seven = Tk.Button(self.parent, text='7', command=self.push_seven)
        button_seven.grid(row=2, column=0, columnspan=1, sticky=Tk.W+Tk.E)
        button_eight = Tk.Button(self.parent, text='8', command=self.push_eight)
        button_eight.grid(row=2, column=1, columnspan=1, sticky=Tk.W+Tk.E)
        button_nine = Tk.Button(self.parent, text='9', command=self.push_nine)
        button_nine.grid(row=2, column=2, columnspan=1, sticky=Tk.W+Tk.E)
        button_divide = Tk.Button(self.parent, text='/', command=self.divide)
        button_divide.grid(row=2, column=3, columnspan=1, sticky=Tk.W+Tk.E)
        button_mod = Tk.Button(self.parent, text='%', command=self.mod)
        button_mod.grid(row=2, column=4, columnspan=1, sticky=Tk.W+Tk.E)
        # Row 3
        button_four = Tk.Button(self.parent, text='4', command=self.push_four)
        button_four.grid(row=3, column=0, columnspan=1, sticky=Tk.W+Tk.E)
        button_five = Tk.Button(self.parent, text='5', command=self.push_five)
        button_five.grid(row=3, column=1, columnspan=1, sticky=Tk.W+Tk.E)
        button_six = Tk.Button(self.parent, text='6', command=self.push_six)
        button_six.grid(row=3, column=2, columnspan=1, sticky=Tk.W+Tk.E)
        button_multiply = Tk.Button(self.parent, text='*', command=self.mult)
        button_multiply.grid(row=3, column=3, columnspan=1, sticky=Tk.W+Tk.E)
        button_invert = Tk.Button(self.parent, text='1/x', command=self.invert)
        button_invert.grid(row=3, column=4, columnspan=1, sticky=Tk.W+Tk.E)
        # Row 4
        button_one = Tk.Button(self.parent, text='1', command=self.push_one)
        button_one.grid(row=4, column=0, columnspan=1, sticky=Tk.W+Tk.E)
        button_two = Tk.Button(self.parent, text='2', command=self.push_two)
        button_two.grid(row=4, column=1, columnspan=1, sticky=Tk.W+Tk.E)
        button_three = Tk.Button(self.parent, text='3', command=self.push_three)
        button_three.grid(row=4, column=2, columnspan=1, sticky=Tk.W+Tk.E)
        button_minus = Tk.Button(self.parent, text='-', command=self.minus)
        button_minus.grid(row=4, column=3, columnspan=1, sticky=Tk.W+Tk.E)
        button_equals = Tk.Button(self.parent, text='=', command=self.equals)
        button_equals.grid(row=4, column=4, rowspan=2,
                           sticky=Tk.W+Tk.E+Tk.N+Tk.S)
        # Row 5
        button_zero = Tk.Button(self.parent, text='0', command=self.push_zero)
        button_zero.grid(row=5, column=0, columnspan=2, sticky=Tk.W+Tk.E)
        button_point = Tk.Button(self.parent, text='.', command=self.point)
        button_point.grid(row=5, column=2, columnspan=1, sticky=Tk.W+Tk.E)
        button_plus = Tk.Button(self.parent, text='+', command=self.add)
        button_plus.grid(row=5, column=3, columnspan=1, sticky=Tk.W+Tk.E)

        self.parent.config(menu=menu_bar)

    # Non Number functions
    def back(self):
        print('Back')

    def clear(self):
        print('Clear')

    def negate(self):
        print('Invert')

    def sqrt(self):
        print('Square Root')

    def divide(self):
        print('Divide')

    def mod(self):
        print('Mod')

    def mult(self):
        print('Multiply')

    def invert(self):
        print('Invert')

    def minus(self):
        print('Minus')

    def equals(self):
        print('Equals')

    def point(self):
        print('Point')

    def add(self):
        print('Add')

    # Menu Functions
    def standard_view(self):
        print('Standard View')

    def copy_text(self):
        print('Copy Text')

    def paste_text(self):
        print('Paste Text')

    def view_history(self):
        print('View History')

    def display_help(self):
        print('Display Help')

    def display_about(self):
        print('Display About')

    # Button Functions
    def push_seven(self):
        print('Push Seven')

    def push_eight(self):
        print('Push Eight')

    def push_nine(self):
        print('Push Nine')

    def push_four(self):
        print('Push Four')

    def push_five(self):
        print('Push Five')

    def push_six(self):
        print('Push Six')

    def push_one(self):
        print('Push One')

    def push_two(self):
        print('Push Two')

    def push_three(self):
        print('Push Three')

    def push_zero(self):
        print('Push Zero')


def main():
    # Create root Frame
    root = Tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()