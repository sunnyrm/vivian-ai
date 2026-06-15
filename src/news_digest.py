import os
import logging
import feedparser
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load .env from project root (one level up from src/)
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

FEED_URL = 'https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en'
TOP_N = 10

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs', 'vivian.log')

logging.basicConfig(
    filename=os.path.abspath(LOG_PATH),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


def shorten_url(url):
    try:
        r = requests.get(f'https://tinyurl.com/api-create.php?url={url}', timeout=10)
        if r.ok and r.text.startswith('https://tinyurl.com'):
            return r.text.strip()
    except Exception:
        pass
    return url


def fetch_stories():
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; RSS reader)'}
    try:
        response = requests.get(FEED_URL, headers=headers, timeout=10)
        response.raise_for_status()
        feed = feedparser.parse(response.content)
        stories = []
        for entry in feed.entries:
            link = entry.get('link', '')
            if not link:
                continue
            stories.append({
                'title': entry.get('title', '').strip(),
                'link': shorten_url(link),
            })
        top = stories[:TOP_N]
        logging.info(f'Fetched {len(feed.entries)} stories → top {len(top)} selected')
        for i, s in enumerate(top, 1):
            logging.info(f'  {i}. {s["title"]}')
        return top
    except Exception as e:
        logging.error(f'Feed failed: {e}')
        return []


def format_message(stories):
    today = datetime.now().strftime('%A, %d %B %Y')
    lines = [
        '🌅 Good morning! Vivian here.',
        f'📅 {today}',
        '',
        '📰 TOP STORIES',
    ]
    for i, s in enumerate(stories, 1):
        lines.append('')
        lines.append(f'{i}. {s["title"]}')
        lines.append(f'🔗 {s["link"]}')
    lines.append('')
    lines.append('— Vivian 🤖')
    return '\n'.join(lines)


def send_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'disable_web_page_preview': True,
    }
    response = requests.post(url, json=payload, timeout=10)
    if response.ok:
        logging.info('Telegram delivery: SUCCESS')
    else:
        logging.error(f'Telegram delivery: FAILED — {response.status_code} {response.text}')
        raise RuntimeError(f'Telegram send failed: {response.status_code}')


def main():
    logging.info('--- Vivian digest starting ---')
    stories = fetch_stories()

    if not stories:
        logging.error('No stories fetched — aborting send')
        return

    message = format_message(stories)
    send_telegram(message)
    logging.info('--- Vivian digest complete ---')


if __name__ == '__main__':
    main()
