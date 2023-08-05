import json
from operator import itemgetter
from class_functions import Operations


print("Добрый день, уважаемый клиент!\nНа экране 5 последних проведенных транзакицй!")  #старт обслуживания
print("")

with open('operations.json', 'rt', encoding="utf8") as file:   # импорт данных из файла
    operations_data = json.load(file)
    operations_sorted = sorted(operations_data, key=itemgetter('date'), reverse=True) #сортировка списка по дате

operations=[]
for item in operations_sorted: # создание экземпляров класса
    operations.append(Operations(item["state"], item["date"][:10], item["description"], item["to"][-4:], item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"], item["from"] if item.get("from") else""))


d=1
for data in operations:
    if data.is_state_correct() == True: # проверка статуса операции
        if d <=5:                       # ограничение первых 5 операций
            data.date_mirror()          # изменение формата даты
            data.code_count_number()    # форматирование номера карты (счета)
            print(data.build_answers()) # вывод отчета по операциям в определенном формате
            print("")
            d += 1


print("Хорошего дня!")
