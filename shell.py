#import subprocess as s
#s.call('start',shell=True)
import os
try:
    os.system('cmd /c "virtualenv venv & pip install django & django-admin startproject worldCountries . & python manage.py startapp new_app"')
except:
    print('nothing')
