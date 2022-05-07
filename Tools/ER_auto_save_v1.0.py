import shutil
import subprocess
import os

# src = steam save file path
# dest = local backup path
save_file_src = r"C:\Path\to\original save file"
save_file_dest = r"C:\Path\to\copied save file"

shutil.copytree(save_file_src, save_file_dest, dirs_exist_ok=True)

# Elden Ring installation path
subprocess.Popen("C:\\Path\\To\\Elden Ring.exe")
