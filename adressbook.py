# -*- coding: utf-8 -*-
import json
import time,sys

# initialize
print("------Справочник 0.01a------")
# db_directory = "/storage/emulated/0/Download/AdressBook_PY-master/AdressBook_PY-master/db.txt"  # linux
db_directory = "db.txt"  # win
# db_temp = "E:\\Book\\Win\\db_temp.txt"  # win
db = {}


def init():
    global db
    with open(db_directory, "r+") as f:
        content = str(f.read())
        f.seek(0)
        if not (len(content) == 0):
            json1_data = json.loads(content)
            db = json1_data
            print('\x1b[6;30;42m' + "@LOG: " + str(db) + '\x1b[0m')


def add():
    global db
    dct = {}
    init()
    surname = ""
    while len(surname) == 0:
        print("Введите фамилию")
        surname = input()
    dct["surname"] = surname

    name = ""
    while len(name) == 0:
        print("Введите имя")
        name = input()
    dct["name"] = name

    second_name = ""
    print("Введите отчество")
    second_name = input()
    dct["second_name"] = second_name

    phone_number = "0"
    # TODO check for digits
    while not (len(phone_number) == 11 or len(phone_number) == 6):
        print("Введите домашний номер")
        phone_number = input()
    dct["telephone"] = int(phone_number)

    number = "0"
    # TODO check for digits
    while not len(number) == 11:
        print("Введите сотовый номер")
        number = input()
    dct["number"] = int(number)

    city = ""
    while len(city) == 0:
        print("Введите город")
        city = input()
    dct["city"] = city

    street = ""
    while len(street) == 0:
        print("Введите улицу")
        street = input()
    dct["street"] = street

    house = ""
    # TODO check for digits
    while len(house) == 0:
        print("Введите номер дома")
        house = input()
    dct["house"] = int(house)

    print("Введите номер квартиры")
    room = input()
    dct["room"] = room

    f = open(db_directory, "r+")
    # init()
    print('\x1b[6;30;42m' + "@LOG: " + "@LOG: " + str(db) + '\x1b[0m')
    if "contact" in db.keys():
        db["contact"].append(dct)
    else:
        db["contact"] = [dct]

    # db["contact"]=dct
    print('\x1b[6;30;42m' + "@LOG: " + "@LOG: " + str(db) + '\x1b[0m')

    temp = str(db)
    str_dct = temp.replace("\'", "\"")
    f.write(str_dct)
    # f.write(str(db))
    # f.write((str(dct)+",").encode())
    f.close()


def removeJson(index):
    global db
    init()
    #print(db["contact"])
    db["contact"].pop(index - 1)

    f = open(db_directory, "r+")
    f.seek(0)
    f.truncate()
    temp = str(db)
    str_dct = temp.replace("\'", "\"")
    f.write(str_dct)
    f.close()
    #print(db["contact"])


def editJson(index, element):
    global db
    init()
    #print(db["contact"])

    #print("EDIT")

    print("===Введите новое значение===")
    if (element < 6):
        inp = input()
    else:
        inp = int(input())

    if element == 1:
        print("1-фамилия")
        db["contact"][index - 1]["surname"] = inp
    if element == 2:
        print("2-имя")
        db["contact"][index - 1]["name"] = inp
    if element == 3:
        print("3-отчество")
        db["contact"][index - 1]["second_name"] = inp
    if element == 4:
        print("4-город")
        db["contact"][index - 1]["city"] = inp
    if element == 5:
        print("5-улица")
        db["contact"][index - 1]["street"] = inp
    if element == 6:
        print("6-дом")
        db["contact"][index - 1]["house"] = inp
    if element == 7:
        print("7-номер квартиры")
        db["contact"][index - 1]["room"] = inp
    if element == 8:
        print("8-номер домашнего телефона")
        db["contact"][index - 1]["telephone"] = inp
    if element == 9:
        print("9-номер сотового телефона ")
        db["contact"][index - 1]["number"] = inp

    ###

    f = open(db_directory, "r+")
    f.seek(0)
    f.truncate()
    temp = str(db)
    str_dct = temp.replace("\'", "\"")
    f.write(str_dct)
    f.close()
    #print(db["contact"])


'''
def remove(line_index=0):
    lines = []
    with open(db_directory, "r") as f:
        lines = f.readlines()
    r = lines.pop(line_index)
    print("Вы удалили: " + r)
    with open(db_directory, "w") as f:
        for l in lines:
            f.write(l)
'''


def searchJson_city(s1):
    global db
    init()
    print("===Результат поиска===")
    i = 0
    while i < len(db["contact"]):
        if s1.lower() in str(db["contact"][i]["city"]).lower():
            print(str(i + 1) + ") " + str(db["contact"][i]["surname"]) + " " + str(
                db["contact"][i]["name"] + " " + db["contact"][i]["second_name"]) + ", город " + str(
                db["contact"][i]["city"]) + ", улица " + str(db["contact"][i]["street"]) + " " + str(
                db["contact"][i]["house"]) + " " + str(db["contact"][i]["room"]) + ", тел: " + str(
                db["contact"][i]["number"]) + ", дом.тф: " + str(db["contact"][i]["telephone"]))
        i = i + 1
    print("======================")


def searchJson_street(s1, s2):
    global db
    init()
    print("===Результат поиска===")
    i = 0
    while i < len(db["contact"]):
        if s1.lower() in str(db["contact"][i]["city"]).lower():
            if s2.lower() in str(db["contact"][i]["street"]).lower():
                print(str(i + 1) + ") " + str(db["contact"][i]["surname"]) + " " + str(
                    db["contact"][i]["name"] + " " + db["contact"][i]["second_name"]) + ", город " + str(
                    db["contact"][i]["city"]) + ", улица " + str(db["contact"][i]["street"]) + " " + str(
                    db["contact"][i]["house"]) + " " + str(db["contact"][i]["room"]) + ", тел: " + str(
                    db["contact"][i]["number"]) + ", дом.тф: " + str(db["contact"][i]["telephone"]))
        i = i + 1
    print("======================")


def searchJson_house(s1, s2, s3):
    global db
    init()
    print("===Результат поиска===")
    i = 0
    while i < len(db["contact"]):
        if s1.lower() in str(db["contact"][i]["city"]).lower():
            if s2.lower() in str(db["contact"][i]["street"]).lower():
                if str(s3) in str(db["contact"][i]["house"]).lower():
                    print(str(i + 1) + ") " + str(db["contact"][i]["surname"]) + " " + str(
                        db["contact"][i]["name"] + " " + db["contact"][i]["second_name"]) + ", город " + str(
                        db["contact"][i]["city"]) + ", улица " + str(db["contact"][i]["street"]) + " " + str(
                        db["contact"][i]["house"]) + " " + str(db["contact"][i]["room"]) + ", тел: " + str(
                        db["contact"][i]["number"]) + ", дом.тф: " + str(db["contact"][i]["telephone"]))
        i = i + 1
    print("======================")


def search(s):
    # add to .lower()
    print("===Результат поиска===")
    with open(db_directory) as f:
        for line in f:
            if s in line:
                print(line)
    print("======================")


def info():
    print('\033[92m'+"===Что вы хотите сделать?==="+ '\033[0m')
    txt1 = "1-добавить запись"
    txt2 = "2-показать справочник"
    txt3 = "3-удалить запись"
    txt4 = "4-редактировать запись"
    txt5 = "5-поиск"
    txt0 = "0-выйти"
    print(txt1 + "\n" + txt2 + "\n" + txt3 + "\n" + txt4 + "\n" + txt5 + "\n" + txt0)


def info_search():
    print("===Поиск===")
    txt1 = "1-по городу"
    txt2 = "2-по улице"
    txt3 = "3-по дому"
    txt0 = "0-назад"
    print(txt1 + "\n" + txt2 + "\n" + txt3 + "\n" + txt0)


def info_edit():
    print("===Выберите элемент для редактирования===")
    txt1 = "1-фамилия"
    txt2 = "2-имя"
    txt3 = "3-отчество"
    txt4 = "4-город"
    txt5 = "5-улица"
    txt6 = "6-дом"
    txt7 = "7-номер квартиры"
    txt8 = "8-номер домашнего телефона"
    txt9 = "9-номер сотового телефона "
    txt0 = "0-назад"
    print(txt1 + "\n" + txt2 + "\n" + txt3 + "\n" + txt4 + "\n" + txt5 + "\n" +
          txt6 + "\n" + txt7 + "\n" + txt8 + "\n" + txt9 + "\n" + txt0)


def show():
    print("=========СПРАВОЧНИК=========")
    init()
    if len(db) > 0:
        i = len(db["contact"])
        while i > 0:
            # print(db["contact"][i - 1]["name"])
            print(str(i) + ") " + str(db["contact"][i - 1]["surname"]) + " " + str(
                db["contact"][i - 1]["name"] + " " + db["contact"][i - 1]["second_name"]) + ", город " + str(
                db["contact"][i - 1]["city"]) + ", улица " + str(db["contact"][i - 1]["street"]) + " " + str(
                db["contact"][i - 1]["house"]) + " " + str(db["contact"][i - 1]["room"]) + ", тел: " + str(
                db["contact"][i - 1]["number"]) + ", дом.тф: " + str(db["contact"][i - 1]["telephone"]))
            i = i - 1
    print("============================")


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# programm
for i in range(100+1):
    time.sleep(0.1)
    sys.stdout.write(('='*i)+(''*(100-i))+("\r          [ %d"%i+"% ]          "))
    sys.stdout.flush()
print("")
init()
info()
i = -1
while int(i) != 0:
    try:
        i = int(input())
        clear()
    except ValueError:
        print('\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m')
    if int(i) == 2:
        show()
    if int(i) == 1:
        add()
    if int(i) == 3:
        e = -1
        while int(e) != 0:
            print("===Введите индекс контакта для удаления===")
            print("* или введите 0, чтобы вернуться назад")
            try:
                e = int(input())
                clear()
            except ValueError:
                print('\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m')
            if e > 0 and e < (len(db["contact"]) + 1):
                removeJson(e)
                e = 0
    if int(i) == 4:
        e = -1
        while int(e) != 0:
            print("===Введите индекс контакта для редактирования===")
            print("* или введите 0, чтобы вернуться назад")
            try:
                e = int(input())
                clear()
            except ValueError:
                print('\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m')
            if e > 0 and e < (len(db["contact"]) + 1):
                e = 0  # выход к перд.меню
                z = -1
                while int(z) != 0:
                    info_edit()
                    try:
                        z = int(input())
                        clear()
                    except ValueError:
                        print('\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m')
                    if z > 0:
                        editJson(e, int(z))
    if int(i) == 5:
        o = -1
        while int(o) != 0:
            info_search()
            o = int(input())
            if int(o) == 1:
                print("===Введите название города===")
                ss = input()
                searchJson_city(ss)
            if int(o) == 2:
                print("===Введите название города===")
                s1 = input()
                print("===Введите название улицы===")
                s2 = input()
                searchJson_street(s1, s2)
            if int(o) == 3:
                print("===Введите название города===")
                s1 = input()
                print("===Введите название улицы===")
                s2 = input()
                print("===Введите номер дома===")
                s3 = input()
                searchJson_house(s1, s2, s3)
    if int(i) == 5:
        init()
    info()
