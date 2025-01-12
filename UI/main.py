import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import redis


#ToDo
#fix coding style
#change login credentials entry look
# clear user pass after login and key input
# don't clear login/pass upon re-clicking
# password show="*"
# add documentation on github change name to personal manager, 
# tools used, what it does, how to use it, steps
#fix invalid username/pass

class App:
    def __init__(self, root):
        self.root=root
        self.user=""
        self.password=""
        self.redisDB=redis.Redis(host='redis', port=6379, decode_responses=True)
        self.populate_redis()
        self.keysString=tk.StringVar(value="")

        #PAGE ONE(login)
        self.imgFrameLoginPage=tk.Frame(root,width=650,height=450,bg="white")
        self.imgFrameLoginPage.place(relx=.40,rely=.50, anchor="center")

        self.loginImage = ImageTk.PhotoImage(Image.open("login.png"))
        tk.Label(self.imgFrameLoginPage,image=self.loginImage,bg="white").place(x=50,y=50)

        self.credentialsFrameLoginPage=tk.Frame(root,width=400,height=550,bg="white")
        self.credentialsFrameLoginPage.place(relx=.780,rely=.580,anchor="center")

        heading=tk.Label(self.credentialsFrameLoginPage,text='Sign in',fg="#57a1f8",bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(relx=.35,rely=.15,anchor="center")

        #Username input
        self.user=tk.Entry(self.credentialsFrameLoginPage,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11))
        self.user.place(relx=.375,rely=.25,anchor="center")
        # self.user.insert(0,'Username')
        self.user.bind("<FocusIn>", self.on_enter_user())
        self.user.bind("<FocusOut>", self.on_leave_user())

        #Password input
        self.password=tk.Entry(self.credentialsFrameLoginPage,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11),)
        self.password.place(relx=.375,rely=.395,anchor="center")
        # self.password.insert(0,'Password')
        self.password.bind("<FocusIn>", self.on_enter_password())
        self.password.bind("<FocusOut>", self.on_leave_password())
        
        
        tk.Button(self.credentialsFrameLoginPage,width=14,pady=7,text="Sign in",fg="white", bg="#57a1f8", border=0, command=self.signin).place(relx=.385,rely=.495,anchor="center")

        #PAGE TWO(access usernames and passwords)
        self.managerPage = tk.Frame(self.root, height=850, width=700, bg="white")
        self.managerPage.place(relx=.5,rely=.1,anchor="center")
        self.managerPage.place_forget()
        
        self.keyInput = tk.StringVar()
        self.my_var = tk.StringVar(value="")

        tk.Label(self.managerPage,text="Welcome back to your password manager Mr.M18.", font=("Times New Roman", 18, "bold"),bg="white").place(relx=.5,rely=.1,anchor="center")
        tk.Label(self.managerPage,text="Please enter your key(websites/account reference) below.", font=("Times New Roman", 12, "bold"),bg="white").place(relx=.5,rely=.15,anchor="center")
        tk.Label(self.managerPage,text="Hint: enter 'keys' to list all keys.", font=("Times New Roman", 12, "bold"),bg="white").place(relx=.5,rely=.2,anchor="center")
        tk.Entry(self.managerPage, textvariable=self.keyInput).place(relx=.5,rely=.25,anchor="center")
        tk.Button(self.managerPage,width=12,pady=5,text="Enter",fg="white", bg="#57a1f8", border=0,command=self.update_query_response).place(relx=.5,rely=.3,anchor="center")
        self.queryLabel=tk.Label(self.managerPage,textvariable=self.my_var,fg="black",bg="white", font=("Microsoft YaHei UI Light", 20, "bold")).place(relx=.5,rely=.378,anchor="center")

        self.redisImage=Image.open("redisBackground.png")
        self.redisImage= self.redisImage.resize((550,400))
        self.redisImage = ImageTk.PhotoImage(self.redisImage)
        
        # Create a label widget to hold the image.
        image_label = tk.Label(self.managerPage, image=self.redisImage,bg="white")

        # Place the label in the frame.
        image_label.place(relx=.5,rely=.65, anchor="center")

        tk.Button(self.managerPage,bg="white",text="Logout",border=0,command=self.logout).place(relx=.5,rely=.9, anchor="center")

    #switch from login page to username-password manager page.
    def create_second_page(self):
        self.credentialsFrameLoginPage.place_forget()
        self.imgFrameLoginPage.place_forget()
        self.root.geometry("900x800")
        self.managerPage.place(relx=.5,rely=.5,anchor="center")
        self.user.delete(0,'end')
        self.password.delete(0,'end')
        self.on_enter_user()
        self.on_leave_user()
        self.on_enter_password()
        self.on_leave_password()

    #Clear username on click of entry box.
    def on_enter_user(self):
        self.user.delete(0,'end')

    #return username text when clicked off entry box.
    def on_leave_user(self):
        name=self.user.get()
        if name=="":
            self.user.insert(0,'Username')

    #Clear password on click of entry box.
    def on_enter_password(self):
        self.password.delete(0,'end')

    #return password text when clicked off entry box.
    def on_leave_password(self):
        name=self.password.get()
        if name=="":
            self.password.insert(0,'Password')

    #Update query response if key exists. Else write "Key not found.".
    def update_query_response(self):
        entry=self.keyInput.get()
        if entry=="keys":
            for key in self.redisDB.scan_iter("*"):
                current_value = self.keysString.get()
                new_value = current_value +  str(key) + "\n"
                self.keysString.set(new_value)
            self.create_keys_page()
        else:
            value = self.redisDB.get(entry)
            if value:  
                self.my_var.set(value)
            else:
                self.my_var.set("Key not found.")
        self.keyInput.set("")

    #Display keys(account names) to user in new top level window.
    def create_keys_page(self):
        top = tk.Toplevel(self.root, bg="white")
        top.geometry("600x200")
        top.title("Keys")
        testLabel=tk.Label(top,textvariable=self.keysString,bg="white")
        testLabel.pack()

    #Check for correct sign in credentials.
    def signin(self):
        usernameInput=self.user.get()
        passwordInput=self.password.get()

        if usernameInput=="admin" and passwordInput=="pass":
            self.create_second_page()
        elif self.usernameInput!='admin':
            messagebox.showerror("Invalid", "Invalid username.")
        else:
            messagebox.showerror("Invalid", "Invalid password.")
    
    #log user out. Return to login page.
    def logout(self):
        self.managerPage.place_forget()
        self.root.geometry("900x500")
        self.credentialsFrameLoginPage.place(relx=.780,rely=.580,anchor="center")
        self.imgFrameLoginPage.place(relx=.40,rely=.50, anchor="center")
        self.testEntry.set("")
    
    # Create a Redis client.
    def populate_redis(self):
        # change later to containerized redis
        usernamesAndPasswords=open("Users-Passwords.txt","r")
        for line in usernamesAndPasswords:
            lineWords=line.split(",")
            self.redisDB.set(lineWords[0],lineWords[1])

def main():
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Username-Password Manager")
    root.configure(bg="#fff")
    app = App(root)
    root.mainloop()
if __name__ == "__main__":
    main()