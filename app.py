from flask import Flask, render_template, request, abort, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.utils import redirect


client = MongoClient('mongodb+srv://Admin:kHwGiTilGkc8OEq4@cluster0.anqw0.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.get_default_database()
accounts = db.accounts

app = Flask(__name__)

#eg_dono = {'amount': '1,000,000.00', 'charity': 'The best charity', 'date': 'everyday', 'memo' : 'Helping people in need.'}

no_user = {
  'username': 'Login',  
}
donor_user = {
'username': 'donor',
'password': 'password',
'first_name': 'John',
'last_name': 'Doe',
'donations': []
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

#------------------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login_submit():
  account_username = request.form.get('username')
  account = accounts.find_one({'username': account_username})
  if account == None:
      abort(404)
  return redirect('/account_profile/'+ account_username)
  
@app.route('/account_profile/<string:account_username>', methods=['GET'])
def account_profile(account_username):
    account = accounts.find_one({'username': account_username})
    return render_template('account_profile.html', account = account)


#------------------------------------------------------------------------

 
@app.route('/<string:account_username>/donate-now/')
def choose_charity(account_username):
    account = accounts.find_one({'username': account_username})
    return render_template('featured_charities.html', account = account)

@app.route('/<string:account_username>/donate-now/<string:charity>-donation-form')
def donation_form(account_username, charity):
    account = accounts.find_one({'username': account_username})

    if charity == 'st-jude':
        charity = {
            'name': "St. Jude Children's Research Hospital"
        }
    elif charity == 'ACF':
        charity = {
            'name': "Alaska Conservation Foundation"
        }
    elif charity == 'unicef':
        charity = {
            'name': "United States Fund for UNICEF"
        }
    
    return render_template('donation_form.html', account = account, charity = charity)


@app.route('/<string:account_username>/donate-now/<string:charity>-donation-form', methods=['GET', 'POST'])
def donation_form_submit(account_username, charity):
    account = accounts.find_one({'username': account_username})

    if charity == 'st-jude':
        charity = {
            'abbrev': 'st-jude',
            'name': "St. Jude Children's Research Hospital",
            'mission': "Save children"
        }
    elif charity == 'ACF':
        charity = {
            'abbrev': 'ACF',
            'name': "Alaska Conservation Foundation",
            'mission': 'preserve Alaskan Wildlife'
        }
    elif charity == 'unicef':
        charity = {
            'abbrev': 'unicef',
            'name': "United States Fund for UNICEF",
            'mission': "Save children"
        }
    donation = {
        'abbrev': charity['abbrev'],
        'charity': charity['name'],
        'amount': request.form.get('amount'),
        'date': 'today',
        'memo': charity['mission']
    }

    account['donations'].append(donation)
    accounts.save(account)

    return redirect(('/account_profile/' + account_username))

@app.route('/account_profile/<string:account_username>/<string:charity_name>/delete', methods=['GET','POST'])
def delete_donation(account_username, charity_name):
    account = accounts.find_one({'username': account_username})

    for donation in account['donations']:
        if donation['charity'] == charity_name:
            account['donations'].remove(donation)
            accounts.save(account)

    return redirect(('/account_profile/' + account_username))

@app.route('/account_profile/<string:account_username>/<string:charity_name>/update', methods=['GET','POST'])
def update_donation(account_username, charity_name):
    account = accounts.find_one({'username': account_username})

    for donation in account['donations']:
        if donation['charity'] == charity_name:
            charity_name = donation['abbrev']
            account['donations'].remove(donation)
            accounts.save(account)
            return redirect('/'+account_username+'/donate-now/'+charity_name+'-donation-form')

    return redirect(('/account_profile/' + account_username))

#----------------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET','POST'])
def create_account():
    account = {
        'username': request.form.get('Username'),
        'password': request.form.get('Password'),
        'first_name': request.form.get('First Name'),
        'last_name': request.form.get('Last Name'),
        'donations': []
    }
    accounts.insert_one(account)
    return redirect(('/account_profile/' + account['username']))

@app.route('/account_profile/<string:account_username>/delete', methods=['POST'])
def delete_account(account_username):
    account = accounts.find_one({'username': account_username})
    accounts.delete_one(account)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)