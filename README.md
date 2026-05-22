# Recipe Project - CI/CD Demo

Проект демонструє дотримання основних принципів Continuous Integration/Continuous Deployment за допомогою Django, Git та GitHub Actions.

## Вимоги

- Python 3.9+
- Django 4.2.1
- pytest-django
- python-dotenv

## Установка

1. Клонуйте репозиторій:
```bash
git clone https://github.com/Arti0f2/CI-CD_Ivaschuk_Artem_Middle_Test_2.git
cd CI-CD_Ivaschuk_Artem_Middle_Test_2
```

2. Створіть віртуальне середовище:
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

4. Виконайте міграції:
```bash
python manage.py migrate
```

## Запуск

### Розробка
```bash
python manage.py runserver
```

### Тести
Запуск Django тестів:
```bash
python manage.py test
```

Запуск pytest:
```bash
pytest
```

Запуск з покриттям:
```bash
pytest --cov=recipe --cov-report=html
```

## Структура проекту

```
project_recipe/          # Налаштування проекту
├── settings.py         # Налаштування Django
├── urls.py            # URL конфігурація
├── wsgi.py            # WSGI конфігурація
└── asgi.py            # ASGI конфігурація

recipe/                 # Основна додатка
├── models.py          # Моделі (Category, Recipe)
├── views.py           # Views
├── admin.py           # Адмін налаштування
├── tests.py           # Unit-тести
└── templates/
    └── main.html      # Шаблони

templates/              # Глобальні шаблони
└── base.html          # Базовий шаблон
```

## Моделі

### Category
- `name`: CharField (унікальне)
- `__iter__`: ітератор для отримання значень

### Recipe
- `title`: CharField
- `description`: TextField
- `instructions`: TextField
- `ingredients`: TextField
- `created_at`: DateTimeField (автоматично)
- `updated_at`: DateTimeField (автоматично)
- `category`: ForeignKey до Category

## Змінні середовища

Створіть файл `.env` в корні проекту:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Git Workflow

Проект використовує дві основні гілки:
- `main`: Продакшн версія
- `develop`: Розробка нових функцій

### Коміти
Для кожної функції/методу створюється окремий коміт з описовою назвою.

## CI/CD Pipeline

Проект налаштований з GitHub Actions для:
1. Автоматичного запуску тестів при push/PR
2. Перевірки стилю коду (flake8)
3. Розгортання на Heroku при push в main (при наявності credentials)

## Тестування

Проект включає comprehensive unit-тести для:
- Створення та видалення категорій
- Валідації унікальності назви категорії
- Перевірки методу `__iter__`
- Створення та оновлення рецептів
- Зв'язків між моделями
- Каскадного видалення

## Розгортання на Heroku

Проект підготовлений для розгортання на Heroku. Необхідні налаштування:
1. Додайте `Procfile` з командою запуску
2. Налаштуйте environment variables на Heroku
3. Налаштуйте GitHub secrets для HEROKU_API_KEY та HEROKU_APP_NAME

## Автори

Іващук Артем


