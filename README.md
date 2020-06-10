# TODO app for learning

### Base requirements
python 3.7


### Set up enviroment. Run project
- create project **todo_app**:
    `$ mkdir todo_app`
    `$ cd todo_app`
- clone repository from:
    `git clone https://github.com/kasianD/flask_todo.git .`
- create and activate virtualenv:
    `$ python3 -m venv .venv`
    `$ source .venv/bin/activate`
- install the requirements:
    `$ pip install -r requirements.txt`
- create database in postgres, below is an example:
	`$ sudo -u postgres psql`
	`postgres=# create database flask_todo_db;`
	`postgres=# create user todo_user with password 'todo_user_pass';`
	`postgres=# grant all on database flask_todo_db to todo_user;`
- export .evn valriables:
	`$ export FLASK_ENV=development`
	`$ export FLASK_APP=app`
	`$ export DATABASE_URI="postgresql://todo_user:todo_user_pass@localhost/flask_todo_db"`
	`$ export SECRET_KEY=<some_secret_key>`
- make migrations
    `$ db flask init`
    `$ db flask upgrade`
- run server
    `$ python3 run.py` (will be run on [localhost:5000](localhost:5000))
