# PorableNPC

Backend application simulating textual and voice interaction with NPCs in role-playing games. It is a subject of my engineering thesis.

It cooperates with the mobile application [portable-npc](https://github.com/szymonborda/portable-npc)

## Development

* Create .env file based on .env.example
  ```
  $ cp .env.example .env
  ```
* Create a python virtual environment and install dependencies
  ```
  $ python3 -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```
* Run local database using docker-compose
  ```
  $ docker-compose up
  ```
* Apply migrations
  ```
  $ python manage.py migrate
  ```
* Run the application
  ```
  $ python manage.py runserver
  ```
