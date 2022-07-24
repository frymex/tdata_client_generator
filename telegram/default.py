import os
import platform


class Types:
    WARN = 'WARN'
    LOG_TEXT = 'LOG'
    ERROR = 'ERROR'
    FAIL = 'FAIL'


class Models:
    log_context = '[{0}] -> {1} <- [{0}]'


def default_config(err_type: Types, text: str):
    return Models.log_context.format(err_type, text)


def return_log(err_type: Types, text: str, exit_on_complete=None) -> None:
    print(Models.log_context.format(err_type, text))
    if exit_on_complete:
        exit()


def clear_console(os_type='Find') -> None:
    if os_type == 'Windows':
        os.system('cls')
    elif os_type == 'Linux':
        os.system('clear')
    elif os_type == 'Find':
        os_type = platform.system()
        clear_console(os_type)
