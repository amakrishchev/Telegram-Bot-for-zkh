from enum import Enum

# token = '455123093:AAGkYKpxITvziH1jWKjJrJLVLDRxAMk35oI'
#token = '509245030:AAFt4GxhX9LXer1wHsO-aPtnz1LtLlXBY1A'

db_file = "database.vdb"

jokes = ['Стесняюсь спросить: управляющие компании - так они нас обслуживают или они нами управляют?',
         'Две недели можно и в холодной воде помыться. Нежные какие, блин, нашлись. '
         'Детей и жену уже приучил.Сам пока для себя грею.',
         'А Путину летом тоже воду отключают?',
         'Сегодня видел парня лет 18-ти, который во дворе долбил лёд. '
         'А на спине у него распечатка: "Я не дворник. Меня просто задолбало здесь падать".',
         'Если вы, бессовестные, вовремя не оплатили ЖКУ, то они не могут вовремя украсть.',
         'Как птица гриф \n взлетел тариф.\n А пояснять вам, люди, надо ль \n какую ждет стервятник падаль?',
         'Тариф на холодную воду повышен для новосибирцев на 20 %, на горячую воду '
         '— на 15,9 %, на водоотведение — на 20,1 %, на отопление — на 14,9 %. '
         'Руководитель департамента по тарифам НСО Гарей Асмодьяров '
         'в качестве причины повышения тарифов назвал излишнюю экономность горожан.',
         'Декабрь 2009 г. Ростов-на-Дону, число не помню,но в народе этот день назвали белый четверг. '
         'Неожиданно зимой выпал снег, выпало много снега (что для Ростова редкость). '
         'И как следствие транспортный коллапс и прочие сопутствующие радости. '
         'На сайте местных новостей торжественно сообщили, что Администрацией приобретено '
         '800 единиц снегоуборочной техники. В 2010 г. в декабре, как ни удивительно,снег выпал опять. '
         'Отсутствие снегоуборочной техники на улицах города объяснялось, тем что в этом году забыли '
         'выделить деньги на заправку этой техники и зарплату водителям. '
         'Потом всё кануло в небытие. Жаль, что не догадалась, хотя бы на память, скриншот сделать.',
         ]


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    SET_NAME = "1"   # Приветствие, запись имени
    MENU = '2'
    WATER = '3'         # Подменю ВОДА
    PAY = '100'
    COST_W = '3.1'
    PROBLEM_W = '3.2'
    BROKEN_PIPE = '3.2.1'
    NO_W = '3.2.2'
    NO_HW = '3.2.3'
    OTHER_W = '3.2.4'
    ELECTR = '4'           # Подменю ЭЛЕКТРИЧЕСТВО
    COST_E = '4.1'
    PROBLEM_E = '4.2'
    NO_E = '4.2.1'
    WIRE = '4.2.2'
    OTHER_E = '4.2.3'
    GAS = '5'               # Подменю ГАЗ
    COST_G = '5.1'
    PROBLEM_G = '5.2'
    LEAK = '5.2.1'
    NO_G = '5.2.2'
    HTN = '5.2.3'
    OTHER_G = '5.2.4'
    OTHER = '6'             # Подменю ДРУГОЕ
    JOKES = '6.1'
    GRADE = '6.2'
    SHARE_NUM = '99'      # Поделиться номером телефона




# S_ENTER_AGE = "2"
# S_SEND_PIC = "3"
