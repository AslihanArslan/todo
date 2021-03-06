# Django Todo App

```
cd todo/
```

```
pipenv install
```
If there is an error about psycopg2 error:

![Error](https://github.com/AslihanArslan/todo/blob/master/docs/error.jpeg)


You can use this command:

```
sudo apt-get install libpq-dev
```

After this command, try again this command

```
pipenv install
```

```
pipenv shell
```


If there is no postresql in your computer, please install postgresql:

```
sudo apt update & sudo apt install postgresql postgresql-contrib
```

Check service is working or not: 

```
systemctl status postgresql.service
```

Open postgresql in your computer write these codes

```
sudo su - postgres
```

```
psql
```

```
CREATE DATABASE tododb;
```

```
CREATE USER aslihan  WITH PASSWORD '123456';
```

```
\q
```

```
exit
```

Make migrate project

```
python manage.py migrate
```

Run code

```
python manage.py runserver
```
