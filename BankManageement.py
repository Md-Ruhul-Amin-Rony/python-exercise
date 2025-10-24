import json
import random
import string
from pathlib import path




class Bank:

    database = 'data.json'
    data = []
    try:
          if Path(database).exists():
              with open(database, 'r') as fs:
                data = json.loads(fs.read())
          else:
              print("No such file exist ")
    
    except Exception as err:
        print(f"An exception has been occured with error {err}")
            
          
    def __init__(self):
        pass
    def Createaccount(self):
        info = {
            "name" : input("Please write your name: "),
            "age" : int(input("please write your age: ")),
            "email": input("pleasae write your email:") ,
            "pin": int(input("please write your pin:")),
            "accountNo": 1234,
            "balance":0  
        }

    


user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdraw money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account ")

check = int(input("Tell me your response: "))
if check ==1:
    user.Createaccount()

