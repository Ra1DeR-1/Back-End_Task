from datetime import datetime
import random
import json


def init():
    try:
        with open("data.json", 'r') as f:
            return json.load(f)
    except:
        open("data.json", 'w')
        return []


class table:
    storage = None
    if storage is None:
        storage = init()
    string = {
        "id": "",
        "username": "",
        "password": "",
        "created_at": "",
        "updated_at": ""
    }

    def __init__(self):
        self.storage = []
        self.string = {
            "id": "",
            "username": "",
            "password": "",
            "created_at": "",
            "updated_at": ""
        }


def save(self=table):
    f = open("data.json", 'w')
    json.dump(self.storage, f)
    f.close()


def create(self=table, username=input(" input username "), password=input(" input password ")):
    username_ = []
    for i in range(0, len(self.storage)):
        username_.append(self.storage[i]["username"])
    if username_.count(str(username)) != 0:
        print(f"Username -> {username} занят!")
        return None
    _str = self.string.copy()
    id_ = ["-1"]
    for i in range(1, len(self.storage)):
        id_.append(self.storage[i]["id"])
    r = "-1"
    while id_.count(r) != 0:
        r = str(random.randint(0, 4294967296))
    _str["id"] = r
    _str["username"] = str(username)
    _str["password"] = str(password)
    _str["created_at"] = datetime.now().strftime("%A, %d. %B %Y %H:%M:%S")
    _str["updated_at"] = datetime.now().strftime("%A, %d. %B %Y %H:%M:%S")
    self.storage.append(_str)
    save()


def update(self=table, username="", password=""):
    username_ = []
    for i in range(0, len(self.storage)):
        username_.append(self.storage[i]["username"])
    if username_.count(str(username)) == 1:
        ind = username_.index(str(username))
        self.storage[ind]["password"] = str(password)
        self.storage[ind]["updated_at"] = datetime.now().strftime("%A, %d. %B %Y %H:%M:%S")
    else:
        print(f"Username -> {username} nope!")
    save()


def delete(self=table, id="0"):
    id_ = []
    for i in range(0, len(self.storage)):
        id_.append(self.storage[i]["id"])
    if id_.count(str(str(id))) != 0:
        self.storage.pop(id_.index(str(id)))
    save()


def get(self=table, id="0"):
    id_ = []
    for i in range(0, len(self.storage)):
        id_.append(self.storage[i]["id"])
    if id_.count(str(str(id))) != 0:
        return self.storage[id_.index(str(id))]


def main(i):
    if i == "c":
        create()
        print(str(i) + str(table.storage))
    elif i == "u":
        update(username=input(" input update username "), password=input(" input update password "))
        print(str(i) + str(table.storage))
    elif i == "d":
        delete(id=input(" ... "))
        print(str(i) + str(table.storage))
    elif i == "g":
        print(str(i) + str(get(id=input(" ... "))))


if __name__ == "__main__":
    while True:
        main(input(" >>> "))