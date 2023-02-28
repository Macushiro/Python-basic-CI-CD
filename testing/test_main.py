"""
    Файл тестирования приложения на Flask.
    0) Создали базовую версию теста;
"""

# # ---------------------- Step 0 ---------------------- #
# # создали базовую версию теста
# import random       # 1.2 версия, добавили импорт для проверки на рандомное значение
#
#
# def test_get_item(client):
#     """
#     test_get_item
#     :param client:
#     :return:
#     """
#     random_id = random.randint(1, 100)      # 1.2 версия, добавили генерацию рандомного значения
#     # url = '/items/3/'             # 1.0 версия, указали URL тестового запроса
#     url = f'/items/{random_id}/'    # 1.2 версия, добавили передачу сгенеренного значения
#     response = client.get(url)      # 1.0 версия, получаем ответ через тестовый клиент
#                                     # (который настроили в файле "conftest.py")
#     assert response.status_code == 200      # 1.0 версия, сверяем код ответа с ожидаемым значением
#
#     # assert response.json['item']['id'] == 3     # 1.1 версия, после успешного теста добавили
#     #                                             проверку на конкретное значение
#     assert response.json['item']['id'] == random_id     # 1.2 версия, изменили проверку

# ---------------------- Step 1 ---------------------- #
# добавили ещё один тест для view с рендерингом формы
import random


def test_get_item(client):
    """
    test_get_item
    :param client:
    :return:
    """
    random_id = random.randint(1, 100)
    # url = '/items/3/'
    url = f'/items/{random_id}/'
    response = client.get(url)
    assert response.status_code == 200

    assert response.json['item']['id'] == random_id


# 1.0 версия, добавили тест для view с рендерингом формы
def test_add_product(client):
    """
    test add product
    :param client:
    :return:
    """
    # url = '/add/'     # 1.2 версия, изменили адрес, т.к. забыли часть адреса из Blueprint
    url = '/products/add/'      # 1.2 версия, изменили адрес, т.к. забыли часть адреса из Blueprint
    # 1.0 версия, описали полезную нагрузку
    data = {
        'product-name': 'Test product name'
    }
    # 1.0 версия, отправляем POST-запрос на адрес "url", а в теле запроса "data"
    response = client.post(url, data=data)
    # 1.0 версия, сравниваем на статус 302 == перенаправление на другую страницу
    # assert response.status_code == 302    # 1.1 версия, изменили
    # 1.1 версия, добавили вывод текст WEB-страницы
    assert response.status_code == 302, response.text
