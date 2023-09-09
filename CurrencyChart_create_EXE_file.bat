@ECHO OFF
set PYTHONPATH="c:\Users\artem\AppData\Local\Programs\Python\Python311"

rd /s /q build
rd /s /q dist
del /q main.spec

pyinstaller -y --additional-hooks-dir=. --hidden-import ibm_db_sa.ibm_db --hidden-import ibm_db_dbi --hidden-import ibm_db --add-binary "%PYTHONPATH%\Lib\site-packages\ibm_db_dlls\ibm_db.dll;.\ibm_db_dlls" --add-data="%PYTHONPATH%\Lib\site-packages\clidriver;.\clidriver" --onefile --icon=icon.ico main.py

pause
