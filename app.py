from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

@app.route('/')
def home_page():
    """Return homepage."""
    return render_template('home_index.html')

@app.route('/learn-more/')
def learn_more():
    return render_template('learn_more.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('create-account')
def new_account():
    #submit new account object
    #log user in
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)