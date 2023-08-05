import datetime


class Operations():

    def __init__(self, state, date1, description, to, amount, name, *from1):
        self.state = state
        self.date1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
        self.description = description
        self.from1 = from1[0]
        self.to = to
        self.amount = amount
        self.name = name

    def __repr__(self):
        return f"State ({self.state}), date1 ({self.date1}), description ({self.description}), from1 ({self.from1}), to ({self.to}), amount ({self.amount}), name)"


    def date_mirror(self):
        """
        перевод даты операции
        в формат ДД.ММ.ГГ
        """
        self.date1 = self.date1.strftime("%d.%m.%Y")
        return self.date1

    def is_state_correct(self):
        """
        проверка статуса операции
        """
        if self.state == "EXECUTED":
            return True

    def code_count_number(self):
        """
        кодирование номера карты
        """
        f = self.from1[:4]
        if self.from1 == "":
            self.from1 = ""
        else:
            if f == "Счет":
                s = self.from1[-20:]
                s1 = s[:4]
                s2 = s[5:7] + "** **** "
                s3 = s[-4:]
                s4 = self.from1[:-20]
            else:
                s = self.from1[-16:]
                s1 = s[:4]
                s2 = s[5:7] + "** "
                s3 = s[-4:]
                s4 = self.from1[:-16]
            self.from1 = s4 + s1 + " " + s2 + "**** " + s3
        return self.from1


    def build_answers(self):
        """
        вывод ответа пользователю
        """
        return f"{self.date1} {self.description} \n{self.from1} → Счет **{self.to} \n{self.amount} {self.name}"






