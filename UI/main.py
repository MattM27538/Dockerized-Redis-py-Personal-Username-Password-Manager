#ToDOs
# give redis it's own func
#fix coding style
#change login credentials entry look
#make app fit screen? Or lock screen size
# clear user pass after login
# don't clear login/pass upon re-clicking
# e parameter needed?
#top level to display keys
# redis read from txt


import tkinter as tk
from tkinter import messagebox
import redis

def on_enter_user(e):
    user.delete(0,'end')

def on_leave_user(e):
    name=user.get()
    if name=="":
        user.insert(0,'Username')

def on_enter_password(e):
    password.delete(0,'end')

def on_leave_password(e):
    name=password.get()
    if name=="":
        password.insert(0,'Password')

def on_enter_query(e):
    query.delete(0,'end')

def on_leave_query(e):
    name=query.get()
    if name=="":
        query.insert(0,'Account Name')

def initializeRedis():
    # Create a Redis client
    redisDB = redis.Redis(host='localhost', port=6379, decode_responses=True)

    redisDB.set('facebook.com', 'username: foo\npassword: bar')
    redisDB.set('maplestory', 'username: foo2\npassword: bar2')
    return redisDB

def signin():
    usernameInput=user.get()
    passwordInput=password.get()
    queryInput=query.get()

    if usernameInput=="admin" and passwordInput=="pass":
        # print(queryInput)
        # print(redisDB.keys())
        if queryInput=="keys":
            #ADD top level here to list keys
            print("entered 'keys'")
        elif redisDB.get(queryInput):
            # print("redis succeeded")
            queryResponse.config(text=redisDB.get(queryInput))
        else:
            queryResponse.config(text="Incorrect Account \nName")
        # print("logged in successfully")
        
        # redisScreen.mainloop()
    elif usernameInput!='admin':
        messagebox.showerror("Invalid", "Invalid username.")
    else:
        messagebox.showerror("Invalid", "Invalid password.")

root=tk.Tk()
root.geometry("1100x500")
root.title("Username-Password Manager")
root.configure(bg="#fff")
root.resizable(False, False)

imgFrame=tk.Frame(root,width=650,height=450,bg="white")
imgFrame.place(x=20,y=20)

img = tk.PhotoImage(file='login.png')
tk.Label(imgFrame,image=img,bg="white").place(x=50,y=50)

frame=tk.Frame(root,width=400,height=550,bg="white")
frame.place(x=580,y=70)

heading=tk.Label(frame,text='   Welcome back to your password \nmanager Mr.M18!',fg="#57a1f8",bg="white", font=("Microsoft YaHei UI Light", 14, "bold"))
heading.place(x=0,y=5)

headingHint=tk.Label(frame,text='Hint:Enter your credentials along with"keys" as your \naccount name for a list of account names',fg="#57a1f8",bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
headingHint.place(x=0,y=60)

#Username input
user=tk.Entry(frame,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11))
user.place(x=80,y=130)
user.insert(0,'Username')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

#Password input
password=tk.Entry(frame,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11))
password.place(x=80,y=180)
password.insert(0,'Password')
password.bind("<FocusIn>", on_enter_password)
password.bind("<FocusOut>", on_leave_password)

query=tk.Entry(frame,width=25,fg='black',bg='white',font=("Microsoft YaHei UI Light", 11))
query.place(x=80,y=230)
query.insert(0,'Account Name')
query.bind("<FocusIn>", on_enter_query)
query.bind("<FocusOut>", on_leave_query)

# Create a Redis client
global redisDB
redisDB = redis.Redis(host='localhost', port=6379, decode_responses=True)

redisDB.set('facebook.com', 'username: foo\npassword: bar')
redisDB.set('maplestory', 'username: foo2\npassword: bar2')


#Login button
tk.Button(frame,width=14,pady=7,text="Sign in",fg="white", bg="#57a1f8", border=0, command=signin).place(x=120,y=270)

queryResponse=tk.Label(frame,text='',fg="red",bg="white", font=("Microsoft YaHei UI Light", 20, "bold"))
queryResponse.place(x=80,y=310)

root.mainloop()
