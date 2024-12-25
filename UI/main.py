import tkinter as tk


class homePage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="Redis interface page under construction. Come back soon.").pack(padx=10,pady=10)



class loginPage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        usernameInput=tk.StringVar()
        passwordInput=tk.StringVar()


        tk.Label(self, text="Hello, Mr.M18. Please enter your credentials.\n", font=("Times New Roman", 12)).pack()
        usernameLabel=tk.Label(self, text ="Username", font=("Times New Roman", 12,"bold")).pack()
        usernameEntry=tk.Entry(self, textvariable ="usernameInput", font=("Times New Roman", 12,"bold")).pack()

        passwordLabel=tk.Label(self, text="Password", font=("Times New Roman", 12,"bold")).pack()
        passwordEntry=tk.Entry(self, textvariable="passwordInput", font=("Times New Roman", 12,"bold"), show="*").pack()




class mainWindow():
    def __init__(self,master):
        mainframe=tk.Frame(master)
        mainframe.pack(padx=10,pady=10,fill='both',expand=1)
        
        self.index=0
        self.buttonDisplay="Login/Logout"
        # self.loginText="Login"
        # self.logoutText="Logout"


        self.frameList=[homePage(mainframe), loginPage(mainframe)]
        self.frameList[1].forget()

        # self.wordList["login","logout"]

        bottomframe=tk.Frame(master)
        bottomframe.pack(padx=10,pady=10)

        self.changeWindow()

        switch= tk.Button(bottomframe,text=self.buttonDisplay, command=self.changeWindow)
        switch.pack(padx=10,pady=10)
        

    def changeWindow(self):
        self.frameList[self.index].forget()
        self.index=(self.index+1)%len(self.frameList)
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack(padx=10,pady=10)
        #FIX BUTTON TO SWITCH BETWEEN LOGIN AND LOGOUT
        # if self.buttonDisplay=="Login":
        #     self.buttonDisplay="Logout"
        # else:
        #     self.buttonDisplay="Login"


root=tk.Tk()
root.geometry("600x400")
root.title("Username-Password Manager")
window=mainWindow(root)

# welcomeText=tk.Label(root, text="Hello, Mr.M18.\n", font=("Times New Roman", 12))
# # emojiText=tk.Label(root, text='\U0001F923', font=("", 100))

# usernameInput=tk.StringVar()
# passwordInput=tk.StringVar()


# usernameLabel=tk.Label(root, text ="Username", font=("Times New Roman", 12,"bold"))
# usernameEntry=tk.Entry(root, textvariable ="usernameInput", font=("Times New Roman", 12,"bold"))

# passwordLabel=tk.Label(root, text="Password", font=("Times New Roman", 12,"bold"))
# passwordEntry=tk.Entry(root, textvariable="passwordInput", font=("Times New Roman", 12,"bold"))

# # submitButton=tk.Button(root,text="Submit", command=lambda: controller.show_frame(homePage))

# welcomeText.grid(row=0,column=1)

# usernameLabel.grid(row=1, column=0)
# usernameEntry.grid(row=1, column=1)
# passwordLabel.grid(row=2, column=0)
# passwordEntry.grid(row=2, column=1)
# # submitButton.grid(row=3,column=1)

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
# root.columnconfigure(3, weight=1)



root.mainloop()