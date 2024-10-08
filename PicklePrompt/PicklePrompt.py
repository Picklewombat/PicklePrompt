import os
import time
import sys
import random
script_dir = os.path.dirname(os.path.abspath(__file__))
user_path = os.path.join(script_dir, 'users')
cont = True
print("Welcome to PicklePrompt")
while cont == True:
  with open(user_path, "r") as fi:
    #print(fi.read())
    if fi.read() == "FirstStartupTrue":
      print("It appears that this is your first time using PicklePrompt.")
      print("y/n")
      cmd = input("> ")
      fi.close()
      
      if cmd == "y":
        print("Setting up PicklePrompt...")
        cmd = ""
        username = ""
        password = ""
        with open(user_path, "w") as f:
          f.write("recoveryneeded")
          print("What would you like to set your username to?")
          username = input("> ")
          username = username.replace("|", "")
          print("What would you like to set your password to?")
          password = input("> ")
          print("Saving Login Info...")
          f.close()
          with open(user_path, "w") as f:
           cont = False
           f.write("\n" + username + "|" + password)
           f.close()
           print("File Saved Succesfully")
    else:
      with open(user_path, "r") as fi:
        if fi.read() == "recoveryneeded":
          cont = False
          print("An error occured while setting up your PicklePrompt, please try re-installing it.")
          fi.close()
        else:
          with open(user_path, "r") as fi:
            print("Enter your password and username")
            print("\n")
            fileadd = 0
            accountiteration = 0
            accountdata = {}
            correctusername = ""
            correctpassword = ""
            for i in fi.readlines():
              fileadd = 0
              accountiteration += 1
              correctusername = ""
              correctpassword = ""
              for char in list(i):
                if fileadd == 0:
                  if char == "|":
                    fileadd = 1
                    accountdata[correctusername] = correctpassword
                  else:
                    correctusername = correctusername + char
                    accountdata[correctusername] = correctpassword
                elif fileadd == 1:
                  correctpassword = correctpassword + char
                  accountdata[correctusername] = correctpassword
            username = input("Username: ")
            password = input("Password: ")
            try:
              if accountdata[username] == password:
                 print("Access Granted... Launching")
                 time.sleep(1)
                 os.system('cls' if os.name == 'nt' else 'clear')
                 cont = False
              else:
                print("Incorrect Password")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            except KeyError:
              print("That username was not found")
              time.sleep(1)
              os.system('cls' if os.name == 'nt' else 'clear')
          
      
