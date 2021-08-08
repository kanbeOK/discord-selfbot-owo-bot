import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import cheat, json
class App:
    def __init__(self, root):
        #setting title
        root.title("Choose login method")
        #setting window size
        width=240
        height=100
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        token_button=tk.Button(root)
        token_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        token_button["font"] = ft
        token_button["fg"] = "#000000"
        token_button["justify"] = "center"
        token_button["text"] = "Token"
        token_button.place(x=10,y=50,width=100,height=30)
        token_button["command"] = lambda: self.token_button_command(root)

        token_button=tk.Button(root)
        token_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        token_button["font"] = ft
        token_button["fg"] = "#000000"
        token_button["justify"] = "center"
        token_button["text"] = "email + pass"
        token_button.place(x=130,y=50,width=100,height=30)
        token_button["command"] = lambda: self.mail_button_command(root)

        label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label["font"] = ft
        label["fg"] = "#333333"
        label["justify"] = "center"
        label["text"] = "Choose login method"
        label.place(x=0,y=10,width=242,height=30)

    def mail_button_command(self, root):
        if __name__ == "__main__":
            root.destroy()
            root = tk.Tk()
            app = auth.email(root)
            root.mainloop()


    def token_button_command(self, root):
        if __name__ == "__main__":
            root.destroy()
            root = tk.Tk()
            app = auth.token(root)
            root.mainloop()
class auth:
    email, password, token = "", "", ""
    def login(method, root, i1, i2 = ""):
        print(method, root, i1, i2)
        root.withdraw()
        newline = "\n"
        print(f"login with {'token' if method else 'email and password'} \n { 'token: '+i1 if method else 'email: '+ i1 + newline +' password: '+i2} ")
        CH_RESP = cheat.check_creditials(method, i1, i2)
        print (CH_RESP)
        if CH_RESP.status_code != 200:
            messagebox.showerror("Login Failed", "Cannot login to the account, possible fixes: \n - Allways use Token Auth\n  - be sure token is valid\n - Be sure email and password is correct\n - Be sure you have internet connection")
            root.iconify()
            # this part doesn't work
            # point is show the window, it's hiding on bottom

            # {
            root.lift()
            root.after(1, lambda: root.focus_force())
            # }

        else:
            root.destroy()
            cheat.run(method, i1, i2)
    class email:
        def __init__(self, root):
            root.title("Login")
            width=280
            height=150
            px, py, pb = 20,20,25
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root.geometry(alignstr)
            root.resizable(width=False, height=False)

            email_field=tk.Entry(root, textvariable=auth.email)
            email_field["bg"] = "#999999"
            email_field["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            email_field["font"] = ft
            email_field["fg"] = "#333333"
            email_field["justify"] = "center"
            email_field["text"] = "email"
            email_field["relief"] = "sunken"
            email_field.place(x=px,y=py,width=width-px*2,height=pb)

            password_field=tk.Entry(root, textvariable=auth.password)
            password_field["bg"] = "#999999"
            password_field["borderwidth"] = "1px"
            password_field["cursor"] = "watch"
            ft = tkFont.Font(family='Times',size=10)
            password_field["font"] = ft
            password_field["fg"] = "#333333"
            password_field["justify"] = "center"
            password_field["text"] = "Password"
            password_field["relief"] = "sunken"
            password_field.place(x=px,y=py+pb*2,width=width-px*2,height=pb)

            loginbutton=tk.Button(root)
            loginbutton["bg"] = "#90f090"
            ft = tkFont.Font(family='Times',size=10)
            loginbutton["font"] = ft
            loginbutton["fg"] = "#000000"
            loginbutton["justify"] = "center"
            loginbutton["text"] = "Login"
            loginbutton.place(x=190,y=pb*4+10,width=80,height=30)
            loginbutton["command"] = lambda: auth.login(0, root, email_field.get(), password_field.get())

            changemethodbutton=tk.Button(root)
            changemethodbutton["bg"] = "#932a00"
            ft = tkFont.Font(family='Times',size=10)
            changemethodbutton["font"] = ft
            changemethodbutton["fg"] = "#000000"
            changemethodbutton["justify"] = "center"
            changemethodbutton["text"] = "Use token"
            changemethodbutton.place(x=95,y=pb*4+10,width=80,height=30)
            changemethodbutton["command"] = lambda: self.method(root)
        def method(self, root):
            if __name__ == "__main__":
                root.destroy()
                root = tk.Tk()
                app = auth.token(root)
                root.mainloop()
        def login(self):
            print("login action")


    class token:
        def __init__(self, root):
            root.title("Login")
            width=280
            height=150
            px, py, pb = 20,20,25
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root.geometry(alignstr)
            root.resizable(width=False, height=False)

            token_field=tk.Entry(root, textvariable=auth.token)
            token_field["bg"] = "#999999"
            token_field["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            token_field["font"] = ft
            token_field["fg"] = "#333333"
            token_field["justify"] = "center"
            token_field["text"] = "token"
            token_field["relief"] = "sunken"
            token_field.place(x=px,y=py,width=width-px*2,height=pb)

            loginbutton=tk.Button(root)
            loginbutton["bg"] = "#90f090"
            ft = tkFont.Font(family='Times',size=10)
            loginbutton["font"] = ft
            loginbutton["fg"] = "#000000"
            loginbutton["justify"] = "center"
            loginbutton["text"] = "Login"
            loginbutton.place(x=190,y=pb*4+10,width=80,height=30)
            loginbutton["command"] = lambda: auth.login(1, root, token_field.get())

            changemethodbutton=tk.Button(root)
            changemethodbutton["bg"] = "#932a00"
            ft = tkFont.Font(family='Times',size=10)
            changemethodbutton["font"] = ft
            changemethodbutton["fg"] = "#000000"
            changemethodbutton["justify"] = "center"
            changemethodbutton["text"] = "Use Email"
            changemethodbutton.place(x=95,y=pb*4+10,width=80,height=30)
            changemethodbutton["command"] = lambda: self.method(root)

        def method(self, root):
            if __name__ == "__main__":
                root.destroy()
                root = tk.Tk()
                app = auth.email(root)
                root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
