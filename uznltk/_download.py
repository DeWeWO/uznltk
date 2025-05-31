import os
import sys
import requests
import zipfile
import io
import shutil

USERNAME = 'DeWeWO'
REPO = 'uznltk_data'
BRANCH = 'master'
RAW_URL = f'https://raw.githubusercontent.com/{USERNAME}/{REPO}/{BRANCH}/'

exe_path = os.path.abspath(sys.executable)
exe_dir = os.path.dirname(exe_path)
dirs_up = exe_dir.split(os.sep)

# 'AppData' papkasining joylashgan joyini topamiz (misol uchun)
if 'AppData' in dirs_up:
    appdata_index = dirs_up.index('AppData')
    roaming_path = os.sep.join(dirs_up[:appdata_index + 2])
else:
    roaming_path = os.path.expanduser('~\\AppData\\Roaming')

CORPORA_PATH = os.path.join(roaming_path, 'corpora')

def download(name):
    if not name:
        return

    file_url = RAW_URL + name + '.txt'
    r = requests.get(file_url)

    if r.status_code == 200:
        download_file(name + '.txt', r.text)
    else:
        download_folder(name)

def download_file(file_name, content):
    file_path = os.path.join(CORPORA_PATH, file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"The file named {file_name} was downloaded.")

def download_folder(name):
    zip_url = f'https://github.com/{USERNAME}/{REPO}/archive/refs/heads/{BRANCH}.zip'

    r = requests.get(zip_url)
    if r.status_code != 200:
        print("The ZIP could not be downloaded.")
        return

    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        top_folder = f"{REPO}-{BRANCH}/"
        target_folder = top_folder + name + '/'

        names = [f for f in z.namelist() if f.startswith(target_folder)]

        if not names:
            print(f"Folder not found {name}")
            return

        for file in names:
            if file.endswith('/'):
                continue
            extracted_path = os.path.join(CORPORA_PATH, file.replace(top_folder, ''))
            os.makedirs(os.path.dirname(extracted_path), exist_ok=True)
            with z.open(file) as src, open(extracted_path, 'wb') as out:
                shutil.copyfileobj(src, out)
        print(f"The folder named {name} has been downloaded.")
