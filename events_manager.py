import subprocess
import os
import codecs
from parser_dates import *
from parser_toponyms import ParserToponym
from parser_persons import ParserPerson


class TomitaManager:
    def __init__(self, session_name='default', path_to_tomita='./tomita/'):
        self.__path_to_tomita = os.path.abspath(path_to_tomita)
        self.__date_config = 'encoding "utf8";' \
                             'TTextMinerConfig {' \
                             '    Dictionary = "dic.gzt";' \
                             '    Input = {File =  "date.txt" }' \
                             '    Output = {File = "date.xml" }' \
                             '    Articles = [' \
                             '        {Name = "дата"}' \
                             '    ]' \
                             '    Facts = [' \
                             '        {Name = "Date"}' \
                             '    ]' \
                             '}'
        self.__toponym_config = 'encoding "utf8";' \
                                'TTextMinerConfig {' \
                                '    Dictionary = "dic.gzt";' \
                                '    Input = {File =  "toponym.txt" }' \
                                '    Output = {File = "toponym.xml" }' \
                                '    Articles = [' \
                                '        {Name = "топоним"}' \
                                '    ]' \
                                '    Facts = [' \
                                '        {Name = "Toponym"}' \
                                '    ]' \
                                '}'
        self.__fio_config = 'encoding "utf8";' \
                            'TTextMinerConfig {' \
                            '    Dictionary = "dic.gzt";' \
                            '    Input = {File =  "fio.txt" }' \
                            '    Output = {File = "fio.xml" }' \
                            '    Articles = [' \
                            '        {Name = "фио"}' \
                            '    ]' \
                            '    Facts = [' \
                            '        {Name = "FIO"}' \
                            '    ]' \
                            '}'
        self.__events = []

    def extract_date_and_sentence(self, text):
        f = codecs.open(self.__path_to_tomita + '\\date.txt', 'w', 'utf-8')
        f.write(text)
        f.close()

        f = codecs.open(self.__path_to_tomita + '\\date.proto', 'w', 'utf-8')
        f.write(self.__date_config)
        f.close()

        subprocess.Popen([self.__path_to_tomita + '\\' + 'tomitaparser.exe',
                          'date.proto'], cwd=self.__path_to_tomita).wait()

        parser = ParserWikiDate(self.__path_to_tomita + '\\date.xml')

        return parser.get_events()

    def extract_toponym(self, text):
        f = codecs.open(self.__path_to_tomita + '\\toponym.txt', 'w', 'utf-8')
        f.write(text)
        f.close()

        f = codecs.open(self.__path_to_tomita + '\\toponym.proto', 'w', 'utf-8')
        f.write(self.__toponym_config)
        f.close()

        subprocess.Popen([self.__path_to_tomita + '\\' + 'tomitaparser.exe',
                          'toponym.proto'], cwd=self.__path_to_tomita).wait()

        parser = ParserToponym(self.__path_to_tomita + '\\toponym.xml')
        toponyms = parser.get_toponyms()
        tops = []
        for t in toponyms:
            if t not in tops:
                tops.append(t)
        return tops

    def extract_person(self, text):
        f = codecs.open(self.__path_to_tomita + '\\fio.txt', 'w', 'utf-8')
        f.write(text)
        f.close()

        f = codecs.open(self.__path_to_tomita + '\\fio.proto', 'w', 'utf-8')
        f.write(self.__fio_config)
        f.close()

        subprocess.Popen([self.__path_to_tomita + '\\' + 'tomitaparser.exe',
                          'fio.proto'], cwd=self.__path_to_tomita).wait()

        parser = ParserPerson(self.__path_to_tomita + '\\fio.xml')
        return parser.get_persons()

    def extract_events_from_article(self, text, clear=True):
        self.__events = self.extract_date_and_sentence(text)
        for event in self.__events:
            event.toponyms = self.extract_toponym(event.sentence)
            event.persons = self.extract_person(event.sentence)

        if clear:
            os.remove(self.__path_to_tomita + '\\date.txt')
            os.remove(self.__path_to_tomita + '\\date.proto')
            os.remove(self.__path_to_tomita + '\\date.xml')
            if os.path.exists(self.__path_to_tomita + '\\toponym.proto'):
                os.remove(self.__path_to_tomita + '\\toponym.txt')
                os.remove(self.__path_to_tomita + '\\toponym.proto')
                os.remove(self.__path_to_tomita + '\\toponym.xml')
            if os.path.exists(self.__path_to_tomita + '\\fio.proto'):
                os.remove(self.__path_to_tomita + '\\fio.txt')
                os.remove(self.__path_to_tomita + '\\fio.proto')
                os.remove(self.__path_to_tomita + '\\fio.xml')

        return self.__events


if __name__ == '__main__':
    tm = TomitaManager()
    events = tm.extract_events_from_article(
        "В 1385 году великий князь литовский Ягайло в соответствии с Кревской унией обязался присоединить Великое "
        "княжество Литовское к Королевству Польскому и становился королём Польши. В декабре 1926 года в Литве "
        "произошёл военный переворот, возглавивший его лидер националистической партии Антанас Смятона установил "
        "авторитарный режим. 22   июня   1941   года   , после нападения Германии на СССР, последовали антисоветские "
        "мятежи   в   Литве. 22 марта 1939 года гитлеровская Германия предъявила Литве ультиматум с требованием "
        "вернуть ей Мемельланд, который Литва была вынуждена принять. ")
    for event in events:
        print(event)
