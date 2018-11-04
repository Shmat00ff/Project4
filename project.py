text = str(input("Введите текст: "))
letter = str(input("Введите букву: "))
vowels = "аоиеёэыуюяАОИЕЁЭЫУЮЯ"
consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

if letter in consonants:
    agree = str(input("Начнём?(Да/Нет): ")).upper()
    while agree == "ДА":
        for i in range(len(vowels)):
            k = text.find(vowels[i])
            if k != -1:
                text = text.replace(text[k], text[k] + letter.lower() + text[k].lower())
        print(text)
        agree = str(input("Хотите ещё?(Да/Нет): ")).upper()
        if agree == "ДА":
            text = str(input("Введите текст: "))
            letter = str(input("Введите букву: "))
            if not letter in consonants:
                print("Вы ввели не согласную букву")
                agree = "нет"
elif not letter in consonants:
    print("Вы ввели не согласную букву")
