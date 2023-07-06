import random
import math

def is_valid_text(text):
    if text.isdigit():
        if math.trunc(float(text)) == float(text):
            return True
    return False

def is_valid(text, n):
    if is_valid_text(text):
        if 1 <= int(text) <= n:
            return True
    return False

print('Добро пожаловать в числовую угадайку')
flag = True

while flag:
    n = input('Введите целое число больше 1 до которого будем загадывать:')
    if not is_valid_text(n) or int(n) < 2:
        print('Введите корректное число!')
        continue
    n = int(n)
    rand_num = random.randint(1, n)
    count = 0
    while True:
        print('Введите целое число от 1 до {}:'.format(n))
        num = input()
        if not is_valid(num, n):
            print('А может быть все-таки введем целое число от 1 до {}?'.format(n))
            continue
        num = int(num)
        count += 1
        if num < rand_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > rand_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
    print('Вы угадали с {} попытки.'.format(count))
    while True:
        print('Хотите сыграть еще? (д/н):')
        answer = input()
        if answer == 'д':
            break
        elif answer == 'н':
            flag = False
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
