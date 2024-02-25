## Instructions
1) **Download the repository zip file**
2) **Open a CMD terminal in the repo location**
3) **Create a Python Virtual Environment**
```
python -m venv venv
```
4) **Activate the virtual environment**
```
venv\Scripts\activate.bat
```
5) **Install all dependencies**
```
pip install -r requirement.txt
```

6) Run the following commands
```
python manage.py migrate --run-syncdb 
python manage.py makemigrations predictor
python manage.py migrate predictor
```

7) **Run server**
```
python manage.py runserver
```


