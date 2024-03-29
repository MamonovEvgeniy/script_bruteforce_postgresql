# bruteforce_postgresql

<h3 align="center">Файл <code>pass.txt</code> положить рядом с исполняемым скриптом</h1>

___________________________________________________________

Скрипт поможет вспомнить пароль PostgreSQL сервера, если вы его забыли🤗

Скрипт запускатеся из консоли следующим образом:

<code>postgresql_bruteforce.py -h 192.168.0.22 -p 5432 –с path/to/file</code>

где:

•	<code>-h</code> – обязательный параметр - хост (доменное имя или IPv4-адрес), на котором запущен PostgreSQL сервер

•	<code>-p</code> – опциональный параметр - порт, на котором запущен PostgreSQL сервер. Значение по умолчанию: 5432

•	<code>-c</code> – обязательный параметр - путь до файла с данными для перебора (логин/пароль)

В файле с данными для перебора, логины и пароли указаны через пробел по одной паре на каждой строке:

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=10000&pause=500&color=A862F7&center=%D0%BB%D0%BE%D0%B6%D1%8C&vCenter=%D0%BB%D0%BE%D0%B6%D1%8C&multiline=true&repeat=%D0%BB%D0%BE%D0%B6%D1%8C&width=435&lines=%3Clogin%3E+%3Cpass%3E%5Cn;%3Clogin%3E+%3Cpass%3E%5Cn;...)](https://git.io/typing-svg)


Результат выполнения скрипта выводится в консоль и содержит следующее:

•	Информацию об успешно подобранных учетных данных

•	Сообщения об ошибках в ходе работы (если такие будут)

•	Сообщение, если не удалось подобрать ни один логин/пароль

•	Общее время работы скрипта

___________________________________________________________

Пример запуска:

<code>python postgresql_bruteforce.py -h localhost -c pass.txt</code>
  
Результат запуска:
<pre>
Успешно подобрано 1 УЗ:
postgres postgre

Ошибки при попытке подключения:
Ошибка подключения к БД postgres с login и pass: login1/password1

Ошибка подключения к БД postgres с login и pass: login2/password2

Ошибка подключения к БД postgres с login и pass: login3/password3

Время выполнения скрипта: 0.22508740425109863 секунд
</pre>
