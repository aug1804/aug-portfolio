@rem inic.bat inicialização-Python-Django.bat

@rem - Windows+R --> cmd

cd C:\Users\aug18\aug\python\meu_projeto6
pause

workon ve
pause

python manage.py makemigrations portal6
pause

python manage.py migrate
pause

python manage.py runserver

@rem *** Fim ***