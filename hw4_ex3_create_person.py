import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'


def new_pers(name, type, level, book):
    new_pers = requests.post(base_url + 'roles/', data={"name": name, "type": type, "level": level, "book": book})

    return new_pers.json()


def check_pers_existence_link(id):
    get_pers = requests.get(base_url + 'roles/' + str(id))
    return get_pers


def check_pers_existence_in_list(id):
    perss = requests.get(base_url + 'roles/')
    pers_list = perss.json()

    for p in pers_list:
        if p['id'] == id:
            return True
    return False


def change_name_pers(id, name):
    requests.put(base_url + 'roles/' + str(id) + '/', data={"name": name})
    get_pers = requests.get(base_url + 'roles/' + str(id))
    return get_pers.text


def change_type_pers(id, type):
    requests.put(base_url + 'roles/' + str(id) + '/', data={"type": type})
    get_pers = requests.get(base_url + 'roles/' + str(id))
    return get_pers.text


def change_level_pers(id, level):
    requests.put(base_url + 'roles/' + str(id) + '/', data={"level": level})
    get_pers = requests.get(base_url + 'roles/' + str(id))
    return get_pers.text


def change_book_pers(id, book):
    requests.put(base_url + 'roles/' + str(id) + '/', data={"book": book})
    get_pers = requests.get(base_url + 'roles/' + str(id))
    return get_pers.text


def delete_pers(id):
    del_pers = requests.delete(base_url + 'roles/' + str(id) + '/')
    return del_pers.status_code, del_pers.reason


res_id = new_pers("Snape", "teacher", "150", "1")['id']

print(res_id)
print('Новый элемент доступен по ссылке. ' + str(check_pers_existence_link(res_id)))
print('Новый элемент есть в списке книг. ' + str(check_pers_existence_in_list(res_id)))
print('Измененный элемент (имя): ' + str(change_name_pers(res_id, 'Severus Snape')))
print('Измененный элемент (должность): ' + str(change_type_pers(res_id, 'Course supervisor')))
print('Измененный элемент (уровень): ' + str(change_level_pers(res_id, '250')))
print('Измененный элемент (книга): ' + str(change_book_pers(res_id, '2')))
print('Измененный элемент доступен по ссылке. ' + str(check_pers_existence_link(res_id)))
print('Измененный элемент есть в списке книг. ' + str(check_pers_existence_in_list(res_id)))
print('Поиск элемента после удаления. ' + str(delete_pers(res_id)))
