import random


def randomForKellyUp():
    randomInt = random.randint(1, 100)
    if randomInt <= 50:
        return 0
    elif 51 <= randomInt <= 75:
        return 1
    elif 76 <= randomInt <= 95:
        return 2
    else:
        return 3


def randomForKellyDown():
    randomInt = random.randint(1, 100)
    if randomInt <= 5:
        return 0
    elif 6 <= randomInt <= 25:
        return 1
    elif 26 <= randomInt <= 70:
        return 2
    else:
        return 3


def randomForTravisLeft():
    randomInt = random.randint(1, 100)
    if randomInt <= 20:
        return 0
    elif 21 <= randomInt <= 25:
        return 1
    elif 26 <= randomInt <= 55:
        return 2
    else:
        return 3


def randomForTravisRight():
    randomInt = random.randint(1, 100)
    if randomInt <= 45:
        return 0
    elif 46 <= randomInt <= 75:
        return 1
    elif 76 <= randomInt <= 95:
        return 2
    else:
        return 3
