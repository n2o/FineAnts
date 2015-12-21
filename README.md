# FineAnts

```bash
        |     |
         \   /
          \_/
     __   /^\   __
    '  `. \_/ ,'  `
         \/ \/     
    _,--./| |\.--._  
 _,'   _.-\_/-._   `._
      |   / \   |
      |  /   \  |
     /   |   |   \
   -'    \___/    `-
```

## Installation

*This is a python3 project.*

Set up a new virtualenv for this project:

```bash
$ mkvirtualenv --python=/usr/bin/python3 FineAnts
```

and install Django:

```bash
$ workon FineAnts
$ pip install -r requirements.txt
```

### Initialize new database
Start the server to create an empty database and migrate the Django models into the newly created database:

```bash
$ python manage.py runserver
# STRG + C to kill the server
$ python manage.py migrate
```

#### Create superuser
Create a superuser (= administrator) for your database:

```bash
$ python manage.py createsuperuser
```

### Start the application
The steps above are only necessary, if you have not set up your own database yet. Start the integrated webserver this way:

```bash
$ python manage.py runserver
```
