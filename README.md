# sensors

This project is the monitoring system for collecting and analyzing data from sensors 


**Run project**

1. Install python

> sudo apt-get install python-pip

Check python version
pip -V
pip 22.3.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)

2. Instal virtual env

> pip install virtualenv

3. Create virtual env
 
> virtualenv <name>
4. install libs (mentioned in Libs block)
5. run env [ source env/bin/activate ]
6. run server python 
> cd sensors 

> python manage.py runserver 
or 
> python3 manage.py runserver 
7. go to http://127.0.0.1:8000
8. to open admin panel - go to http://127.0.0.1:8000/admin/
9. to run tests [ python manage.py test djangoapp/tests ]

-------

**LIBS**

Install needed libraries

> python -m pip install Django

> pip install djangorestframework

> pip install asgiref

> pip install dnspython

> pip install pytz

> pip install sqlparse

> pip install -U scikit-learn

> pip install pandas

> pip install matplotlib

> pip install numpy

----
Lib versions

- asgiref==3.5.2
- Django==4.1.3
- djangorestframework==3.14.0
- dnspython==2.3.0
- pytz==2022.7
- sqlparse==0.2.4
- pandas==1.5.3
- numpy==1.24.1
- scikit-learn==1.2.1
- matplotlib==3.6.3




