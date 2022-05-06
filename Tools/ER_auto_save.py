import shutil
import subprocess
import os

# src = steam save file path
# dest = local backup path
save_file_src = r"C:\Users\jserrano\OneDrive - HPM Foundation, Inc\Desktop\Test Folder"
save_file_dest = r"C:\Users\jserrano\OneDrive - HPM Foundation, Inc\Desktop\Test Folder Copied"

shutil.copytree(save_file_src, save_file_dest, dirs_exist_ok=True)

# Elden Ring installation path
subprocess.Popen("C:\\Windows\\System32\\calc.exe")

print("Task Executed Successfully")
exit