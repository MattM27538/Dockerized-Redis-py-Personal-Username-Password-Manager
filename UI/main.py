import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox



class App:
    def __init__(self, root):
        self.root= root
        self.user=""
        self.password=""
        # self.my_var = tk.StringVar(value="Initial Value")
        # self.queryEntry=tk.StringVar(value="Initial Value")

        self.imgFrame=tk.Frame(root,width=650,height=450,bg="white")
        self.imgFrame.place(x=20,y=20)

        self.loginImage = ImageTk.PhotoImage(Image.open("login.png"))
        tk.Label(self.imgFrame,image=self.loginImage,bg="white").place(x=50,y=50)

        self.credentialsFrame=tk.Frame(root,width=400,height=550,bg="white")
        self.credentialsFrame.place(x=580,y=70)

        heading=tk.Label(self.credentialsFrame,text='Sign in',fg="#57a1f8",bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=80,y=5)

        #Username input
        self.user=tk.Entry(self.credentialsFrame,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30,y=80)
        self.user.insert(0,'Username')
        self.user.bind("<FocusIn>", self.on_enter_user())
        self.user.bind("<FocusOut>", self.on_leave_user())

        #Password input
        self.password=tk.Entry(self.credentialsFrame,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11))
        self.password.place(x=30,y=150)
        self.password.insert(0,'Password')
        self.password.bind("<FocusIn>", self.on_enter_password())
        self.password.bind("<FocusOut>", self.on_leave_password())
        
        
        tk.Button(self.credentialsFrame,width=14,pady=7,text="Sign in",fg="white", bg="#57a1f8", border=0, command=self.signin).place(x=70,y=204)

    def on_enter_user(self):
        self.user.delete(0,'end')

    def on_leave_user(self):
        name=self.user.get()
        if name=="":
            self.user.insert(0,'Username')

    def on_enter_password(self):
        self.password.delete(0,'end')

    def on_leave_password(self):
        name=self.password.get()
        if name=="":
            self.password.insert(0,'Password')

    def update_query(self,queryEntry):
        self.my_var=queryEntry.get()
        print(self.my_var)

    def create_second_page(self):
        root.geometry("900x800")
        # global entry_value
        # Create a new frame
        self.managerFrame = tk.Frame(self.root, bg="white")
        self.managerFrame.pack()
        # self.query=tk.StringVar
        # self.entry=tk.StringVar
        # Update variable with user input
        # self.my_var.set(self.entry1.get())

        # Display the updated variable
        # self.label2 = tk.Label(self.frame2, textvariable=self.my_var)
        # self.label2.pack()
        tk.Label(self.managerFrame,text="Welcome back to your password manager Mr.M18.", font=("Times New Roman", 18, "bold"),bg="white").grid(row=0,column=3,pady=(20,0))
        tk.Label(self.managerFrame,text="Please enter your key(websites/account reference) below.", font=("Times New Roman", 12, "bold"),bg="white").grid(row=1,column=3,pady=10)
        tk.Label(self.managerFrame,text="Hint: enter 'keys' to list all keys.", font=("Times New Roman", 12, "bold"),bg="white").grid(row=2,column=3,pady=10)
        entry=tk.Entry(self.managerFrame).grid(row=3,column=3,pady=10)
        tk.Button(self.managerFrame,width=12,pady=5,text="Enter",fg="white", bg="#57a1f8", border=0,command=print()).grid(row=4,column=3,pady=10)
        queryResponse=tk.Label(self.managerFrame,text='',fg="black",bg="white", font=("Microsoft YaHei UI Light", 20, "bold")).grid(row=5,column=3,pady=10)


        self.image = ImageTk.PhotoImage(Image.open("redisBackground.png"))

        # Create a label widget to hold the image
        image_label = tk.Label(self.managerFrame, image=self.image,bg="white")

        # Place the label in the frame
        image_label.grid(row=6, column=3)

    def signin(self):
        usernameInput=self.user.get()
        passwordInput=self.password.get()

        if usernameInput=="admin" and passwordInput=="pass":
            self.imgFrame.destroy()
            self.credentialsFrame.destroy()
            self.create_second_page()
        elif self.usernameInput!='admin':
            messagebox.showerror("Invalid", "Invalid username.")
        else:
            messagebox.showerror("Invalid", "Invalid password.")

root = tk.Tk()
# entry_value = tk.StringVar(value="initalval")
root.geometry("900x500")
root.title("Username-Password Manager")
root.configure(bg="#fff")
root.resizable(False, False)
app = App(root)
root.mainloop()