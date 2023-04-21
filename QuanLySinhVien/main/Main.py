from tkinter import *
import tkinter.messagebox as mbox
from tkinter.ttk import Combobox
import mysql.connector
#  Connect database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="trongtu.vn"
)

#  Tạo label thông tin
form_sv = Tk()
form_sv.geometry("350x300")
title = Label(form_sv, text="Thông tin sinh viên", fg="blue", font=("Arial", 20)).place(x=60, y=10)
maSV = Label(form_sv, text="Mã SV: ", font=("Arial", 10)).place(x=30, y=50)
fullname = Label(form_sv, text="Họ và tên: ", font=("Arial", 10)).place(x=30, y=90)
email = Label(form_sv, text="Email: ", font=("Arial", 10)).place(x=30, y=130)
gender = Label(form_sv, text="Giới tính: ", font=("Arial", 10)).place(x=30, y=170)
lop = Label(form_sv, text="Lớp: ", font=("Arial", 10)).place(x=30, y=210)

# Tạo ô nhập má sinh viên
sv1 = Entry(form_sv)
sv1.place(x=100, y=50, width=200)
sv1.focus()

# Tạo ô nhập họ và tên
sv2 = Entry(form_sv)
sv2.place(x=100, y=90, width=200)
sv2.focus()

# Tạp ô nhập email
sv3 = Entry(form_sv)
sv3.place(x=100, y=130, width=200)
sv3.focus()

# Tạo option chọn giới tính
sv4 = Combobox(form_sv)
sv4['values'] = ("--Chọn--", "Nam", "Nữ")
sv4.place(x=100, y=170, width=70)
sv4.current(0)
sv4.focus()

# Tạo ô nhâp lớp
sv5 = Entry(form_sv)
sv5.place(x=100, y=210, width=200)
sv5.focus()

# Cử lý dữ liệu và thêm vào database
def add_pupil():
    maSV=int(sv1.get())
    fullname=sv2.get()
    email=sv3.get()
    gender=sv4.get()
    lop=sv5.get()
    print(gender)
    mycursor = mydb.cursor()
    sql = "INSERT INTO `tbl_users` (MaSV, fullname, email, gender, lop)     VALUES (%s, %s ,%s, %s, %s)"
    val = [maSV, fullname, email, gender, lop]
    mycursor.execute(sql, val)
    mydb.commit()
    mbox.showinfo("Thông báo", "Thêm sinh viên thành công")

# Tạo nút submit dữ liệu
submit = Button(form_sv, text = "Thêm sinh viên", fg="red" , font=("Arial", 10), command= add_pupil).place(x=140, y=250)
form_sv.mainloop()
