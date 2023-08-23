from random import choice, choices
from string import digits

import pandas as pd

RECORDS_NUMBER: int = 100000

numbers: str = digits

names: list = [
    'Александр', 'Алексей', 'Анатолий', 'Андрей', 'Антон', 'Аркадий', 'Арсений', 'Артём',
    'Борис', 'Вадим', 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир',
    'Владислав', 'Вячеслав', 'Геннадий', 'Георгий', 'Глеб', 'Григорий', 'Даниил', 'Денис',
    'Дмитрий', 'Евгений', 'Егор', 'Иван', 'Игорь', 'Илья', 'Кирилл', 'Константин', 'Лев',
    'Леонид', 'Максим', 'Марат', 'Марк', 'Матвей', 'Михаил', 'Никита', 'Николай', 'Олег',
    'Павел', 'Пётр', 'Роман', 'Руслан', 'Сергей', 'Станислав', 'Степан', 'Тимур', 'Тихон',
    'Фёдор', 'Юрий', 'Ярослав', 'Алексей', 'Анатолий', 'Андрей', 'Антон', 'Аркадий', 'Арсений',
    'Артём', 'Борис', 'Вадим', 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир',
    'Владислав', 'Вячеслав', 'Геннадий', 'Георгий', 'Глеб', 'Григорий', 'Даниил', 'Денис', 'Дмитрий',
    'Евгений', 'Егор', 'Иван', 'Игорь', 'Илья', 'Кирилл', 'Константин', 'Лев', 'Леонид', 'Максим',
    'Марат', 'Марк', 'Матвей', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Пётр', 'Роман', 'Руслан',
    'Сергей', 'Станислав', 'Степан', 'Тимур', 'Тихон', 'Фёдор', 'Юрий', 'Ярослав'
]

surnames: list = [
    'Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Соколов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов',
    'Петров', 'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Голубев', 'Виноградов',
    'Богданов', 'Воробьёв', 'Фёдоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов',
    'Киселёв', 'Макаров', 'Андреев', 'Ковалёв', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов',
    'Куликов', 'Алексеев', 'Степанов', 'Яковлев', 'Сорокин', 'Сергеев', 'Романов', 'Захаров', 'Борисов',
    'Королёв', 'Герасимов', 'Пономарёв', 'Григорьев', 'Лазарев', 'Медведев', 'Ершов', 'Никитин', 'Соболев',
    'Рябов', 'Поляков', 'Цветков', 'Данилов', 'Жуков', 'Фролов', 'Журавлев', 'Николаев', 'Крылов', 'Максимов',
    'Сидоров', 'Осипов', 'Белоусов', 'Федотов', 'Дорофеев', 'Егоров', 'Матвеев', 'Бобров', 'Дмитриев', 'Калинин',
    'Анисимов', 'Петухов', 'Антонов', 'Тимофеев', 'Никифоров', 'Веселов', 'Филиппов', 'Марков', 'Большаков', 'Суханов',
    'Миронов', 'Ширяев', 'Александров', 'Коновалов', 'Шестаков', 'Казаков', 'Ефимов', 'Денисов', 'Громов', 'Фомин',
    'Давыдов', 'Мельников', 'Щербаков', 'Блинов', 'Колесников'
]

patronymics: list = [
    'Александрович', 'Алексеевич', 'Анатольевич', 'Андреевич', 'Антонович', 'Аркадьевич', 'Арсеньевич', 'Артёмович',
    'Борисович', 'Вадимович', 'Валентинович', 'Валерьевич', 'Васильевич', 'Викторович', 'Витальевич', 'Владимирович',
    'Владиславович', 'Вячеславович', 'Геннадьевич', 'Георгиевич', 'Глебович', 'Григорьевич', 'Даниилович', 'Денисович',
    'Дмитриевич', 'Евгеньевич', 'Егорович', 'Иванович', 'Игоревич', 'Ильич', 'Кириллович', 'Константинович', 'Львович',
    'Леонидович', 'Максимович', 'Маратович', 'Маркович', 'Матвеевич', 'Михайлович', 'Никитич', 'Николаевич', 'Олегович',
    'Павлович', 'Петрович', 'Романович', 'Русланович', 'Сергеевич', 'Станиславович', 'Степанович', 'Тимурович',
    'Тихонович', 'Фёдорович', 'Юрьевич', 'Ярославович', 'Алексеевич', 'Анатольевич', 'Андреевич', 'Антонович',
    'Аркадьевич', 'Арсеньевич', 'Артёмович', 'Борисович', 'Вадимович', 'Валентинович', 'Валерьевич', 'Васильевич',
    'Викторович', 'Витальевич', 'Владимирович', 'Владиславович', 'Вячеславович', 'Геннадьевич', 'Георгиевич',
    'Глебович', 'Григорьевич', 'Даниилович', 'Денисович', 'Дмитриевич', 'Евгеньевич', 'Егорович', 'Иванович',
    'Игоревич', 'Ильич', 'Кириллович', 'Константинович', 'Львович', 'Леонидович', 'Максимович', 'Маратович',
    'Маркович', 'Матвеевич', 'Михайлович', 'Никитич', 'Николаевич', 'Олегович', 'Павлович', 'Петрович', 'Романович',
    'Русланович', 'Сергеевич', 'Станиславович', 'Степанович', 'Тимурович', 'Тихонович', 'Фёдорович', 'Юрьевич',
    'Ярославович'
]

companies: list = [
    'АО Новые Технологии', 'АО ТехноПром', 'АО ТехноСтрой', 'АО Технодизайн', 'АО УралТех', 'ЗАО АвтоТех',
    'ЗАО Альфастрой', 'ЗАО Интегра', 'ЗАО ПромСтрой', 'ЗАО ПромТех', 'ЗАО Промстрой', 'ЗАО Русский Металл',
    'ЗАО ЭкоСтрой', 'ЗАО Экострой', 'ЗАО ЭлектроСервис', 'ОАО Инновационные Решения', 'ОАО Интегра',
    'ОАО ИнтерСтрой', 'ОАО Интерком', 'ОАО МегаСтрой', 'ОАО ПромТех', 'ОАО Росстаткрайтелеком',
    'ОАО СтройЭнерго', 'ОАО ТехноСтрой', 'ОАО ЮниверсалСтрой', 'ООО АвтоСервис', 'ООО АвтоТранс',
    'ООО Инновационные Решения', 'ООО ИнтерСтрой', 'ООО ПромИнжиниринг', 'ООО Русский Металл', 'ООО СтройПроект',
    'ООО СтройЭнерго', 'ООО Стройгазинвест', 'ООО ЭнергоПром', 'ООО ЭнергоСтрой', 'ООО Энергопром'
]


def generate_random_record() -> list[str]:
    return [
        choice(surnames), choice(names), choice(patronymics), choice(companies),
        ''.join(choices(numbers, k=9)), ''.join(choices(numbers, k=9))
    ]


csv_file: str = 'db/db.csv'
data: list = [generate_random_record() for _ in range(RECORDS_NUMBER)]
df: pd.DataFrame = pd.DataFrame(data, columns=['last_name', 'name', 'patronymic', 'company', 'work_ph', 'private_ph'])
sorted_df: pd.DataFrame = df.sort_values(by=['last_name', 'name', 'patronymic'])

df_reset: pd.DataFrame = sorted_df.reset_index(drop=True)
df_reset.index += 1

df_reset.to_csv(csv_file, index=True, sep='|', header=False)
