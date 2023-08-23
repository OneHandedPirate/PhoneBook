class Render:
    """
    Class for rendering different elements for PhoneBook class
    """

    @staticmethod
    def main_menu() -> None:
        """Render main menu"""

        res: str = """
         \033[92m_____  _                      ____              _
        |  __ \\| |                    |  _ \\            | |
        | |__) | |__   ___  _ __   ___| |_) | ___   ___ | | __
        |  ___/| '_ \\ / _ \\| '_ \\ / _ \\  _ < / _ \\ / _ \\| |/ /
        | |    | | | | (_) | | | |  __/ |_) | (_) | (_) |   <
        |_|    |_| |_|\\___/|_| |_|\\___|____/ \\___/ \\___/|_|\\_\\ \033[0m

                                        \033[96mby OneHandedPirate \033[0m

            **********************************************
            *                                            *
            *            \033[93m1\033[0m. Справочник                   *
            *            \033[93m2\033[0m. Добавить запись              *
            *            \033[93m3\033[0m. Поиск                        *
            *                                            *
            **********************************************
        """
        print(res)

    @staticmethod
    def headers() -> None:
        """Render table headers"""

        print(
            f' {"_" * 135} \n'
            '|     №     |       Фамилия       |       Имя       |      Отчество    '
            '|           Компания         |   Телефон(раб.)  | Телефон(личн.) |'
        )

    @staticmethod
    def record(
            number: int, last_name: str, name: str, patronymic: str,
            company: str, work_ph: str, private_ph: str
    ) -> None:
        """Render single row of the table"""

        print(
            f' {"_" * 135} \n'
            f'| {number:^9} | {last_name:<19} | {name:<15} | {patronymic:<16} | '
            f'{company:<26} | {work_ph:<16} | {private_ph:<14} |'
        )

    @staticmethod
    def hor_delimiter() -> None:
        """Render a horizontal delimiter"""

        print(f' {"_" * 135} ')
