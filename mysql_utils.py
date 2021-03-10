import json
import nlp_utils as nlp
from datetime import date
import mysql.connector as connector
from app_config import MYSQL_PASSWORD

def get_conn_cursor():
    conn = connector.connect(
        host='localhost',
        database='euva',
        user='root',
        password=MYSQL_PASSWORD)
    cursor = conn.cursor()
    return conn, cursor

def close_conn_cursor(conn, cursor):
    cursor.close()
    conn.close()

def execute(cmd, fetch=None, commit=False):
    returnable = None
    conn, cursor = get_conn_cursor()
    cursor.execute(cmd)
    if commit:
        conn.commit()
    if fetch == 'all':
        returnable = cursor.fetchall()
    elif fetch == 'one':
        returnable = cursor.fetchone()
    close_conn_cursor(conn, cursor)
    return returnable

def create_user(userinfo):
    _id = userinfo['id']
    for table in execute('SHOW TABLES', fetch='all'):
        if table[0].replace('user_', '') == _id: return
    execute(f'CREATE TABLE user_{_id}(journal_date DATE NOT NULL PRIMARY KEY, journal_entry TEXT NOT NULL, sentiment_score DECIMAL(4, 2) ZEROFILL NOT NULL)', commit=True)

def today_journal_blocks(userinfo):
    _id = userinfo['id']
    journal_entry = execute(f'SELECT journal_entry FROM user_{_id} WHERE journal_date="{date.today()}"', fetch='one')
    if not journal_entry is None:
        journal_entry = nlp.replace_journal(journal_entry[0], (1, 0)).replace('&nbsp;', ' ')
        journal_entry = json.loads(journal_entry)
        if journal_entry['blocks']:
            return execute(f'SELECT journal_entry FROM user_{_id} WHERE journal_date="{date.today()}"', fetch='one')[0]
    return str({'blocks': [{'type': 'header', 'data': {'text': 'Journal - ' + date.today().strftime('%B %d, %Y'), 'level': 2}}]})

def save_journal_entry(userinfo, form):
    _id = userinfo['id']
    journal_entry = json.loads(form['journal-entry-input'].replace('&nbsp;', ' '))
    del journal_entry['time']
    del journal_entry['version']
    sentiment_score = nlp.sentiment_score(journal_entry)
    journal_entry = nlp.replace_journal(json.dumps(journal_entry), (0, 1))
    for journal_date in execute(f'SELECT journal_date FROM user_{_id}', fetch='all'):
        if journal_date[0].strftime('%Y-%m-%d') == str(date.today()):
            execute(f'UPDATE user_{_id} SET journal_entry="{journal_entry}", sentiment_score={sentiment_score} WHERE journal_date="{date.today()}"', commit=True)
            return True
    execute(f'INSERT INTO user_{_id}(journal_date, journal_entry, sentiment_score) values("{date.today()}", "{journal_entry}", {sentiment_score})', commit=True)
    return True

def journal_from_date(user_id, journal_date):
    journal_dates = execute(f'SELECT journal_date FROM user_{user_id}', fetch='all')
    for db_date in journal_dates:
        if db_date[0].strftime('%Y-%m-%d') == journal_date:
            return execute(f'SELECT journal_entry, sentiment_score FROM user_{user_id} WHERE journal_date="{journal_date}"', fetch='one')
    return 'Invalid Date'

def journal_from_dates(user_id, dates):
    journal_dates = execute(f'SELECT journal_date FROM user_{user_id}', fetch='all')
    for journal_date in journal_dates:
        for date in dates:
            if date.strftime('%Y-%m-%d') == journal_date[0].strftime('%Y-%m-%d'):
                return date.strftime('%Y-%m-%d')

def last_five_journals(userinfo):
    _id = userinfo['id']
    dataset = execute(f'SELECT journal_date, sentiment_score FROM user_{_id}', fetch='all')
    for i in range(len(dataset)):
        dataset[i] = list(dataset[i])
        dataset[i].append(dataset[i][0].strftime('%b %d'))
        dataset[i][0] = dataset[i][0].strftime('%Y-%m-%d')
        dataset[i][1] = float(dataset[i][1])
    return dataset

def sentiment_scores(userinfo):
    _id = userinfo['id']
    return [float(s[0]) for s in execute(f'SELECT sentiment_score FROM user_{_id}', fetch='all')]

def latest_journal_date():
    return execute('SELECT max(journal_date) from user_109041459781692369999', fetch='one')[0].strftime('%Y-%m-%d')
