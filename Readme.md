# Django Project Example

### 1. create project
```
django-admin startproject <projectname>
```

### 2. Running the Django Project
```
cd <projectname>
py manage.py runserver
```

### 3. Django Admin INterface

To access it at browser use '/admin' at a local machine like localhost::8000/admin/ and ishows the following output:

- Create an Admin user
```
py manage.py migrate
py manage.py createsuperuser
```