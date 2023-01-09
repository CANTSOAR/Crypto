import datetime as dt

def code(uinput, creationdate = dt.datetime.today()):
    # cd = codedate, lc = lengthcount, ind = innercodedate

    letters = "yGsUq6Hu1:KEjn!3CYJo'IWApixS7bLRX r0l.eVDz,Oh2ZTB\"8Pf5?wNk=Qd4a-mM9c/vgFt"
               

    cd = creationdate - dt.timedelta(days = len(uinput))

    lc = 0

    res = ""

    for char in uinput:

        keycorrection = ""

        if lc % 3 == 0:
            date = cd.year
        elif lc % 3 == 1:
            date = cd.day
        else:
            date = cd.month
        
        x = 2

        while x in range(2, min((lc + date), len(letters))+1):
            if (lc + date) % x == len(letters) % x == 0:
                date += 1
                keycorrection += "~"
                x = 1
            x += 1

        key = (letters.find(char) * (lc + date)) % len(letters)
        res += keycorrection + letters[key]

        lc += 1

    res += "|" + str((creationdate.year * 10000 + creationdate.day * 100 + creationdate.month) * lc)

    return res

def decode(coded):
    # cd = codedate, lc = lengthcount, ind = innercodedate

    letters = "yGsUq6Hu1:KEjn!3CYJo'IWApixS7bLRX r0l.eVDz,Oh2ZTB\"8Pf5?wNk=Qd4a-mM9c/vgFt"

    lc = 0
    lccorrection = 1

    for char in coded:
        if char != "|":
            lc += 1
            if char == "~":
                lccorrection += 1
        else:
            lc += 1
            break

    codeddate = str(int(coded[lc:]) / (lc - lccorrection))

    coded = coded[:lc - 1]

    cd = dt.date(int(codeddate[:4]), int(codeddate[6:8]), int(codeddate[4:6])) - dt.timedelta(days = lc - lccorrection)

    res = ""

    lc = 0

    keycorrection = 0

    for char in coded:

        if char != "~":

            newdex = 0

            if lc % 3 == 0:
                date = cd.year
            elif lc % 3 == 1:
                date = cd.day
            else:
                date = cd.month

            while (newdex * (lc + date + keycorrection)) % len(letters) != letters.find(char):
                newdex += 1

            res += letters[newdex]

            keycorrection = 0
        else:
            keycorrection += 1
            lc -= 1

        lc += 1

    return res

action = input("type \"input\" or \"decode\": ")

if action == "input":
    uinput = input("Input: ")

    print(code(uinput))

    print(decode(code(uinput)))

elif action == "decode":
    udecode = input("Decode: ")

    print(decode(udecode))

    print(code(decode(udecode)))