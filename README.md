# sensors

This project is the monitoring system for collecting and analyzing data from sensors 


**Run project**

1. Install python

> sudo apt-get install python-pip

Check python version
> pip -V

pip 22.3.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)

2. Install virtual env

> pip install virtualenv

3. Create virtual env
 
> virtualenv \<name>
4. runnning env:
go to folder with env and run
> source bin/activate 
5. install libs (mentioned in Libs block)
6. run server python 
> cd sensors 

> python manage.py runserver 

or 

> python3 manage.py runserver 
7. go to http://127.0.0.1:8000
8. to open admin panel - go to http://127.0.0.1:8000/admin/
9. to run tests 
> python manage.py test djangoapp/tests


To run on virtualbox you need to share your local server with ngrok after you run a local server.

1. download ngrok from https://dashboard.ngrok.com/get-started/setup

2. connect account 
> ngrok config add-authtoken 2IrBFk2X8HyHxYal9G94zzXtWqI_2yVF1hmoV5qfARbShAGd9

3. run server
> ngrok http 8000

4. add to file settings.py AllowedHosts new host from ngrok 
ALLOWED_HOSTS = [‘…host…’]

5. change urls in all .py files on raspberry os
url = ‘…host…’;

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
Libs versions

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




