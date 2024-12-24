import tkinter as tk

root=tk.Tk()

root.geometry("600x400")
root.title("Username-Password Manager")

welcomeText=tk.Label(root, text="Hello, Mr.M18.\nWelcome back to your username-password manager.", font=("Times New Roman", 12))
# emojiText=tk.Label(root, text='\U0001F923', font=("", 100))

usernameInput=tk.StringVar()
passwordInput=tk.StringVar()


usernameLabel=tk.Label(root, text ="Username", font=("Times New Roman", 12,"bold"))
usernameEntry=tk.Entry(root, textvariable ="usernameInput", font=("Times New Roman", 12,"bold"))

passwordLabel=tk.Label(root, text="Password", font=("Times New Roman", 12,"bold"))
passwordEntry=tk.Entry(root, textvariable="passwordInput", font=("Times New Roman", 12,"bold"))

submitButton=tk.Button(root,text="Submit")

welcomeText.grid(row=0,column=1)

usernameLabel.grid(row=1, column=0)
usernameEntry.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0)
passwordEntry.grid(row=2, column=1)
submitButton.grid(row=3,column=1)

# root.columnconfigure(0, weight=0)
# root.columnconfigure(1, weight=1)

redisFrame=tk.Frame(root)
redisFrame.configure(height=600,width=400)

root.mainloop()