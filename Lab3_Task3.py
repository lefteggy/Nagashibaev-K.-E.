# TODO  Напишите функцию count_letters
def count_letters(string):
    string = string.lower()
    list = {}
    for letter in string:
        if letter.isalpha():
            if list.get(letter) != None:
                list[letter] += 1
            else:
                list[letter] = 1
    return list
# TODO Напишите функцию calculate_frequency
def calculate_frequency(list):
    frequency = {}
    count = 0
    for key in list.keys():
        count += list[key]
    for key in list.keys():
        frequency[key] = list[key]/count
    return frequency
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
list = count_letters(main_str)
frequency = calculate_frequency(list)
for key in frequency.keys():
    print(f"{key}: {"%.2lf"}" % frequency[key])
