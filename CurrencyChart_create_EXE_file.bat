@ECHO OFF
set PYTHONPATH="c:\Users\artem\AppData\Local\Programs\Python\Python312"

rd /s /q build
rd /s /q dist
del /q main.spec

pyinstaller --noconsole -y --additional-hooks-dir=. --onefile --icon=icon.ico main.py

pause
