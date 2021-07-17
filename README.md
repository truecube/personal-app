I am going to type all the steps I take to create and deploy this app to Heroku.  This way I don't have to go to youtube and watch the saaaaaaaammmmmeeee video a million times.
Steps: 
1. Assuming you had already installed pipenv (by running command pip install pipenv), enter virutal env by typing command pipenv shell
2. install the following: 
    - pipenv install flask
    - pipenv install psycopg2-binary
    - pipenv install flask-sqlalchemy
    - pipenv install gunicorn

heroku commands: 
heroku login
heroku create yuvapersonalapp
heroku addons:create heroku-postgresql:hobby-dev --app personal-app
heroku config --app yuvapersonalapp (gives you DATABASE_URL)
heroku pg:psql --app yuvapersonalapp

creating tables: 
using pgadmin4 create 'personal-app' database
enter python terminal and type: 
    from app import db
    db.create_all()
git push heroku master    