# 4. Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена пробелами. Выведите ее на экран.
st = 'Homework'
print('\n','Отцентрованная строка "Homework": ', st.center(100))
print()

while True:
    var_input = input(
        'Введите 1, если хотите использовать для задания предустановленную строку. Введите 2, если хотите сами ввести строку.\n', )
    if var_input == '1':
        st_input = 'all I ever wanted. All I ever needed. Is here in my arms. Words are very unnecessary.'
        break
    elif var_input == '2':
        st_input = input('Введите строку: ', )
        break
    else:
        print('Некорректный ввод данных.')
        continue

# 1. Определите является ли строка записью числа.
if st_input.isnumeric():
    print("Строка яаляется записью числа.", '\n')
else:
    print("Строка не яаляется записью числа.", '\n')

# 2. Посчитайте сколько у вас пробелов в строке.
print('Количество пробелов в строке - ', st_input.count(' '), '\n')

# 3. Посчитайте сколько у вас символов точки '.' в строке.
print('Количество точек в строке - ', st_input.count('.'), '\n')

# 5. Сделайте первые буквы слов строки большими (upper case).
st_list = list(st_input)
res = ''
for i in range(len(st_list)):
    if st_list[i - 1].isalpha() == False:
        st_list[i] = st_list[i].upper()
k = ''.join(st_list)
print('Строка, в которой все первые буквы слов большие:', '\n', k)
