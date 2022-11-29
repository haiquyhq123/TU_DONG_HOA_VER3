#import modules
from pathlib import Path
from tkinter import *
from tkinter import ttk
import os
import subprocess
from PIL import *
import PIL.Image
from PIL import ImageTk
import tkinter.messagebox as mbox
import time
import pyautogui as au
import pyautogui, sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/haiquy/OnlineJudgeDeploy/build2/assets/frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups and new pop up window

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    def lenh():
        mbox.askyesnocancel(title="XAC NHAN LAI",message="BAN CO MUON TIEP TUC")
        au.hotkey('ctrl', 'alt', 't')
        au.moveTo(355,218,2)
        au.click()
        au.write('sudo lsof -i tcp:80',interval=1)
        au.press("enter")
        au.click()
        au.write("hq07092005",interval=0.25)
        au.press("enter")
        au.click()
        au.write("sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill",interval=1)
        au.press("enter")
        au.write("sudo -i",interval=0.25)
        au.press("enter")
        au.write("cd ..",interval=0.25)
        au.press("enter")
        au.write("cd home",interval=0.25)
        au.press("enter")
        au.write("cd haiquy",interval=0.25)
        au.press("enter")
        au.write("cd OnlineJudgeDeploy",interval=0.25)
        au.press("enter")
        au.write("apt install docker.io docker-compose",interval=0.25)
        au.press("enter")
        au.write("docker-compose up -d")
        au.press("enter")
    def lenh2():
        mbox.askyesnocancel(title="XAC NHAN LAI",message="BAN CO MUON TIEP TUC")
        au.hotkey('ctrl', 'alt', 't')
        au.moveTo(355,218,2)
        au.click()
        au.write('git clone https://github.com/Greenhat1998/OnlineJudgeDeploy',interval=1.25)
        au.press("enter")
    def lenh3():
        os.system("gnome-terminal -e 'bash -c \"sudo apt install net-tools; exec bash\"'"),
        mbox.askyesnocancel(title="XAC NHAN LAI",message="BAN CO MUON TIEP TUC")
        au.hotkey('ctrl', 'alt', 't')
        au.moveTo(355,218,2)
        au.write("sudo -i",interval=0.25)
        au.press("enter")
        au.write("hq07092005")
        au.press("enter")
        au.write("cd ..",interval=0.25)
        au.press("enter")
        au.write("cd home",interval=0.25)
        au.press("enter")
        au.write("cd haiquy",interval=0.25)
        au.press("enter")
        au.write("cd OnlineJudgeDeploy",interval=0.25)
        au.press("enter")
        au.write("ifconfig",interval=0.25)
        au.press("enter")
    def lenh4():
        hq1=Toplevel()
        hq1.geometry("200x200")
        def get_value_2():
            hq=Toplevel()
            hq.geometry("200x200")
            def cj():
                hq.destroy()
            Label(hq,text="tinh nang dang thu nghiem").pack()
            Button(hq,text="thoat",command=cj).pack()
        def cj():
            hq1.destroy()

        hq1=Toplevel()
        hq1.title("TINH NANG")
        frame2 = Frame(hq1,highlightthickness=2,highlightbackground="black")
        Label(frame2, text="Tinh nang:").grid(row=0)
        var1 = IntVar()
        Checkbutton(frame2, text="Cham bai", variable=var1).grid(row=1,column=0,padx=20)
        var2 = IntVar()
        Checkbutton(frame2, text="User", variable=var2).grid(row=1,column=1)
        var3 = IntVar()
        Checkbutton(frame2, text="Toan", variable=var3,command=get_value_2).grid(row=2,column=0)
        var4 = IntVar()
        Checkbutton(frame2, text="Tin", variable=var4).grid(row=2,column=1)
        btn = Button(frame2, text = 'xac nhan',command=cj).grid(row=5,sticky=E)
        var5 =IntVar()
        Checkbutton(frame2, text="BXH", variable=var5).grid(row=1,column=2)
        var6 =IntVar()
        Checkbutton(frame2, text="PYTHON", variable=var6).grid(row=2,column=2)
        var7 =IntVar()
        Checkbutton(frame2, text="C++", variable=var7).grid(row=1,column=3)
        var8 =IntVar()
        Checkbutton(frame2, text="JAVA", variable=var8,).grid(row=2,column=3)
        frame2.pack()
        Button(hq1,Text="Thoat",command= cj).pack()

        
    
    
    def hq():
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"/home/haiquy/OnlineJudgeDeploy/build3/assets/frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        window_2 = Toplevel()

        window_2.geometry("350x550")
        window_2.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window_2,
            bg = "#FFFFFF",
            height = 550,
            width = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            92.0,
            314.0,
            anchor="nw",
            text="TRÌNH CÀI ĐẶT Sever",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        canvas.create_rectangle(
            -2.0,
            28.0,
            349.9998779296875,
            31.044769287109375,
            fill="#000000",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            window_2,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lenh4,
            relief="flat"
        )
        button_1.place(
            x=129.0,
            y=49.0,
            width=72.0,
            height=33.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            window_2,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: os.system("gnome-terminal -e 'bash -c \"sudo apt update; exec bash\"'"),
            relief="flat"
        )
        button_2.place(
            x=3.0,
            y=137.0,
            width=108.0,
            height=28.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            window_2,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: os.system("gnome-terminal -e 'bash -c \"sudo apt -y upgrade; exec bash\"'"),
            relief="flat"
        )
        button_3.place(
            x=121.0,
            y=137.0,
            width=103.0,
            height=28.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            window_2,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: os.system("gnome-terminal -e 'bash -c \"sudo apt install git curl python3-pip; exec bash\"'"),
            relief="flat"
        )
        button_4.place(
            x=234.0,
            y=137.0,
            width=112.0,
            height=27.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            window_2,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: os.system("gnome-terminal -e 'bash -c \"pip install docker-compose; exec bash\"'"),
            relief="flat"
        )
        button_5.place(
            x=234.0,
            y=171.0,
            width=112.0,
            height=27.0
        )


        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            window_2,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lenh2,
            relief="flat"
        )
        button_8.place(
            x=6.0,
            y=279.0,
            width=112.0,
            height=27.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            window_2,
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lenh,
            relief="flat"
        )
        button_9.place(
            x=126.0,
            y=279.0,
            width=112.0,
            height=27.0
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            window_2,
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lenh3,
            relief="flat"
        )
        button_10.place(
            x=244.0,
            y=279.0,
            width=92.0,
            height=27.0
        )

        button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_11 = Button(
            window_2,
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: os.system("gnome-terminal -e 'bash -c \"sudo curl -sSL https://get.daocloud.io/docker/ | sh; exec bash\"'"),
            relief="flat"
        )
        button_11.place(
            x=124.0,
            y=172.0,
            width=100.3611068725586,
            height=26.0
        )


        canvas.create_rectangle(
            -2.0,
            98.0,
            350.0,
            100.0,
            fill="#000000",
            outline="")

        canvas.create_text(
            78.0,
            6.0,
            anchor="nw",
            text="TRÌNH CÀI ĐẶT TRANG WEB",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        canvas.create_rectangle(
            -2.0,
            128.0,
            350.0,
            130.0,
            fill="#000000",
            outline="")

        canvas.create_text(
            111.0,
            108.0,
            anchor="nw",
            text="ROAD MAP CÀI ĐẶT",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        canvas.create_rectangle(
            -2.0,
            273.0,
            350.0,
            275.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            -2.0,
            308.0,
            350.0,
            310.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            10.0,
            306.0,
            13.034194946289062,
            549.9998474121094,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            334.0,
            306.0,
            336.0,
            550.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            12.0,
            336.0,
            337.0,
            339.0,
            fill="#000000",
            outline="")
        window_2.resizable(False, False)
        window_2.mainloop()
    window_1 = Toplevel()
    window_1.title("OTESL")
    window_1.geometry("1366x768")
    window_1.configure(bg = "#FFFFFF")
    canvas = Canvas(
        window_1,
        bg = "#FFFFFF",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window_1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=1211.0,
        y=0.0,
        width=167.0,
        height=161.0
    )
    canvas.create_rectangle(
        -4.0,
        75.76373291015625,
        1235.0,
        80.0,
        fill="#000000",
        outline="")
    canvas.create_rectangle(
        1342.0,
        76.0,
        1440.0,
        80.0,
        fill="#000000",
        outline="")
    canvas.create_rectangle(
        178.0,
        75.0,
        186.0,
        1024.0,
        fill="#000000",
        outline="")
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window_1,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=0.0,
        y=108.0,
        width=167.0,
        height=106.0
    )
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        window_1,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=395.0,
        y=406.0,
        width=163.0,
        height=61.0
    )
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        window_1,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=985.0,
        y=406.0,
        width=163.0,
        height=61.0
    )
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        window_1,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=0.0,
        y=255.0,
        width=167.0,
        height=106.0
    )
    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        window_1,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=0.0,
        y=397.0,
        width=167.0,
        height=106.0
    )
    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        window_1,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=hq,
        relief="flat"
    )
    button_7.place(
        x=384.0,
        y=202.0,
        width=188.0,
        height=167.0
    )
    canvas.create_text(
        202.0,
        104.0,
        anchor="nw",
        text="Nhung Thiet Ke Mau:",
        fill="#000000",
        font=("Inter", 30 * -1)
    )
    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        window_1,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=846.0,
        y=213.0,
        width=413.0,
        height=148.0
    )
    canvas.create_text(
        19.0,
        20.0,
        anchor="nw",
        text="OTESL",
        fill="#000000",
        font=("Inter", 40 * -1)
    )
    canvas.create_rectangle(
        175.0,
        158.0,
        1440.0,
        162.0,
        fill="#000000",
        outline="")
    canvas.create_rectangle(
        174.0,
        507.0,
        1440.0,
        512.0,
        fill="#000000",
        outline="")
    canvas.create_text(
        205.0,
        536.0,
        anchor="nw",
        text="Ca Nhan Hoa (Thiet Ke Nang Cao):",
        fill="#000000",
        font=("Inter", 30 * -1)
    )
    canvas.create_rectangle(
        177.0,
        589.9233856201172,
        1439.999755859375,
        599.0,
        fill="#000000",
        outline="")
    canvas.create_text(
        205.0,
        622.0,
        anchor="nw",
        text="Tinh Nang Nay Dang Trong Giai Doan Phat Trien.\n Xin Loi Quy Khach Vi Su Bat TIen Nay !!!",
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    window_1.resizable(False, False)
    window_1.mainloop()




def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()