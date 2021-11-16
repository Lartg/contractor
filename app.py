from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

#remove when implemented db
donor_user = {
'username': 'donor',
'password': 'password',
'donations': []
}

charity_user = {
'username': 'charity',
'password': 'password',
'donations': []
}

advisor_user = {
'username': 'advisor',
'password': 'password',
'clients': []
}

users = [donor_user, charity_user, advisor_user]

@app.route('/')
def home_page():
    """Return homepage."""
    return render_template('home_index.html')

# NAVBAR ROUTES ---------------------------------------------------------
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/CW/')
def return_home():
    """Return homepage."""
    return render_template('home_index.html')

@app.route('/featured-charities/')
def featured_charities():
    return render_template('featured_charities.html')
#------------------------------------------------------------------------
@app.route('/learn-more/')
def learn_more():
    return render_template('learn_more.html')

@app.route('/create-account/')
def new_account():
    #submit new account object
    #log user in
    #we are ingnoring this for now, creating 3 super accounts to demo project
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)