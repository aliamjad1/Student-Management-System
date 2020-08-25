from sqlite3 import *
from Database import d
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# from Database import d

class Software:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment Software")
        self.root.state("zoomed")
        self.roolno_Entry_Var=StringVar()
        self.Name_Entry_Var=StringVar()
        self.Email_Entry_Var=StringVar()
        self.DOB_Entry_Var=StringVar()
        self.combo_Gender_Entry_Var=StringVar()
        self.Adrees_Entry_Var=StringVar()
        self.Contact_Entry_Var=StringVar()
        self.Search_Entry_Var=StringVar()
        self.combo_Search_Entry_Var=StringVar()
        #################  FRAMES  ##############
        Title=Label(root,text="Student Management System",fg="black",bd=10,relief=RIDGE,font=("verdana",40,"bold"),bg="cadet blue")
        Title.pack(side=TOP,fill=X)
        Managae_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#ffffcc")
        Managae_Frame.place(x=20,y=100,width=460,height=580)
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#ffffcc")
        Detail_Frame.place(x=490, y=100, width=855, height=580)
##############  Labels ##############################3
        Lbl_title_Manage=Label(Managae_Frame,text="Manage Students",fg="Dark blue",font=("times new roman",20,"bold"),bg="#ffffcc")
        Lbl_title_Manage.grid(row=0,column=0,pady=8)
        Lbl_RollNo_Manage = Label(Managae_Frame, text="Roll No:", fg="Dark blue",
                                 font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_RollNo_Manage.grid(row=1,column=0, pady=8,sticky="w")


        self.roolno_Entry=Entry(Managae_Frame,textvariable=self.roolno_Entry_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,width=23)
        self.roolno_Entry.grid(row=1,column=0,pady=8,padx=14)
        Lbl_Name_Manage = Label(Managae_Frame, text="Name:", fg="Dark blue",
                                 font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_Name_Manage.grid(row=2, column=0, pady=8, sticky="w")
        self.Name_Entry = Entry(Managae_Frame, textvariable=self.Name_Entry_Var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=23)
        self.Name_Entry.grid(row=2, column=0,  padx=14)
        Lbl_Email_Manage = Label(Managae_Frame, text="Email:", fg="Dark blue",
                                 font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_Email_Manage.grid(row=3, column=0, pady=8, sticky="w")
        self.Email_Entry = Entry(Managae_Frame,textvariable=self.Email_Entry_Var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=23)
        self.Email_Entry.grid(row=3, column=0, pady=8, padx=190)
        Lbl_Gender_Manage = Label(Managae_Frame, text="Gender:", fg="Dark blue",
                                 font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_Gender_Manage.grid(row=4, column=0,  sticky="w")
        self.combo_Gender_Entry=ttk.Combobox(Managae_Frame,textvariable=self.combo_Gender_Entry_Var,font=("times new roman",15,"bold"),width=22,state="readonly")
        self.combo_Gender_Entry["values"]=("Male","Female","Other")
        self.combo_Gender_Entry.grid(row=4,column=0,padx=10)
        Lbl_ContactNo_Manage = Label(Managae_Frame, text="Contact No:", fg="Dark blue",
                                 font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_ContactNo_Manage.grid(row=5, column=0,pady=8, sticky="w")
        self.Contact_Entry = Entry(Managae_Frame, textvariable=self.Contact_Entry_Var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=23)
        self.Contact_Entry.grid(row=5, column=0,  padx=10)
        Lbl_DOB_Manage = Label(Managae_Frame, text="D.O.B:", fg="Dark blue",
                                 font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_DOB_Manage.grid(row=6, column=0, pady=8, sticky="w")
        self.DOB_Entry = Entry(Managae_Frame, textvariable=self.DOB_Entry_Var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=23)
        self.DOB_Entry.grid(row=6, column=0, pady=8, padx=10)
        Lbl_ADDRESS_Manage = Label(Managae_Frame, text="Address:", fg="Dark blue",
                               font=("times new roman", 20, "bold"), bg="#ffffcc")
        Lbl_ADDRESS_Manage.grid(row=7, column=0, pady=8, sticky="w")
        self.Adrees_Entry = Entry(Managae_Frame, textvariable=self.Adrees_Entry_Var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=23)
        self.Adrees_Entry.grid(row=7, column=0, pady=8, padx=10)

        #########Buttons_FRame#########333

        Buttons_Frames_Manage=Frame(Managae_Frame,bd=14,bg="#ffff66",relief=RIDGE,width=100,height=50)
        Buttons_Frames_Manage.place(y=470)
        Button_Add_Manage=Button(Buttons_Frames_Manage,relief=GROOVE,fg="Black",text="Update Data",bd=9,width=10,height=3
                                 ,command=lambda:[self.update()
                                     # d.Data(Name_Entry.get(),self.Email_Entry.get(),roolno_Entry.get())
                                 ])
        Button_Add_Manage.grid(row=0)
        Button_Update_Manage = Button(Buttons_Frames_Manage, relief=GROOVE,text="Add Data", bd=9, width=10,height=3,command=lambda :[self.database(),self.reset(),
                                                                                                                                     messagebox.showinfo("Added","Your Data has been saved successfully!")])

        # self.AddData(self.roolno_Entry.get(),self.Name_Entry.get(),self.Email_Entry.get(),self.Adrees_Entry.get(),self.Contact_Entry.get()),self.reset()

        Button_Update_Manage.grid(row=0,column=2,padx=8)
        Button_Delete_Manage = Button(Buttons_Frames_Manage, relief=GROOVE,text="Delete Data", bd=9, width=10,height=3,command=lambda :self.deleteData(self.roolno_Entry.get()))

        Button_Delete_Manage.grid(row=0,column=3,padx=2)
        Button_Quit_Manage = Button(Buttons_Frames_Manage, relief=GROOVE,text="Show Data", bd=9, width=10,height=3,command=self.tree)
        Button_Quit_Manage.grid(row=0,column=4,padx=10)
        #######Detail FRAME###############


        lbl_Search_Deatil=Label(Detail_Frame,text="Search By",font=("times new roman",17,"bold"),bg="#ffffcc",fg="Dark Blue")
        lbl_Search_Deatil.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        self.combo_Search_Entry=ttk.Combobox(Detail_Frame,textvariable=self.combo_Search_Entry_Var,text="search",font=("times new roman",15,"bold"),width=15,state="readonly")
        self.combo_Search_Entry["values"]=("StdRollNo","StdName","StdEmail","StdGender")
        self.combo_Search_Entry.grid(row=0,column=1,padx=10)
        self.Search_Entry = Entry(Detail_Frame, textvariable=self.Search_Entry_Var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=15)
        self.Search_Entry.grid(row=0, column=2, pady=8, padx=10)
        lbl_Search_Deatil = Button(Detail_Frame,width=10, text="Search ", bd=5,relief=GROOVE,font=("times new roman", 15, "bold"), bg="white",
                                  fg="black",command=lambda :[self.tree_search()])
         #

        lbl_Search_Deatil.grid(row=0, column=3, pady=10, padx=10, sticky="w")
        lbl_Search_Deatil = Button(Detail_Frame,width=10, text="Show All ",bd=5,relief=GROOVE, font=("times new roman", 15, "bold"), bg="white",
                                  fg="black",command=lambda: [
                self.tree()
            ])
        lbl_Search_Deatil.grid(row=0, column=4, pady=10, padx=10, sticky="w")

        txt_Frame=Frame(Detail_Frame)
        txt_Frame.place(x=20,y=70,width=810,height=485)
        scroll = Scrollbar(txt_Frame, orient=VERTICAL)
        scroll_x = Scrollbar(txt_Frame, orient=HORIZONTAL)
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('times new roman', 15, 'bold'))  # Modify the font of the headings
        # style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        self.student_table=ttk.Treeview(txt_Frame,style="mystyle.Treeview",selectmode='browse',height=23,columns=("roll no","name","gender","email","D.O.B","address","contact"),yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll.config(command=self.student_table.yview)
        scroll_x.config(command=self.student_table.xview)
        self.student_table.heading("roll no",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("D.O.B",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("contact",text="Contact")
        self.student_table["show"]="headings"
        self.student_table.column("roll no",width=110,anchor='w')
        self.student_table.column("name",width=110)
        self.student_table.column("email",width=110)
        self.student_table.column("gender",width=110)
        self.student_table.column("D.O.B",width=110)
        self.student_table.column("address",width=110)
        self.student_table.column("contact",width=110)
        self.student_table.pack()
        # self.tree()
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.student_table.tag_configure('odd',background='#E8E8E8')
        self.student_table.tag_configure('even',background='#DFDFDF')


    def database(self):
        conn = connect("studentdatabase.db")
        cur = conn.cursor()
        # sql="CREATE TABLE studentdatabase12 (StdRollNo integer,StdName text,StdEmail text,StdGender text,StdDOB text,StdAddress text,StdContact integer)"
        # sql="INSERT INTO studentdatabase VALUES('" +str(StdName) + "'," + str(StdAge) + ")"
        # sql="""INSERT INTO studentdatabase (StdName, StdAge) VALUES ("testemail123", "gmail.com");"""
        # sql = "INSERT INTO studentdatabase (StdName, StdAge) VALUES('"+str(StdName) + "', " + str(StdAge)+")"
        # sql="INSERT INTO studentdatabase VALUES (%s,%s) ,('"+str(StdName) + "'," + str(StdAge)+")"
        # number = "Ali"
        # name = "GeeksforGeeks"
        # cur.execute(sql)
        cur.execute("INSERT INTO studentdatabase12 (StdRollNo, StdName,StdEmail,StdGender,StdDOB,StdAddress,StdContact) VALUES(?,?,?,?,?,?,?)",
                    (self.roolno_Entry_Var.get(), self.Name_Entry_Var.get(),self.Email_Entry_Var.get(),self.combo_Gender_Entry_Var.get(),self.DOB_Entry_Var.get(),self.Adrees_Entry_Var.get(),self.Contact_Entry_Var.get()))
        conn.commit()
        conn.close()


    def update(self):
        name=str(self.Name_Entry.get())
        email=str(self.Email_Entry.get())
        gender=str(self.combo_Gender_Entry.get())
        dob=str(self.DOB_Entry.get())
        aadress=str(self.Adrees_Entry.get())
        contact=str(self.Contact_Entry.get())
        roll=str(self.roolno_Entry.get())
        conn = connect("studentdatabase.db")
            # conn = connect("ali.dbms")
        cur = conn.cursor()
            # sql="""CREATE TABLE AliButt123456 (StdName text,Stdrollno integer, StdEmail integer,StdAddress integer,StdContact iteger )"""
        cur.execute("UPDATE  studentdatabase12 set StdName=?,StdEmail=?,StdGender=?,StdDOB=?,StdAddress=?,StdContact=? where StdRollNo=?",(name,email,
                                                                                                                                      gender,dob,aadress,contact,roll

        ))



        conn.commit()
        conn.close()


    def showdata(self):
        conn = connect("studentdatabase.db")

        cur = conn.cursor()
        sql = """SELECT * from studentdatabase12"""
        cur.execute(sql)
        x=cur.fetchall()
        conn.commit()
        conn.close()
        return x

    def tree(self):
        self.student_table.delete(*self.student_table.get_children())

        self.allrecieved=self.showdata()


        for eachreacord in self.allrecieved:


            self.student_table.insert('', END, values=(eachreacord))

        self.student_table.column("roll no",anchor="center")
        self.student_table.column("name",anchor="center")
        self.student_table.column("email",anchor="center")
        self.student_table.column("gender",anchor="center")
        self.student_table.column("D.O.B",anchor="center")
        self.student_table.column("address",anchor="center")
        self.student_table.column("contact",anchor="center")

    def reset(self):
        self.roolno_Entry_Var.set("")
        self.Name_Entry_Var.set("")
        self.Email_Entry_Var.set("")
        self.Adrees_Entry_Var.set("")
        self.Contact_Entry_Var.set("")
        self.DOB_Entry_Var.set("")
        self.combo_Gender_Entry.set("")
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']

        self.roolno_Entry_Var.set(row[0])
        self.Name_Entry_Var.set(row[1])
        self.Email_Entry_Var.set(row[2])
        self.combo_Gender_Entry_Var.set(row[3])
        self.DOB_Entry_Var.set(row[4])
        self.Adrees_Entry_Var.set(row[5])
        self.Contact_Entry_Var.set(row[6])
    def deleteData(self,delete):
        conn = connect("studentdatabase.db")

        cur = conn.cursor()
        sql = "DELETE FROM studentdatabase12 WHERE StdRollNo="+str(delete)
        cur.execute(sql)
        conn.commit()
        conn.close()
    def searchData(self):
        conn = connect("studentdatabase.db")

        cur = conn.cursor()
        sql = "SELECT * FROM studentdatabase12 WHERE "  + str(self.combo_Search_Entry.get())+" LIKE '%"+str(self.Search_Entry.get())+"%'"
        cur.execute(sql)
        x=cur.fetchall()

        conn.commit()
        conn.close()
        return x
    def tree_search(self):
        self.student_table.delete(*self.student_table.get_children())

        self.allrecieved = self.searchData()
        # self.student_table.insert('', END, values=self.allrecieved)
        # return self.allrecieved

        for eachreacord in self.allrecieved:
            # self.student_table.delete(x)
            self.student_table.insert('', END, values=(eachreacord))

        self.student_table.column("roll no", anchor="center")
        self.student_table.column("name", anchor="center")
        self.student_table.column("email", anchor="center")
        self.student_table.column("gender", anchor="center")
        self.student_table.column("D.O.B", anchor="center")
        self.student_table.column("address", anchor="center")
        self.student_table.column("contact", anchor="center")
    def searchDataByGender(self):
        conn = connect("studentdatabase.db")

        cur = conn.cursor()
        sql = "SELECT StdName FROM studentdatabase12 WHERE "  + str(self.Name_Entry.get())+" LIKE '%"+str(self.Search_Entry.get())+"%'"
        cur.execute(sql)
        x=cur.fetchall()

        conn.commit()
        conn.close()
        return x
    def SearchGender_search(self):
        self.student_table.delete(*self.student_table.get_children())

        self.allrecieved = self.searchDataByGender()


        for eachreacord in self.allrecieved:
            # self.student_table.delete(x)
            self.student_table.insert('', END, values=(eachreacord))

        self.student_table.column("roll no", anchor="center")
        self.student_table.column("name", anchor="center")
        self.student_table.column("email", anchor="center")
        self.student_table.column("gender", anchor="center")
        self.student_table.column("D.O.B", anchor="center")
        self.student_table.column("address", anchor="center")
        self.student_table.column("contact", anchor="center")
root=Tk()
s=Software(root)
root.mainloop()
























