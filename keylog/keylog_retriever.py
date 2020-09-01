import shutil

save_path = 'C:/Intel/Lan/'
home_path = ':/keylog/'

try:
    shutil.move(save_path, 'D'+home_path)
except:
    try:
        shutil.move(save_path, 'E'+home_path)
    except:
        try:
            shutil.move(save_path, 'F'+home_path)
        except:
            try:
                shutil.move(save_path, 'G'+home_path)
            except:
                try:
                    shutil.move(save_path, 'H'+home_path)
                except:
                    try:
                        shutil.move(save_path, 'I'+home_path)
                    except:
                        try:
                            shutil.move(save_path, 'J'+home_path)
                        except:
                            print('error')

#shutil.rmtree(save_path)