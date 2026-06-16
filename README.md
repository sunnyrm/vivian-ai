# Vivian AI

A personal AI chief of staff that runs 24/7 and starts your day with what matters.

## Why I built this

Product guy tinkering with AI to make daily life easier, and learning in the process.

## What it does

Vivian sends a daily morning news digest to Telegram at 6am. It pulls the top 10 stories from Google News (India locale), ranked by editorial prominence — a mix of India and world news relevant to an Indian reader.

## Stack

- **Interface:** Telegram Bot
- **Hosting:** Hetzner VPS (Ubuntu 26.04)
- **News:** Google News RSS — editorially ranked, no AI for MVP
- **Language:** Python 3
- **Scheduler:** cron

## How to run

**Prerequisites:** Python 3, a Telegram bot token, a Hetzner (or any) VPS

```bash
git clone https://github.com/sunnyrm/vivian-ai.git
cd vivian-ai
pip3 install -r requirements.txt
cp .env.example .env  # fill in your credentials
python3 src/news_digest.py
```

For scheduled delivery, add to crontab:
```
0 4 * * * cd /path/to/vivian-ai && python3 src/news_digest.py >> logs/vivian.log 2>&1
```

## Roadmap

| Status | Use Case |
|---|---|
| ✅ | Daily news digest |
| ⏳ | Email scanning + reply drafting |
| ⏳ | Household coordination |
| ⏳ | Diet organiser |
| ⏳ | Financial organiser |
| ⏳ | Idea capture |
| ⏳ | Content generation |
| ⏳ | Calendar management |

## Cost

- Hetzner VPS: ~€7/month
- API costs: €0 (no AI used in MVP)

## License

MIT
