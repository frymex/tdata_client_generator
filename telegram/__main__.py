import os
import time
import platform
import default
import argparse


os.system('echo ------ Soft by CAZQEV ------')
time.sleep(0.5)
os.system('echo ------ Version 1.0 ------')
os.system('@echo off')
time.sleep(5.5)

default.clear_console()

if platform.system() == 'Windows':
    default.return_log(default.Types.FAIL, 'К сожалению софт работает только на WINDOWS', True)

default.return_log(default.Types.LOG_TEXT, 'Скачивание програм, настройка конфига', True)
