home = C:\Users\hp\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0
implementation = CPython
version_info = 3.13.3.final.0
virtualenv = 20.24.5
include-system-site-packages = false
version = 3.13.3
executable = C:\Users\hp\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe
command = C:\Users\hp\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe -m venv --without-pip --without-scm-ignore-files C:\Users\hp\Desktop\uznltk\uznltk\.venv
eturn

    try:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            main_dir = z.namelist()[0].split('/')[0]
            extract_path = f"{main_dir}/{folder_name}"
            found = False
            extract_to = f"temp_extract_{folder_name}"

            if os.path.exists(extract_to):
                shutil.rmtree(extract_to)
            os.makedirs(extract_to)

            for file in z.namelist():
                if file.startswith(extract_path + "/") and not file.endswith("/"):
                    found = True
                    z.extract(file, extract_to)

            if not found:
                print(f"'{folder_name}' papkasi topilmadi.")
                shutil.rmtree(extract_to)
                return

            if not os.path.exists("Manba"):
                os.makedirs("Manba")

            final_path = os.path.join("Manba", folder_name)
            if os.path.exists(final_path):
                shutil.rmtree(final_path)
            shutil.move(os.path.join(extract_to, main_dir, folder_name), final_path)
            shutil.rmtree(extract_to)
            print(f"'{folder_name}' papkasi 'Manba/' ichiga muvaffaqiyatli yuklandi.")

    except zipfile.BadZipFile:
        print("ZIP faylni ochishda xatolik.")
    except Exception as e:
        print(f"Faylni ajratishda xatolik: {e}")

def book_download():
    download_folder("Uzb_kitoblar")

def news_download():
    download_folder("Yangiliklar")
