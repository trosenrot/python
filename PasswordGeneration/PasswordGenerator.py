import random

def question(text, symbols):
    text = text + ' ' + symbols + '?(д/н): '
    while True:
        answer = input(text).strip()
        if is_corrected_answer(answer):
            return is_yes_or_no(answer)
        else:
            continue

def is_corrected_answer(answer):
    if answer == 'д' or answer == 'н':
        return True
    return False

def is_yes_or_no(answer):
    if answer == 'д':
        return True
    return False
    
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password
    

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
symbols = 'il1Lo0O'
chars = ''

num_passwords = int(input('Количество паролей для генерации: '))
num_chars = int(input('Длина одного пароля: '))
if question('Включать ли цифры', digits):
    chars += digits
if question('Включать ли прописные буквы', uppercase_letters):
    chars += uppercase_letters
if question('Включать ли строчные буквы', lowercase_letters):
    chars += lowercase_letters
if question('Включать ли символы', punctuation):
    chars += punctuation
if question('Исключить ли неоднозначные символы', symbols):
    for c in symbols:
        if c in chars:
            chars = chars.replace(c, '')
for _ in range(num_passwords):
    print(generate_password(num_chars, chars))
