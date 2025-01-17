Docker-containerized password manager using python and redis-py. 

Redis-py-Personal-Password-Manager creates an image of a redis instance containing usernames and password values keyed from domain-names/ account-identifiers. The image can be uploaded to dockerhub to access from any point with access to the internet that can run docker. 

The manager requires login credentials by changing the values to check for on line 152 of main.py, to be set before the image is created:
![image](https://github.com/user-attachments/assets/be5270ea-e984-4f56-8e4a-56d1b20aa2c6)

I created this manager because I've had computers randomly die on me and I lost my saved usernames and passwords on those computers. By using docker/dockerhub to store this information I or anyone else that wishes to use my manager can access this information from any 
computer with docker and internet access without using any external services such as google docs or other iterations of password managers across the internet.
