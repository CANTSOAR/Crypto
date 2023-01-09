alpha = [" ","a","b","c","d",
         "e","f","g","h","i",
         "j","k","l","m","n",
         "o","p","q","r","s",
         "t","u","v","w","x",
         "y","z"]

input = input("encode: ").lower()

def encode(input):
    code1 = []
    tempcode = ""

    for char in input:
        codenum = alpha.index(char)

        if not codenum:
            if tempcode:
                code1.append(tempcode)
                tempcode = ""
            else:
                code1.append("00")
            continue
        if int(codenum / 10) == 0:
            codenum = "0" + str(codenum)

        tempcode += str(codenum)

    code1.append(tempcode)

    code2 = []

    for code in range(len(code1)):
        base = int(int(code1[code]) ** (1 / len(code1[code])))
        extra = int(code1[code]) - int(base ** len(code1[code]))

        code2.append(str(int(len(code1[code]))) + "-" + str(base) + "-" + str(extra))

    return code2

def output(input):
    output = ""

    if "-" in input[0]:
        spacer = "|"
    else:
        spacer = " "

    for code in input:
        output += code + spacer

    return output

def decode(encoded_input):
    coded1 = []
    code_word = ""
    for char in encoded_input:
        if char != "|":
            code_word += char
        else:
            coded1.append(code_word)
            code_word = ""

    coded2 = []

    for code in coded1:
        sindex = 0
        eindex = -1
        power = 0
        base = 0
        extra = 0

        for char in code:
            eindex += 1
            if char == "-":
                power = int(code[sindex:eindex])
                sindex = eindex + 1
                break

        for char in code[eindex + 1:]:
            eindex += 1
            if char == "-":
                base = int(code[sindex:eindex])
                sindex = eindex + 1
                break

        extra = int(code[eindex + 1:])

        coded2.append(str(base ** power + extra))

    decoded = []

    for code in coded2:
        word = ""
        while int(code):
            word = alpha[int(code) % 100] + word
            code = int(code) / 100

        decoded.append(word)

    return decoded


coded = encode(input)
print(output(coded))
decoded = decode(output(coded))
print(output(decoded))