# Logger для Python 3

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

Logger - це модуль для реєстрації подій, повідомлень та помилок у програмах, написаних на мові Python 3.

## Вступ до логування (Introduction to Logging)

Логування є важливою частиною розробки програм, оскільки дозволяє фіксувати події та повідомлення, які виникають під час виконання програми. Logger дозволяє збирати ці повідомлення та події для подальшого аналізу та налагодження.

## Створення логера (Creating a Logger)

Для створення логера необхідно імпортувати модуль `logging` і використовувати його функції та класи.

```python
import logging
```

# Створення об'єкту логування
```python
logger = logging.getLogger('my_logger')
``` 


## Встановлення

Встановити бібліотеку можна за допомогою `pip`:

```bash
pip install logger
``` 
## Використання

```python
import logger
``` 

# Ініціалізувати об'єкт логування
```python
log = logger.Logger('my_app.log')
``` 

# Додати повідомлення
```python
log.info('Це інформаційне повідомлення')
log.warning('Це попередження')
log.error('Це помилка')
``` 

# Закрити лог-файл
```python
log.close()
``` 

## Додаткові можливості

- Логування на рівні інформації, попереджень та помилок.
- Запис повідомлень в лог-файл.
- Підтримка різних форматів лог-файлу (текстовий, JSON тощо).
- Конфігурування параметрів логування (рівень логування, формат повідомлень тощо).
- Більш детальну інформацію про використання можна знайти у документації.

## Приклад використання
```python
import logger

# Ініціалізувати об'єкт логування
log = logger.Logger('my_app.log')

# Додати повідомлення
log.info('Це інформаційне повідомлення')

# Закрити лог-файл
log.close()
``` 

## Рівні логування (Log Levels)

Logger підтримує різні рівні логування, що дозволяють відокремлювати повідомлення за їх важливістю. Доступні рівні логування включають:
```python
- DEBUG: найнижчий рівень, використовується для налагодження та детального виведення інформації.
- INFO: рівень інформаційних повідомлень, які слугують для сповіщення про події в програмі.
- WARNING: рівень попереджень, що вказують на можливі проблеми або некритичні помилки.
- ERROR: рівень помилок, які відображають серйозні проблеми в програмі.
  ``` 

## Логування помилок та повідомлень (Logging Errors and Messages) ##
```python
logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це інформаційне повідомлення')
logger.warning('Це попередження')
logger.error('Це помилка')
``` 

## Встановлення рівня логування (Setting the Log Level)
За замовчуванням, рівень логування встановлений на WARNING. Щоб змінити цей рівень, використовуйте метод `setLevel()`:

`logger.setLevel(logging.DEBUG)`
  
## Логування в файл (Logging to a File)
Logger дозволяє зберігати повідомлення в лог-файлі. Для цього необхідно налаштувати об'єкт `FileHandler` та додати його до логера:

```python
file_handler = logging.FileHandler('my_app.log')
logger.addHandler(file_handler)
``` 

## Логування на консоль та в файл (Logging to Console and File)
Щоб виводити повідомлення одночасно на консоль та в лог-файл, використовуйте `StreamHandler`:

```python  
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('my_app.log')
logger.addHandler(console_handler)
logger.addHandler(file_handler)
``` 

## Форматування логів (Formatting the Logs)
Логер дозволяє налаштовувати формат виведення повідомлень. Використовуйте метод Formatter для вказівки потрібного формату:
```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
``` 

## Використання basicConfig()
Існує ще один спосіб налаштування логера - за допомогою методу `basicConfig()`. Цей метод автоматично налаштовує об'єкт логування з вказаними параметрами:
```python
logging.basicConfig(filename='my_app.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
``` 
