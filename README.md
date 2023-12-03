# Python_CurrencyChart-PyQt6-VS
Python PyQt6 project VS Code - generating report from DB
(Oracle, MS SQL, Azure SQL, PostgreSQL, MySQL, MariaDB, IBM DB2, Firebird, SQLite, Amazon Aurora MySQL, Amazon Aurora PostgreSQL, MongoDB, Cassandra).
Creation of schedules of NBU exchange rates by year to monitor change trends.

IDE - Visual Studio Code

1) Add Extensions
-> Python
-> Pylance
-> Qt for Python
-> Ruff

У командному рядку терміналу CMD
2) Додаємо бібліотеки
-> pip install PyQt6
-> pip install python-dateutil
-> pip install matplotlib
-> pip install reportlab

-> pip install psycopg2 (PostgreSQL)
-> pip install mysql-connector-python (MySQL)
-> pip install mariadb (MariaDB)
-> pip install oracledb (Oracle)
-> pip install pyodbc (MSSQL)
-> pip install pymssql (MSSQL)
-> pip install ibm_db (IBM DB2) max python 3.11
-> pip install fdb (Firebird) + для Windows установить Firebird Client Library (https://firebirdsql.org/en/firebird-4-0/)
-> pip install pymongo (MongoDB)
-> pip install cassandra-driver (Cassandra)
-> pip install pyasyncore (Cassandra)


3) Qt Designer
Окремо встановлюємо:
-> https://build-system.fman.io/qt-designer-download
або:
-> pip install pyqt6-tools
   Запускаємо -> pyqt6-tools designer


4) Перетворення *.ui файлу у файл типу *.py
-> На файлі MainWindow.ui - права клавіша миші - Compile Qt UI File (uic)

---------------------------------------------------
Створення EXE файла
1) Ставимо pyinstaller
-> pip install pyinstaller

2) Запускаємо файл .\CurrencyChart_create_EXE_file.bat для автоматичної збірки exe файла
Сформований файл буде розташований у каталозі \dist\

---------------------------------------------------------------------------------
Завантаження первинних курсів
---------------------------------------------------------------------------------
- https://bank.gov.ua/control/uk/curmetal/currency/search/form/period
- Вказати період та експорт JSON
