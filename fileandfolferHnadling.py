from pathlib import Path
import shutil
# ...existing code...


def readfolders():
    root = Path.cwd()
    for i, d in enumerate(sorted(p for p in root.iterdir() if p.is_dir()
                                 and d.name != ".git" and not p.name.startswith(".")), start=1):
        print(f"{i} : {d.name}")


def create_folder():
    try:
        readfolders()
        name = input("Folder name to create: ").strip()
        p = Path(name)
        if p.exists():
            print("A file/folder with that name already exists.")
            return
        p.mkdir()
        print("Folder created successfully!")
    except Exception as err:
        print(f"An error occurred: {err}")


def read_folder():
    try:
        readfolders()
        name = input("Which folder to view ('.' for current): ").strip() or "."
        p = Path(name)
        if not p.exists() or not p.is_dir():
            print("Folder does not exist.")
            return
        for item in sorted(p.iterdir()):
            if item.name == ".git" or item.name.startswith("."):
                continue
            tag = "[DIR]" if item.is_dir() else "     "
            print(f"{tag} {item.name}")
    except Exception as err:
        print(f"An error occurred: {err}")


def rename_folder():
    try:
        readfolders()
        old = Path(input("Folder to rename: ").strip())
        if not old.exists() or not old.is_dir():
            print("Folder does not exist.")
            return
        new_name = input("New folder name: ").strip()
        new = old.with_name(new_name)
        if new.exists():
            print("Target name already exists.")
            return
        old.rename(new)
        print("Folder renamed successfully!")
    except Exception as err:
        print(f"An error occurred: {err}")


def delete_folder():
    try:
        readfolders()
        target = Path(input("Folder to delete: ").strip())
        if not target.exists() or not target.is_dir():
            print("Folder does not exist.")
            return
        if any(target.iterdir()):
            confirm = input(
                "Folder not empty. Delete recursively? (y/N): ").strip().lower()
            if confirm == "y":
                shutil.rmtree(target)
                print("Folder deleted.")
            else:
                print("Cancelled.")
        else:
            target.rmdir()
            print("Folder deleted.")
    except Exception as err:
        print(f"An error occurred: {err}")


# ...existing code...
print("Press 1 for creating a file ")
print("Press 2 for reading a file ")
print("Press 3 for updating a file ")
print("Press 4 for deletion a file ")
print("Press 5 for creating a folder ")
print("Press 6 for reading a folder ")
print("Press 7 for renaming a folder ")
print("Press 8 for deleting a folder ")

check = int(input("Select your options between 1 to 8: "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    print("Update file not implemented yet.")
elif check == 4:
    print("Delete file not implemented yet.")
elif check == 5:
    create_folder()
elif check == 6:
    read_folder()
elif check == 7:
    rename_folder()
elif check == 8:
    delete_folder()
else:
    print("Invalid option.")
