# sensors

Check python version
pip -V
pip 22.3.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)

Install needed libraries

with comand 
> pip install 

example 
> pip install djangorestframework

- pipenv
- asgiref==3.5.2
- Django==4.1.3
- djangorestframework==3.14.0
- djongo==1.3.6
- dnspython==2.3.0
- pymongo==4.3.3
- pytz==2022.7
- sqlparse==0.2.4


Run project
1. create environment "env" [ source env/bin/activate ]
2. run env [ source env/bin/activate ]
3. run server python 
[ cd sensors ]
[ python manage.py runserver ] or [ python3 manage.py runserver ] 
4. go to http://127.0.0.1:8000/measurements/
