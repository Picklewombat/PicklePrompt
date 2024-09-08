import os
import time
import sys
import random
cont = True
print("Welcome to PicklePrompt")
while cont == True:
  with open("PicklePrompt/users", "r") as fi:
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
        with open("PicklePrompt/users", "w") as f:
          f.write("recoveryneeded")
          print("What would you like to set your username to?")
          username = input("> ")
          username = username.replace("|", "")
          print("What would you like to set your password to?")
          password = input("> ")
          print("Saving Login Info...")
          f.close()
          with open("PicklePrompt/users", "w") as f:
           cont = False
           f.write("\n" + username + "|" + password)
           f.close()
           print("File Saved Succesfully")
    else:
      with open("PicklePrompt/users", "r") as fi:
        if fi.read() == "recoveryneeded":
          cont = False
          print("An error occured while setting up your PicklePrompt, please try re-installing it.")
          fi.close()
        else:
          with open("PicklePrompt/users", "r") as fi:
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
                 os.system("clr")
                 cont = False
              else:
                print("Incorrect Password")
                print(accountdata[correctusername])
                time.sleep(1)
                os.system("clr")
            except KeyError:
              print("That username was not found")
              time.sleep(1)
              os.system("clr")
          
      
