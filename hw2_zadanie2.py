while True:
    var_input = input(
        'Введите 1, если хотите использовать для задания предустановленную строку. Введите 2, если хотите сами ввести строку.\n', )
    if var_input == '1':
        st_input = 'We are not what we should be! We are not what we need to be. But at least we are not what we used to bе.'
        break
    elif var_input == '2':
        st_input = input('Введите строку: ', )
        break
    else:
        print('Некорректный ввод данных.')
        continue

# 1. Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
st_in = st_input.split(' ')
len_in = len(st_input.split(' '))
print('Количество слов в тексте: ', len_in, '\n')

# 2. Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# Вариант первый, который мне не нравится
non_sign = []
mid = ''
mid1 = ''
for i in range(len_in):
    mid = st_in[i].strip()
    mid1 = mid.strip('!')
    non_sign.append(mid1.strip('.'))
    joi = ''.join(non_sign)
print('Текст без знаков препинания. Вариант 1: ', joi, '\n')


# 2. Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# Второй вариант. Который мне тоже не очень нравится. В этом случае, если в самом слове будет находится символ знака
# препинания, все зациклится. Но я еще подумаю над этим)
non_sign = []
a = [',', '!','.',' ', '?', '*']
mid = ''
for i in range(len_in):
    while st_in[i].isalnum() == False:
        for k in range(len(a)):
            mid = st_in[i]
            st_in[i] = mid.strip(a[k])
            print(st_in[i])
    non_sign.append(st_in[i])
    joi = ''.join(non_sign)
print('Текст без знаков препинания. Вариант 2: ', joi, '\n')

# 3. Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
non_sign.sort()
print('Отсортированный по алфавиту: ', non_sign, '\n')

# 4. Посчитать, сколько раз встречается каждое слово.
diction = {}
for el in non_sign:
    if el in diction:
        diction[el] += 1
    else:
        diction[el] = 1
print(diction)
