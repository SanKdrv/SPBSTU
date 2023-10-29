# TODO  Напишите функцию count_letters
def count_letters(text):
    counted_letters = dict()
    for char in text:
        if char.isalpha():
            counted_letters[char.lower()] = text.lower().count(char.lower())
    return counted_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(text, dictionary):
    length_of_text = 0
    for letter in text:
        if letter.lower().isalpha():
            length_of_text += 1
    frequency_of_letters = dict()
    for key in dictionary:
        frequency_of_letters[key] = dictionary[key] / length_of_text
    return frequency_of_letters


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
solve = calculate_frequency(main_str, count_letters(main_str))
for element in solve:
    print(element + ":", "{:.2f}".format(round(solve[element], 2)))
