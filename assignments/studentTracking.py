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

            self.btnDelete = Button(self,master, text = "Delete", width = 10, height = 2, command = self.delete)
            self.btnDelete.grid(row = 13, column = 1, padx = (0,0), pady = (30,0), sticky = NE)

         

            


      def submit(self):
            conn = sqlite3.connect('students.db')
            with conn:
                  cursor = conn.cursor()
                  cursor.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_phone, col_email, col_course) VALUES (?,?,?,?,?);""",  )
                  onClear(self)
            conn.commit()
            conn.close()


      def onClear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_phone.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_course.delete(0,END)

            def onDeleted(self):
                 
                  self.txt_fname.delete(0,END)
                  self.txt_lname.delete(0,END)
                  self.txt_phone.delete(0,END)
                  self.txt_email.delete(0,END)
                  self.txt_course.delete(0,END)


      def delete(self):
            conn = sqlite3.connect('students.db')
            with conn:
                  cur = con.cursor()
                  count = cur.execute("""SELECT COUNT(*) FROM tbl_students""")
                  count = cur.fetchone()[0]
                  if count > 1:
                        confirm = messagebox.askokcancel("Delete Confirmation", "All information will be permenantly deleted from the database. \n\nProceed with the deletion request?")
                        if confirm:
                              con = sqlite3.connect('students.db')
                              with conn:
                                    cursor = conn.cursor()
                                    cursor.execute("""DELETE FROM tbl_students WHERE col_fname  = '{}' AND col_lname = '{}'""".format(varFname,varLName))
                              onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
      #####                   onRefresh(self)  # update the listbox of the changes
                              conn.commit()
                  else:
                        confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time.   \n\nPlease add another record first before you can delete ({}).".format(var_select, var_select))
            conn.close()

            
                  


      def cancel (self):
            self.master.destroy()

      
            


conn = sqlite3.connect('students.db')
with conn:
      cur = conn.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS tbl_students (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fname TEXT, col_lname TEXT, col_phone TEXT, col_email TEXT, col_course TEXT);")
                            
      conn.commit()
      
                              




      








if __name__ == "__main__":
      root = Tk()
      App = ParentWindow(root)
      root.mainloop()

