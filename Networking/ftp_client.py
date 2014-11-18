#!python2
# Tui Popenoe
# ftp_client.py

import Tkinter as Tk
import tkFileDialog
import paramiko

class FTPClient(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_UI()

    def init_UI(self):
        self.parent.title('FTP Client 1.0')
        #File Editor Frame

        # Create root menu
        menu_bar = Tk.Menu(self.parent)
        # Create file menu
        file_menu = Tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open Connection',
                              command=self.open_connection)
        file_menu.add_command(label='Refresh', command=self.refresh)
        menu_bar.add_cascade(label='File', menu=file_menu)
        self.parent.config(menu=menu_bar)

    def open_connection(self):
        print('Open COnnection')

    def refresh(self):
        print('Refresh')

def main():
    # Create root Frame
    root = Tk.Tk()
    ftp_client = FTPClient(root)
    root.mainloop()

if __name__ == '__main__':
    main()