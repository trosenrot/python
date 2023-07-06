def is_valid(text, answers):
    while True:
        answer = input(text).lower()
        if answer not in answers and (''.join(answers)).isalpha():
            print('Некорректное значение! (введите {} или {})'.format(answers[0], answers[1]))
            continue
        elif answer not in answers and (''.join(answers)).isdigit():
            print('Некорректное значение! (введите значение между {} и {})'.format(answers[0], answers[len(answers)-1]))
            continue
        else:
            return answer
            
print('Здравствуйте!')
sign = is_valid ('Что требуется сделать с текстом: зашифровать или дешифровать?: ', ['зашифровать', 'дешифровать'])
language = is_valid ('На каком языке текст: русском или английском?: ', ['русский', 'английский'])
if language == 'русский':
    upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    step = int(is_valid ('Какой шаг сдвига?: ', [str(i) for i in range(1,33)]))
    n = 32
else:
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    step = int(is_valid ('Какой шаг сдвига?: ', [str(i) for i in range(1,27)]))
    n = 26
if sign == 'дешифровать':
    step = -step
text = input('Введите текст: ')
text2 = ''
for i in range(len(text)):
    c = text[i]
    if c in upper_alphabet:
        index = upper_alphabet.index(c)
        index = (index + step) % n
        c = upper_alphabet[index]
    elif c in lower_alphabet:
        index = lower_alphabet.index(c)
        index = (index + step) % n
        c = lower_alphabet[index]
    text2 += c
print(text2)
