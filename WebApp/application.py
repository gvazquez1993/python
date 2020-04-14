from flask import flask        #In this python file we want to use that Flask Module

app = Flask(__name__) # I want to create a new web app, and i want this web app to be a flask web app. (__name__) Represent this current file. that this file is going to represent my web app

@app.route("/")         #At app.route /, this / represent the default page
def index():
    return "Hello, world!"

#And what line 5 is saying, app.route, is that when the user go just slash on my website, goes to that default route,
#the function inmmediately below it is the function that i want to run.
