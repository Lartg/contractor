from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    """Return homepage."""
    return render_template('home_index.html')

@app.route('/learn-more')
def learn_more():
    return render_template('learn_more.html')
if __name__ == '__main__':
    app.run(debug=True)