from transformers import pipeline

sentiment_analysis = pipeline('sentiment-analysis')

journal_block_replacements = [('\'', ':sq:'), ('\"', ':dq:')]

def sentiment_score(journal_entry):
    text = ''
    for block in journal_entry['blocks']:
        text += block['data']['text'] + ' '
    return sentiment_score_api(text)

def sentiment_score_api(text):
    sentiment = sentiment_analysis(text)[0]
    sentiment['score'] = sentiment['score'] * 100
    if sentiment['label'] == 'NEGATIVE':
        sentiment['score'] = 100 - sentiment['score']
    return round(sentiment['score'], 2)

def replace_journal(journal_entry, order):
    for replacement in journal_block_replacements:
        journal_entry = journal_entry.replace(replacement[order[0]], replacement[order[1]])
    return journal_entry
