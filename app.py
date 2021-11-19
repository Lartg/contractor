from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId
# from werkzeug.utils import redirect
# from werkzeug.wrappers import request

client = MongoClient('mongodb+srv://Admin:kHwGiTilGkc8OEq4@cluster0.anqw0.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.get_default_database()
accounts = db.accounts

app = Flask(__name__)

#stock accounts for demo
eg_dono = {'amount': 1000000, 'charity': 'The best charity', 'date': 'everyday'}

donor_user = {
'username': 'donor',
'password': 'password',
'donations': eg_dono,
}
#add new charity
charity_user = {
'username': 'charity',
'password': 'password',
'donations': [],
'donors': []
}
#view donor account
advisor_user = {
'username': 'advisor',
'password': 'password',
'clients': []
}
accounts.insert_one(donor_user)
accounts.insert_one(charity_user)
accounts.insert_one(advisor_user)
#, charity_user, advisor_user


@app.route('/')
def home_page():
    """Return homepage."""
    return render_template('home_index.html')

# NAVBAR ROUTES ---------------------------------------------------------
@app.route('/login/')
def login_page():
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

#------------------------------------------------------------------------

@app.route('/login', methods=['POST'])
def login_submit():
  account_username = request.form.get('username')
  account = accounts.find_one({'username': account_username})
  print(account)
  return render_template('account_profile.html', account = account)
  

 
   























if __name__ == '__main__':
    app.run(debug=True)