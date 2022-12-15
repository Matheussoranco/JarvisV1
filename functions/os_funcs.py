import os
import subprocess as subp

paths = {
    'notepad': "/usr/bin/gnote",
    'firefox': "/snap/bin/firefox",
    'Thuderbird':"/usr/bin/thunderbird",
    'Discord':"/snap/bin/discord",
    'spotify':"/snap/bin/spotify",
    'Visual Studio Code':"/snap/bin/code"
}

def open_notepad():
    os.startfile(paths['notepad'])


def open_firefox():
    os.startfile(paths['firefox'])


def open_discord():
    os.startfile(paths['Discord'])


def open_Thunderbird():
    os.startfile(paths['Thuderbird'])


def open_spotify():
    os.startfile(paths['spotify'])


def open_VSCode():
    os.startfile(paths['Visual Studio Code'])


def open_terminal():
    os.system('start terminal')