
         _____  _                      ____              _
        |  __ \| |                    |  _ \            | |
        | |__) | |__   ___  _ __   ___| |_) | ___   ___ | | __
        |  ___/| '_ \ / _ \| '_ \ / _ \  _ < / _ \ / _ \| |/ /
        | |    | | | | (_) | | | |  __/ |_) | (_) | (_) |   <
        |_|    |_| |_|\___/|_| |_|\___|____/ \___/ \___/|_|\_\
                                            by OneHandedPirate

<hr>
Простое приложение командной строки, имитирующее телефонную книгу.


### Особенности:

- Главное меню для удобной навигации
- Добавление новых записей
- Редактирование существующих записей
- Поиск контактов по разным полям
- Пагинация для отображения записей

### Структура:

```
├── db
│   └── db.csv
├── __init__.py
├── form_db.py
├── phonebook.py
├── main.py
└── render.py
```
* `db.csv` - cодержит данные "базы данных" (100_000 записей).
* `form_db.py` - код для форматирования "базы данных" из случайных комбинаций полей. Содержит переменную `RECORDS_NUMBER`, определяющую количество записей.
* `phonebook.py` - содержит класс `PhoneBook` для управления записями телефонной книги.
* `main.py` - главный код для запуска приложения.
* `render.py` - содержит вспомогательный класс Render, который реализует методы для визуального отображения элементов интерфейса.

### Установка:

- стянуть репо и перейти в папку `PhoneBook`:<br>
  `git clone https://github.com/OneHandedPirate/PhoneBook.git` <br>
  `cd PhoneBook`
- Если вы используете `poetry`:
  - активировать виртуальное окружение `poetry`:<br>
    `poetry shell`
  - установить зависимости:<br>
    `poetry install --without dev`
- Если вы не используете `poetry`:
  - создайте виртуальное окружение:<br>
    `virtualenv venv`
  - активируйте его:
    - Linux/Mas:
    `source venv/bin/activate`
    - Windows:
    `.\venv\Scripts\activate`
  - установите зависимости:<br>
    `pip install -r requirements.txt`

### Запуск:

- из папки `PhoneBook/app` выполнить команду `python3 main.py`

### Особенности:

- лучше запускать непосредственно из терминала (а не из IDE), тогда экран будет корректно очищаться.
- изменить количество записей на странице (как в выводе справочника, так и в поиске) можно изменив переменную `PER_PAGE` в классе `PhoneBook` в `phonebook.py`.
- после добавления/изменения записи `db.csv` автоматически сортируется.
- поиск не регистрозависим, можно ввести часть поискового параметра.

### Использование:

- На каждом экране есть подсказки, просто следуйте им.

### Скриншоты:

1. Главное меню:<br>
![menu.png](images%2Fmenu.png)


2. Постраничный вывод записей:<br>
![records.png](images%2Frecords.png)


3. Добавление/изменение записей (единый интерфейс):<br>
![add_edit.png](images%2Fadd_edit.png)


4. Интерфейс поиска:<br>
![search.png](images%2Fsearch.png)


5. Результраты поиска:<br>
![search_results.png](images%2Fsearch_results.png)
