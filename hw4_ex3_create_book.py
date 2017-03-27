import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'


def new_book(title, author):
    new_book = requests.post(base_url + 'books/', data={"title": title, "author": author})

    return new_book.json()


def check_book_existence_link(id):
    get_book = requests.get(base_url + 'books/' + str(id))
    return get_book


def check_book_existence_in_list(id):
    books = requests.get(base_url + 'books/')
    book_list = books.json()

    for b in book_list:
        if b['id'] == id:
            return True
    return False


def change_title_book(id, title):
    requests.put(base_url + 'books/' + str(id) + '/', data={"title": title})
    get_book = requests.get(base_url + 'books/' + str(id))
    return get_book.text


def change_author_book(id, author):
    requests.put(base_url + 'books/' + str(id) + '/', data={"author": author})
    get_book = requests.get(base_url + 'books/' + str(id))
    return get_book.text


def delete_book(id):
    del_book = requests.delete(base_url + 'books/' + str(id) + '/')
    return del_book.status_code, del_book.reason


res_id = new_book("XOP", "WERTY")['id']

print(res_id)
print('Новый элемент доступен по ссылке. ' + str(check_book_existence_link(res_id)))
print('Новый элемент есть в списке книг. ' + str(check_book_existence_in_list(res_id)))
print('Измененный элемент (автор): ' + str(change_author_book(res_id, 'К.Дойль')))
print('Измененный элемент (автор): ' + str(change_title_book(res_id, 'Пляшущие человечки')))
print('Измененный элемент доступен по ссылке. ' + str(check_book_existence_link(res_id)))
print('Измененный элемент есть в списке книг. ' + str(check_book_existence_in_list(res_id)))
print('Поиск элемента после удаления. ' + str(delete_book(res_id)))
