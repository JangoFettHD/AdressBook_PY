# -*- coding: utf-8 -*-
import json

# initialize
print("------Справочник 0.01a------")
# db_directory="/media/student/JF-MINI/Book/db.txt" #linux
db_directory = "E:\\Book\\Win\\db.txt"  # win
db_temp = "E:\\Book\\Win\\db_temp.txt"  # win
db = {}


def init():
    global db
    with open(db_directory, "r+") as f:
        content = str(f.read())
        f.seek(0)
        if not (len(content) == 0):
            json1_data = json.loads(content)
            db = json1_data
            print('\x1b[6;30;42m'+"@LOG: "+str(db) + '\x1b[0m')


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
    print('\x1b[6;30;42m'+"@LOG: "+"@LOG: "+str(db)+ '\x1b[0m')
    if "contact" in db.keys():
        db["contact"].append(dct)
    else:
        db["contact"] = [dct]

    # db["contact"]=dct
    print('\x1b[6;30;42m'+"@LOG: "+"@LOG: "+str(db)+ '\x1b[0m')

    temp = str(db)
    str_dct = temp.replace("\'", "\"")
    f.write(str_dct)
    # f.write(str(db))
    # f.write((str(dct)+",").encode())
    f.close()


def remove(line_index):
    lines = []
    with open(db_directory, "r") as f:
        lines = f.readlines()
    r = lines.pop(line_index)
    print("Вы удалили: " + r)
    with open(db_directory, "w") as f:
        for l in lines:
            f.write(l)


def search(s):
    # add to .lower()
    print("===Результат поиска===")
    with open(db_directory) as f:
        for line in f:
            if s in line:
                print(line)
    print("======================")


def info():
    print("===Что вы хотите сделать?===")
    txt1 = "1-добавить запись"
    txt2 = "2-показать справочник"
    txt3 = "3-удалить запись"
    txt4 = "4-поиск"
    txt0 = "0-выйти"
    print(txt1 + "\n" + txt2 + "\n" + txt3 + "\n" + txt4 + "\n" + txt0)


def info_search():
    print("===Поиск===")
    txt1 = "1-по городу"
    txt2 = "2-по улице"
    txt3 = "3-по фамилии"
    txt0 = "0-назад"
    print(txt1 + "\n" + txt2 + "\n" + txt3 + "\n" + txt0)


'''
def show():
    print("=========СПРАВОЧНИК=========")
    t = open(db_directory, "r+")
    print(t.read())
    t.close()
    print("============================")
    '''


def show():
    print("=========СПРАВОЧНИК=========")
    init()
    if len(db) > 0:
        i = len(db["contact"])
        while i > 0:
            #print(db["contact"][i - 1]["name"])
            print(str(db["contact"][i - 1]["surname"])+" "+str(db["contact"][i - 1]["name"]+" "+db["contact"][i - 1]["second_name"])+", город "+str(db["contact"][i - 1]["city"])+", улица "+str(db["contact"][i - 1]["street"])+" "+str(db["contact"][i - 1]["house"])+" "+str(db["contact"][i - 1]["room"])+", тел: "+str(db["contact"][i - 1]["number"])+", дом.тф: "+str(db["contact"][i - 1]["telephone"]))
            i = i - 1
    print("============================")


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# programm
info()
i = -1
while int(i) != 0:
    i = int(input())
    clear()
    if int(i) == 2:
        show()
    if int(i) == 1:
        add()
    if int(i) == 3:
        print("===Введите номер строки для удаления===")
        b = int(input())
        remove(b)
    if int(i) == 4:
        print("===Введите слово для поиска===")
        inp1 = input()
        search(inp1)
    if int(i) == 5:
        init()
    info()
