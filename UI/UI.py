import redis

username="Mmartinez18"
password="Redisacc0unt!"

print("Hello, Mr.M18.")

# Login with credentials
while True:
    print("Please Enter username(case-sensitive):")
    usernameCheck=str(input())
    if(usernameCheck!=username):
        print("Incorrect username")
    else: break

while True:
    print("Please Enter Password(case-sensitive):")
    passCheck=str(input())
    if(passCheck!=password):
        print("Incorrect password")
    else: break


# Create a Redis client
redisDB = redis.Redis(host='localhost', port=6379, decode_responses=True)

redisDB.set('facebook.com', 'username: foo\npassword: bar')
redisDB.set('maplestory', 'username: foo2\npassword: bar2')

#Simple UI for database
print("Welcome back to your password manager Mr.M18.")
while True:
    print("Enter 1 to list keys(websites/account reference), 2 to enter a key, or 3 to exit.")
    task=str(input())
    if task=="1":
        for key in redisDB.scan_iter():
            print(key)
    elif task=="2":
        print("Enter key:")
        value=str(input())
        print(redisDB.get(value))
    elif task=="3":
        print("Password manager closing. Goodbye.")
        redisDB.flushdb()
        break
    else: print("Unrecognized command.")