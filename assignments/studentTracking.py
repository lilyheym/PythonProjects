import os
import tkinter
from tkinter import *
import sqlite3


class ParentWindow(Frame):
      def __init__ (self,master):
            Frame.__init__ (self)

            self.master = master
            self.master.resizable(width = False, height = False)
            self.master.geometry('{}x{}'.format(1000,1000))
            self.master.title('Learning Tkinter!')
            self.master.config(bg='lightgray')

            self.varFName = StringVar()
            self.varLName = StringVar()
            self.varPhone = StringVar()
            self.varEmail = StringVar()
            self.varCourse = StringVar()
         
            # labels for the stuff
            
            self.lblFName = Label(self.master,text = 'First Name: ', font = ("Helvectica", 16), fg = 'black', bg = 'lightgray' )
            self.lblFName.grid(row = 0, column = 1, padx =(27,0), pady =(30,0))

            self.lblLName = Label(self.master,text = 'Last Name: ', font = ("Helvectica", 16),fg = 'black', bg = 'lightgray' )
            self.lblLName.grid(row = 2, column = 1, padx = (27,0), pady = (10,0))

            self.lblPhone = Label(self.master,text = 'Phone: ', font = ("Helvectica", 16),fg = 'black', bg = 'lightgray' )
            self.lblPhone.grid(row = 4, column = 1, padx = (27,0), pady = (10,0))
            
            self.lblEmail = Label(self.master,text = 'Email: ', font = ("Helvectica", 16),fg = 'black', bg = 'lightgray' )
            self.lblEmail.grid(row = 6, column = 1, padx = (27,0), pady = (10,0))

            self.lblCourse = Label(self.master,text = 'Course: ', font = ("Helvectica", 16),fg = 'black', bg = 'lightgray' )
            self.lblCourse.grid(row = 8, column = 1, padx = (00,0), pady = (10,0))

            # display thing
            
            self.lblDisplay = Label(self.master,text = '', font = ("Helvectica", 16),fg = 'black', bg = 'lightgray' )
            self.lblDisplay.grid(row = 15, column = 1, padx =(30,0), pady = (30,0))

            # text entry boxes to put in the words
            
            self.txtFName = Entry(self.master, text = self.varFName, font = ("Helvetica", 16), fg = 'black', bg = 'white' )
            self.txtFName.grid(row=1, column=1, rowspan = 1, columnspan = 2, padx =(30,40), pady =(0,0))

            self.txtLName = Entry(self.master, text = self.varLName, font = ("Helvetica", 16), fg = 'black', bg = 'white' )
            self.txtLName.grid(row=3, column=1, padx = (30,40),  pady =(0,0))

            self.txtPhone = Entry(self.master, text = self.varPhone, font = ("Helvetica", 16), fg = 'black', bg = 'white' )
            self.txtPhone.grid(row=5, column=1, padx = (30,40),  pady =(0,0))

            self.txtEmail = Entry(self.master, text = self.varEmail, font = ("Helvetica", 16), fg = 'black', bg = 'white' )
            self.txtEmail.grid(row=7, column=1, padx = (30,40),  pady =(0,0))

            self.txtCourse = Entry(self.master, text = self.varCourse, font = ("Helvetica", 16), fg = 'black', bg = 'white' )
            self.txtCourse.grid(row=9, column=1, padx = (30,40),  pady =(0,0))


            
            # buttons
            
            self.btnSubmit = Button(self.master, text="Submit", width = 10, height = 2, command = self.submit)
            self.btnSubmit.grid(row = 11, column = 1, padx = (0,0), pady = (30,0), sticky = NE)

            self.btnCancel = Button(self.master, text="Cancel", width = 10, height = 2, command = self.cancel)
            self.btnCancel.grid(row = 11, column = 1, padx = (0,90), pady = (30,0), sticky = NE)

            


      def submit(self):
            fn = self.varFName.get()
            ln = self.varLName.get()
            self.lblDisplay.config(text = 'Hello {} {}!'.format(fn,ln))


      def cancel (self):
            self.master.destroy()

      
            


def create_db(self):
      conn = sqlite3.connect('studentTracking.db')
      with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_phonebook( \
                  ID IDENTIFIER PRIMARY KEY AUTOINCREMENT, \
                  col_fname TEXT, \
                  col_lname TEXT, \
                  col_phone TEXT, \
                  col_email TEXT, \
                  col_course TEXT \
                  );")
            # You must commit() to save changes and close the database connection
            conn.commit()
      conn.close()
      
            


      








if __name__ == "__main__":
      root = Tk()
      App = ParentWindow(root)
      root.mainloop()

