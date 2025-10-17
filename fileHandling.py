

from pathlib import Path





def readfileandfolder():
    root = Path.cwd()
    for i, p in enumerate(sorted(root.iterdir()), start=1):
        if p.is_file() and p.name != ".git" and not p.name.startswith("."):
            print(f"{i} : {p.name}")


def createfile():
    try:

        readfileandfolder()
        name = input("please tell your file name:-")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as f:
                data = input("What do you want to write")
                f.write(data)
            print("File Created successfully!!")
        else:

            print("This file already exist!!")   

        
    except Exception as err:
        print(f"An error occurs as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file do you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("Readed successfully!!")
        else:
            print("File does not exist ")
    except Exception as err:
        print(f"An error has occured as {err}")       

             


               



print("Press 1 for creating a file ")
print("Press 2 for reading a file ")
print("Press 3 for updating a file ")
print("Press 4 for deletion a file ")

check = int(input("Select your options between 1 to 4:"))

if check ==1:
    readfileandfolder()
    createfile()
if check == 2:
    readfileandfolder()
    readfile()

