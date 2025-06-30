# HabiticaProject

> [Ссылка на сайт Habitica](https://habitica.com)

## Структура проекта
```
HabiticaProject/
├── model/                      # Page Objects
│   ├──data
│       ├──users.py
│   ├──pages                    
│       ├── login_page.py       # Страница авторизации
│       └── main_page.py        # Главная страница
├── tests/                      # UI Тесты
│   ├── conftest.py             # Конфигурация pytest
│   └── test_login.py           # Тесты формы авторизации    
│   ├── test_registration.py    # Тесты формы регистрации
├── utils/                      # Утилиты
│   └── attach.py               # Функции для Allure
├── .env                        # Переменные окружения
├── requirements.txt            # Зависимости проекта
└── pytest.ini                  # Конфигурация pytest