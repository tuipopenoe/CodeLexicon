#!python2
# Tui Popenoe
# Code Lexicon - Guestbook

import Tkinter as Tk

class Guestbook(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()
        self.labels = []

    def init_ui(self):
        self.parent.title('Guestbook 1.0')
        self.entry = Tk.Entry(self.parent, bd=1, width=30)
        self.entry.pack()
        self.add_comment = Tk.Button(self.parent,
                                     text='Add Comment',
                                     command=self.create_label)
        self.add_comment.pack(side=Tk.BOTTOM, anchor=Tk.SW)

    def create_label(self):
        text_string = self.entry.get()
        label = Tk.Label(self.parent, text=text_string)
        label.pack()

def main():
    root = Tk.Tk()
    guestbook = Guestbook(root)
    guestbook.mainloop()

if __name__ == '__main__':
    main()
