#!python2
# Tui Popenoe
# text_editor.py

import Tkinter
import tkMessageBox

def main():
    # Create root frame
    root = Tkinter.Tk()
    root.title('Text Editor 1.0')
    # Create Text Area
    text = Tkinter.Text(root)
    # Create root menu bar
    menu_bar = Tkinter.Menu(root)
    # Create the File Menu
    file_menu = Tkinter.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Open File', command=open_file)
    file_menu.add_command(label='Save File', command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=root.quit)
    menu_bar.add_cascade(label='File', menu=file_menu)
    # Create the Edit menu
    edit_menu = Tkinter.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label='Cut', command=cut_text)
    edit_menu.add_command(label='Copy', command=copy_text)
    edit_menu.add_command(label='Paste', command=paste_text)
    menu_bar.add_cascade(label='Edit', menu=edit_menu)
    # Create the help menu
    help_menu = Tkinter.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='About', command=display_help)
    menu_bar.add_cascade(label='Help', menu=help_menu)
    # Display the root menu bar
    root.config(menu=menu_bar)
    # Display the text area
    text.pack()
    root.mainloop()

def save_file():
    tkMessageBox.showinfo('Save File', 'Save File')

def open_file():
    tkMessageBox.showinfo('Open file', 'OpenFile')

def cut_text():
    tkMessageBox.showinfo('Cut Text', 'Cut Text')

def copy_text():
    tkMessageBox.showinfo('Copy Text', 'Copy Text')

def paste_text():
    tkMessageBox.showinfo('Paste Text', 'Paste Text')

def display_help():
    tkMessageBox.showinfo('Text Editor 1.0')

if __name__ == '__main__':
    main()
