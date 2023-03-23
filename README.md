# bruteforce_postgresql

<h1 align="center">Файл pass.txt положить рядом с исполняемым скриптом</h1>
___________________________________________________________

Скрипт поможет вспомнить пароль PostgreSQL сервера, если вы его забыли.

Скрипт запускатеся из консоли следующим образом:

postgresql_bruteforce.py -h 192.168.0.22 -p 5432 –с path/to/file

где:

•	h – обязательный параметр - хост (доменное имя или IPv4-адрес), на котором запущен PostgreSQL сервер

•	p – опциональный параметр - порт, на котором запущен PostgreSQL сервер. Значение по умолчанию: 5432

•	c – обязательный параметр - путь до файла с данными для перебора (логин/пароль)

В файле с данными для перебора, логины и пароли должны быть указаны через пробел по одной паре на каждой строке:

<login> <pass>\n

<login> <pass>\n

…

Результат выполнения скрипта выводится в консоль и содержит следующее:

•	Информацию об успешно подобранных учетных данных

•	Сообщения об ошибках в ходе работы (если такие будут)

•	Сообщение, если не удалось подобрать ни один логин/пароль

•	Общее время работы скрипта

___________________________________________________________

Пример запуска:

python postgresql_bruteforce.py -h localhost -c pass.txt
  
Результат запуска:

Успешно подобрано 1 УЗ:
postgres postgre

Ошибки при попытке подключения:
Ошибка подключения к БД postgres с login и pass: login1/password1

Ошибка подключения к БД postgres с login и pass: login2/password2

Ошибка подключения к БД postgres с login и pass: login3/password3

Время выполнения скрипта: 0.22508740425109863 секунд

