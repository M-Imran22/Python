from pathlib import Path
import shutil

file_path = Path("./My_Intro.txt")
# print(file_path.cwd()) # print : cuttent working dir

# print(file_path.absolute()) # print the complete path of the file

# print(file_path.read_text()) # print: the file text in string

# file_path.write_text("Hi, it's M Imran form jehangira.A BSCS student in GDC Lahore Sawabi.") # update the file with new text.

# file_path.rename("Intro.txt") # remane the file

# print(file_path.exists()) # print: True

# print(file_path.name)  # print : file name (My_Intro.txt)

# print(file_path.suffix)  # print : file type (.txt)
# file_path.unlink() # delete the file.

target = Path() / "New_Intro.py"

# shutil.copy(file_path, target) # copy all the file (My_Intro.txt) into new file (New_Intro.py)

# print(target.read_text()) # print: the same text.
