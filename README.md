### Парсер заказов | TParser

Скрипт написан для небольшой экскурсионной мастерской и предназначен для получения данных о заказах экскурсий с
платформы Трипстер. Он автоматизирует процесс составления уведомлений и их рассылку туристам: легко извлекает информацию
о ближайших оплаченных экскурсиях, формирует сообщения на основе этой информации и отправляет уведомления туристам на
WhatsApp.
В случае, если появились новые "last minute" заявки после рассылки сообщений, предусмотрена возможность повторного сбора
заказов, полученных после конкретного часа.

-------------

####Основная функциональность

- Получение списка всех будущих заказов
- Фильтрация оплаченных заказов на сегодня и завтра
- Извлечение необходимых данных для формирования сообщений

-------------

####Использование

- Клонирвать репозиторий с GitHub:
  `git clone https://github.com/nataliadudina/tripster_parser`

- Установить виртуальное окружение и Poetry:
  `pip install poetry`

- Установить зависимости:
  `poetry install`

- Запустить скрипт из терминала:
  `poetry run python main.py`

-------------

####Структура проекта
Проект состоит из следующих компонентов:

1) Модуль 'tparser.py' с классом Парсера, который имеет три метода:

- получение списка всех будущих заказов,
- фильтрация ближайших оплаченных заказов (на сегодня и завтра),
- извлечение необходимых данных для формирования сообщений.

2) Три сервисных модуля:

- 'utils.py': вспомогательные функции
- 'servicies.py': функция отправки сообщения на WhatsApp
- 'texts.py': содержит сами тексты сообщений

3) Основной модуль с функцией 'main.py' для запуска скрипта.

------------
####Техническая информация

- Python 3.11
- Библиотеки:
    - `requests`: HTTP-запросы
    - `pywhatkit`: работа с переменными окружения
    - `environs`: управление переменными окружения
    - `flake8`: проверка кода на соответствие PEP 8
    - `isort`: форматирование импортов в файлах
    - `mypy`: статический анализатор типов
  -------------

#### Настройка окружения

Для корректной работы скрипта необходимо создать файл .env в корневой директории проекта со следующим содержимым:
<pre>
TOKEN  = ваш_персональный_token 
URL = URL_API
</pre>

------------

#### Примечание

* Парсер может быть использован как часть системы управления заказами или для интеграции с другими сервисами.
* Для работы скрипта требуется доступ к API Трипстера:
  [Получить токен для доступа к API](https://experience.tripster.ru/help_center/guides/orders/how_to_work/63/)
  [Документация](https://docs.google.com/document/d/1AoS7hvlphYbDc7Bi3lTVLFde_zKa9KgQZH-AiwPz32k/edit?tab=t.0#heading=h.p8az02kk7rud)