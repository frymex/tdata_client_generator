import os, requests, default
from tqdm import tqdm
import zipfile


class AppConfig:
    FilesUrls = [
        'https://telegram.org/dl/desktop/win64_portable',
        'url_of_tdata'
    ]


def is_availability(file: str, path='./'):
    if file in os.listdir(path):
        return False
    else:
        return True


def create_dir(dir_name, path='./'):
    if is_availability(dir_name, path):
        os.mkdir('{0}{1}'.format(path, dir_name))


def delete_file(path):
    os.remove(path)


def config_dir(path='../', os_type='win64', tdata_url: str = ''):
    create_dir('tg_bin', path)
    if os_type == 'win64':
        AppConfig.FilesUrls[0] = 'https://telegram.org/dl/desktop/win64_portable'
    elif os_type == 'win32':
        AppConfig.FilesUrls[0] = 'https://telegram.org/dl/desktop/win_portable'
    elif os_type == 'linux':
        default.clear_console()
        default.return_log(default.Types.ERROR, 'Ошибка.', True)

    AppConfig.FilesUrls[1] = tdata_url


def get_and_unpack():
    default.return_log(default.Types.LOG_TEXT, 'Устанавливаем файлы. Ожидайте')

    for idx, u in enumerate(AppConfig.FilesUrls):
        try:
            if idx == 0:
                if is_availability('tg.zip', '../tg_bin'):
                    response = requests.get(u, stream=True)
                    total_size_in_bytes = int(response.headers.get('content-length', 0))
                    block_size = 1024
                    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                    if idx == 0:
                        with open('../tg_bin/tg.zip', 'wb') as file:
                            for data in response.iter_content(block_size):
                                progress_bar.set_description("Downloading")

                                progress_bar.update(len(data))
                                file.write(data)
                        progress_bar.close()

            elif idx == 1:
                if is_availability('tdata.zip', '../tg_bin'):

                    response = requests.get(u, stream=True)
                    total_size_in_bytes = int(response.headers.get('content-length', 0))
                    block_size = 1024
                    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                    if idx == 0:
                        with open('../tg_bin/tdata.zip', 'wb') as file:
                            for data in response.iter_content(block_size):
                                progress_bar.set_description("Downloading")

                                progress_bar.update(len(data))
                                file.write(data)
                        progress_bar.close()

        except requests.exceptions.MissingSchema:
            if idx == 0:
                pass

            default.return_log(default.Types.ERROR, 'Некоректный запрос к API')

    create_dir(r'telegram_app', r'../tg_bin/')

    un_pack(r'../tg_bin/tg.zip', r'../tg_bin/telegram_app/')
    delete_file(r'../tg_bin/tg.zip')

    if not is_availability('tdata.zip', '../tg_bin/'):
        un_pack('../tg_bin/tdata.zip', '../tg_bin/telegram_app/')
    else:
        default.return_log(default.Types.ERROR, 'Файл с TDATA недоступен. Проверьте URL который вы указали', True)


def un_pack(path, to, pwd=None):
    with zipfile.ZipFile(f"{path}", "r") as zip_ref:
        zip_ref.extractall(f"{to}", pwd=pwd)


config_dir(tdata_url=input('Enter link of TDATA [mustb by .zip]: '))
get_and_unpack()
