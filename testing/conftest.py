"""
    Файл настройки тестового клиента в Flask.
    0) Создали базовую версию настроек;
"""

import pytest        # 1.0 версия, добавили импорт, чтобы объявить фикстуру
from flask.testing import FlaskClient    # 1.0 версия, добавили импорт тестового клиента

from main import app


@pytest.fixture
def client() -> FlaskClient:    # 1.0 версия, функция возвращает тестовый клиент
    """
    client
    :return:
    """
    # app.config.update(WTF_CSRF_ENABLED=False)
    with app.test_client() as test_client:      # 1.0 версия, получаем тестовый клиент
        with app.app_context():                 # 1.0 версия, получаем контекст приложения,
                                                # чтобы в нём выполнять тесты
            yield test_client                   # 1.0 версия, превращаем функцию в генератор
