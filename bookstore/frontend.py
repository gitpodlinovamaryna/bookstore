  # coding=<utf-8>

from tkinter import *
from backend import Database

database =Database("books.db")

class Window(object):
    def __init__(self,window):

        self.window=window

        self.window.wm_title("BookStore")

        label_title = Label(window, text = "Title")
        label_title.grid(row=0,column=0)
        label_year = Label(window, text="Year")
        label_year.grid(row=1,column=0)
        label_author = Label(window, text="Author")
        label_author.grid(row=0,column=2)
        label_isbn = Label(window, text="ISBN")
        label_isbn.grid(row=1,column=2)
        self.title_text =StringVar()
        self.entry_title = Entry(window, textvariable=self.title_text)
        self.entry_title.grid(row=0,column=1)
        self.year_text = StringVar()
        self.entry_year = Entry(window, textvariable=self.year_text)
        self.entry_year.grid(row=1,column=1)
        self.author_text=StringVar()
        self.entry_author =Entry(window,textvariable=self.author_text)
        self.entry_author.grid(row=0,column=3)
        self.isbn_text =StringVar()
        self.entry_isbn=Entry(window,textvariable=self.isbn_text)
        self.entry_isbn.grid(row=1,column=3)
        self.list1 = Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)
        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)
        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command=self.list1.yview)
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        b_view_all =Button(window, text="View all",width=12, command=self.view_command)
        b_view_all.grid(row=2,column=3)
        b_search_entry = Button(window, text="Search entry", width=12, command = self.search_command)
        b_search_entry.grid(row=3,column=3)
        b_add_entry = Button(window,text="Add entry",width =12, command = self.add_command)
        b_add_entry.grid(row=4,column=3)
        b_update = Button(window, text="Update",width=12, command=self.update_command)
        b_update.grid(row=5,column=3)
        b_delete =Button(window, text="Delete",width=12, command=self.delete_command)
        b_delete.grid(row=6,column=3)
        b_close= Button(window, text="Close",width=12, command=window.destroy)
        b_close.grid(row=7,column=3)


    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

    def get_selected_row(self,event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,self.selected_tuple[1])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,self.selected_tuple[2])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,self.selected_tuple[3])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def delete_command(self):
        database.delete(self.selected_tuple[0])


    def update_command(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())



window = Tk()
Window(window)
window.mainloop()
