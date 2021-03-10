import chatbot
import requests
import app_config
from flask import *
import nlp_utils as nlp
from datetime import date
import mysql_utils as mysql
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = app_config.APP_SECRET_KEY
CORS(app)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'userinfo' in session:
        jes = False
        mysql.create_user(session['userinfo'])
        date_today = date.today().strftime('%B %d, %Y')
        if request.method == 'POST':
            jes = mysql.save_journal_entry(session['userinfo'], request.form)
        sentiment_scores = mysql.sentiment_scores(session['userinfo'])
        last_five_journals = mysql.last_five_journals(session['userinfo'])
        return render_template(
            'user.html',
            jes=jes,
            date=date_today,
            userinfo=session['userinfo'],
            sentiment_scores=sentiment_scores,
            last_five_journals=last_five_journals,
            sentiment_scores_len=len(sentiment_scores),
            last_five_journals_len=len(last_five_journals),
            latest_journal_date=mysql.latest_journal_date(),
            journal_blocks=mysql.today_journal_blocks(session['userinfo'])
        )
    return redirect('/login/user')

@app.route('/api/sentiment_score/<string:text>')
def sentiment_api(text):
    return jsonify({'sentiment_score': nlp.sentiment_score_api(text)})

@app.route('/api/chatbot/<string:message>')
def chatbot_api(message):
    message, journal = chatbot.response(message, session['userinfo'])
    print(message, journal)
    return jsonify({'message': message, 'journal': journal})

@app.route('/api/journal_from_date/<string:user_id>/<string:journal_date>')
def journal_from_date(user_id, journal_date):
    journal = mysql.journal_from_date(user_id, journal_date)
    if journal == 'Invalid Date':
        return jsonify({'journal_entry': journal})
    return jsonify({'journal_entry': journal[0], 'sentiment_score': float(journal[1])})

@app.route('/login/<string:redirect_url>')
def login(redirect_url):
    session['redirect_url'] = redirect_url
    return redirect(f'https://accounts.google.com/o/oauth2/v2/auth?scope={app_config.SCOPE}&access_type=offline&include_granted_scopes=true&response_type=code&redirect_uri={app_config.DOMAIN}authorized&client_id={app_config.GOOGLE_CLIENT_ID}')

@app.route('/authorized')
def authorized():
    response = requests.post('https://oauth2.googleapis.com/token', data={
        'client_id': app_config.GOOGLE_CLIENT_ID,
        'client_secret': app_config.GOOGLE_CLIENT_SECRET,
        'code': request.args.get('code'),
        'grant_type': 'authorization_code',
        'redirect_uri': f'{app_config.DOMAIN}authorized'}).json()
    access_token = response['access_token']
    userinfo = requests.get(f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}').json()
    session['userinfo'] = userinfo
    return redirect(session['redirect_url'])

if __name__ == '__main__':
    app.run(debug=True)
