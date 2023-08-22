import os
import re
import time
from typing import Callable

import pandas as pd

from render import Render


class PhoneBook:
    """Main class for phonebook"""

    def __init__(self):
        self.PER_PAGE: int = 50
        self.DB_PATH: str = os.path.join(os.path.dirname(__file__), 'db', 'db.csv')
        self.render = Render()

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self) -> None:
        """
        Display main menu of the program and handle user input
        """

        while True:
            self.clear_screen()
            self.render.main_menu()
            inpt: str = input('Введите номер желаемого пункта или X для выхода:\n').lower()
            match inpt:
                case "1":
                    self.get_records_list()
                case "2":
                    self.append_db()
                case "3":
                    self.search_record()
                case 'x' | 'х':
                    exit()
                case _:
                    print('Некорректный ввод, попробуйте еще раз')

            time.sleep(1)

    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate names"""

        return name.isalpha() and name

    @staticmethod
    def validate_number(number: str) -> bool:
        """Validate phone numbers"""

        return number.isdigit() and len(number) >= 6

    def get_validated_value(self, prompt: str, validator: Callable = None) -> str:
        """
        Validate the value according to passed validator.
        If no validator passed the value will be returned as is
        """

        while True:
            value: str = input(prompt)
            if value == 'back':
                self.main_menu()
            if validator:
                if validator(value):
                    return value.capitalize()
                else:
                    print('Некорректный ввод, попробуйте еще раз')
                    continue
            else:
                return value

    def display_records(self, records, page,  page_start, page_end, total_pages) -> None:
        """Display the records"""

        self.render.headers()
        for number, record in records.iloc[page_start:page_end].iterrows():
            last_name, name, patronymic, company, work_ph, private_ph = record
            self.render.record(number, last_name, name, patronymic, company, work_ph, private_ph)
        self.render.hor_delimiter()
        print(f'Страница {page} из {total_pages}\n\n')

    def get_records_list(self, page: int = 1):
        """
        Return a paginated list of records
        and handle user input
        """

        records: pd.DataFrame = self.read_db()
        total_pages: int = len(records) // self.PER_PAGE if not len(records) % self.PER_PAGE else len(
            records) // self.PER_PAGE + 1

        while True:
            self.clear_screen()

            page_start = (page - 1) * self.PER_PAGE
            page_end = page_start + self.PER_PAGE

            self.display_records(records, page, page_start, page_end, total_pages)

            temp: str = input(
                "Введите номер страницы для перехода к ней\n"
                "или\n"
                "edit {номер записи} для ее редактирования\n"
                "или\n"
                "X для возврата в гл. меню: "
            )

            if temp.lower() in ('x', 'х'):
                self.main_menu()
            elif len(e := temp.split()) == 2 and e[0] == 'edit' and e[1].isdigit() and 0 < int(e[1]) <= len(records):
                self.edit_record(int(e[1]))
            elif temp.isdigit() and 0 < int(temp) <= total_pages:
                page = int(temp)
            else:
                print('Некорректный ввод, попробуйте еще раз')
                time.sleep(2)

    @staticmethod
    def get_search_conditions() -> dict:
        """Form search conditions"""

        last_name = input("Введите фамилию (или оставьте пустым): ").lower()
        name = input("Введите имя (или оставьте пустым): ").lower()
        patronymic = input("Введите отчество (или оставьте пустым): ").lower()
        company = input("Введите название компании (или оставьте пустым): ").lower()
        work_ph = input("Введите рабочий телефон (или оставьте пустым): ").lower()
        private_ph = input("Введите личный телефон (или оставьте пустым): ").lower()

        return {
            'last_name': last_name,
            'name': name,
            'patronymic': patronymic,
            'company': company,
            'work_ph': work_ph,
            'private_ph': private_ph
        }

    @staticmethod
    def create_search_mask(records: pd.DataFrame, search_conditions: dict):
        """Creates search mask for records from passed dict"""

        return (
                records['last_name'].str.lower().str.contains(re.escape(search_conditions['last_name'])) &
                records['name'].str.lower().str.contains(re.escape(search_conditions['name'])) &
                records['patronymic'].str.lower().str.contains(re.escape(search_conditions['patronymic'])) &
                records['company'].str.lower().str.contains(re.escape(search_conditions['company'])) &
                records['work_ph'].astype(str).str.lower().str.contains(re.escape(search_conditions['work_ph'])) &
                records['private_ph'].astype(str).str.lower().str.contains(re.escape(search_conditions['private_ph']))
        )

    def search_record(self, page: int = 1) -> None:
        """Search records by one of several fields and render them"""

        self.clear_screen()

        records: pd.DataFrame = self.read_db()

        search_conditions = self.get_search_conditions()

        mask = self.create_search_mask(records, search_conditions)
        search_results = records[mask]

        while True:
            self.clear_screen()

            page_start = (page - 1) * self.PER_PAGE
            page_end = page_start + self.PER_PAGE

            total_pages: int = len(search_results) // self.PER_PAGE if not len(
                search_results) % self.PER_PAGE else len(search_results) // self.PER_PAGE + 1

            if not search_results.empty:
                self.display_records(search_results, page, page_start, page_end, total_pages)
            else:
                print("\nЗаписи не найдены")

            command: str = input(
                '\nВведите номер страницы для перехода к ней\n'
                'или\n'
                'Введите new для нового поиска\n'
                'или\n'
                'Х для возврата в гл. меню: '
            )

            if command.lower() in ('x', 'х'):
                self.main_menu()
            elif command.isdigit() and 0 < int(command) <= total_pages:
                page = int(command)
            elif command.lower() == 'new':
                self.search_record()
            else:
                print('Некорректный ввод попробуйте еще раз')
                time.sleep(2)

    def read_db(self) -> pd.DataFrame:
        """Read db.csv, returns a list of records"""

        try:
            return pd.read_csv(
                self.DB_PATH, sep='|', header=None,
                names=['last_name', 'name', 'patronymic', 'company', 'work_ph', 'private_ph']
            )
        except FileNotFoundError:
            self.clear_screen()
            print('База данных не найдена!')
            time.sleep(3)
            self.main_menu()
        except Exception as e:
            print(e)

    def sort_db(self) -> None:
        """Sort existing db.csv"""

        try:
            all_records: pd.DataFrame = self.read_db()
            sorted_db: pd.DataFrame = all_records.sort_values(
                by=['last_name', 'name', 'patronymic']
            )

            df_reset: pd.DataFrame = sorted_db.reset_index(drop=True)
            df_reset.index += 1

            df_reset.to_csv(self.DB_PATH, sep='|', index=True, header=False)
        except Exception as e:
            print(e)

    def append_db(self) -> None:
        """Append a new record to db.csv and sort the result"""

        df_new = pd.DataFrame(
            [self.set_record('добавлена')],
            columns=['last_name', 'name', 'patronymic', 'company', 'work_ph', 'private_ph']
        )
        df_new.to_csv(self.DB_PATH, index=True, header=False, mode='a', sep='|')
        self.sort_db()

    def set_record(self, s: str) -> list[str]:
        """Form the record as a list"""

        self.clear_screen()

        print('Для возврата в гл. меню введите back в любое поле\n')

        last_name: str = self.get_validated_value(
            'Введите фамилию (только буквы): ', self.validate_name
        )
        name: str = self.get_validated_value(
            'Введите имя (только буквы): ', self.validate_name
        )
        patronymic: str = self.get_validated_value(
            'Введите отчество (только буквы): ',
            self.validate_name
        )
        company: str = self.get_validated_value('Введите название компании: ')
        work_ph: str = self.get_validated_value(
            'Введите рабочий телефон (только цифры, не меньше 6): ',
            self.validate_number
        )
        personal_ph: str = self.get_validated_value(
            'Введите личный телефон (только цифры, не меньше 6): ',
            self.validate_number
        )

        print(f'\nЗапись {s}...')
        time.sleep(1)

        return [last_name, name, patronymic, company, work_ph, personal_ph]

    def edit_record(self, to_edit: int) -> None:
        """Edit the specific record"""

        records: pd.DataFrame = self.read_db()

        try:
            edited_record: list = self.set_record('изменена')
            records.iloc[to_edit-1] = edited_record
            records.to_csv(self.DB_PATH, index=True, sep='|', header=False)

            self.sort_db()

        except Exception as e:
            print(e)

        self.main_menu()

