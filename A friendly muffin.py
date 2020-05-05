def user(self):
  hav_username = input("Do you have a account? (y/n) ", 'green')
  if hav_username == "y":
      # authenticate user
      auth = 0
      users = open("users.txt", 'r')
      username = input("Username: ")
      password = input("Password: ")
      for line in users:
          user, passwd = line.rstrip().split(',')
          if username == user and password == passwd:
              auth = 1
              authuser = user
              print("WELCOME! ")