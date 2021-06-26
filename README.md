# Инструкция
Для сборки исполняемого файла небходимо установить pyinstaller:
`pip install pyinstaller`.

Далее для непосредственной сборки (на примере данного проекта) можно использовать следующую команду:
`sudo pyinstaller --add-data "pyinstaller_example/example.txt:." --windowed --noconfirm --clean -n Example  pyinstaller_example/__main__.py`.
Флаг `--add-data` добавляет файлы как ресурсы в pyinstaller (`source:dest`), для их дальнейшего нахождения уже в собранном
виде можно использовать следующую функцию (relative_path - относительный путь к ресурсу, такой же как и `dest`):
```
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)
```
Флаг `-n` задает имя для собираемой программы. Флаг `--windowed` означает создание в случае
macOS пакета программы формата `.app`.

Также можно сначала создать spec-файл: `pyi-makespec name.py`. Затем уже в созданном
spec-файле изменить все нужные вам параметры. Далее для сборки уже необходимо использовать
следующую команду `pyinstaller name.spec`.

Существует ещё один способ организации сборки - через скрипт. Пример скрипта:
```
#!/usr/bin/env python

from PyInstaller.__main__ import run as pyinstall_run

pyinstall_run([
    'pyinstaller_example/__main__.py',
    '--windowed',
    '--noconfirm',
    '--clean',
    '--add-data',
    'pyinstaller_example/example.txt:.'
    '-n Example',
])

```

# Полезные ссылки
- https://pythonru.com/biblioteki/pyinstaller
- https://realpython.com/pyinstaller-python/
- https://pyinstaller.readthedocs.io/en/stable/usage.html 