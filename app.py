from flask import Flask, render_template, request, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
# from werkzeug.utils import redirect
# from werkzeug.wrappers import request

client = MongoClient('mongodb+srv://Admin:kHwGiTilGkc8OEq4@cluster0.anqw0.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.get_default_database()
accounts = db.accounts

app = Flask(__name__)

#stock accounts for demo
eg_dono = {'amount': '1,000,000.00', 'charity': 'The best charity', 'date': 'everyday', 'mission' : 'Helping people in need.'}


no_user = {
  'username': 'Login',  
}
donor_user = {
'username': 'donor',
'password': 'password',
'first_name': 'John',
'last_name': 'Doe',
'donations': [eg_dono]
}
#add new charity
charity_user = {
'username': 'charity',
'password': 'password',
'donations': eg_dono,
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
  if account == None:
      abort(404)
  print(account)
  return render_template('account_profile.html', account = donor_user)
  
@app.route('/donate-now/')
def donate():
    return render_template('donate_now.html')
 
@app.route('/donation-form/')
def donation_form():
    return render_template('donation_form.html')
 























if __name__ == '__main__':
    app.run(debug=True)