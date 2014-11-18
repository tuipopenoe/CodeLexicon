#!python2
# Tui Popenoe
# text_editor.py

import Tkinter as Tk
import tkMessageBox
import tkFileDialog

class TextEditor(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_UI()
        self.text_buffer = ''

    def init_UI(self):
        self.parent.title('Text Editor 1.0')
        # Create Text Area
        self.text = Tk.Text(self.parent)
        # Create root menu bar
        menu_bar = Tk.Menu(self.parent)
        # Create the File Menu
        file_menu = Tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open File', command=self.open_file)
        file_menu.add_command(label='Save File', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.parent.quit)
        menu_bar.add_cascade(label='File', menu=file_menu)
        # Create the Edit menu
        edit_menu = Tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label='Cut', command=self.cut_text)
        edit_menu.add_command(label='Copy', command=self.copy_text)
        edit_menu.add_command(label='Paste', command=self.paste_text)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)
        # Create the help menu
        help_menu = Tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='About', command=self.display_help)
        menu_bar.add_cascade(label='Help', menu=help_menu)
        self.text.pack()
        self.parent.config(menu=menu_bar)

    def save_file(self):
        f = tkFileDialog.asksaveasfile(mode='w',
                                          defaultextension='.txt')
        if f is None:
            return
        file_text = str(self.text.get(1.0, Tk.END))
        f.write(file_text)
        f.close()


    def open_file(self):
        ftypes = [('Python files', '*.py'), ('All Files', '*')]
        dialog = tkFileDialog.Open(self, filetypes=ftypes)
        fl = dialog.show()
        if fl != '':
            file_text = self.read_file(fl)
            self.text.insert(Tk.END, file_text)

    def read_file(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
            return text

    def cut_text(self):
        tkMessageBox.showinfo('Cut Text', 'Cut Text')

    def copy_text(self):
        self.text_buffer = self.text.get("sel.first", "sel.last")

    def paste_text(self):
        self.text.insert("sel.first", self.text_buffer)

    def display_help(self):
        tkMessageBox.showinfo('Text Editor 1.0')


def main():
    # Create root frame
    root = Tk.Tk()
    text_editor = TextEditor(root)
    # Set Editor geometry to main window + buffer on sides
    root.geometry('1280x720')
    root.mainloop()

if __name__ == '__main__':
    main()
