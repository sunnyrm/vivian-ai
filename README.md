# Vivian AI

A personal AI chief of staff. Lives in Telegram.
Runs 24/7 on Hetzner. Built incrementally.

## What Vivian does (MVP)
- Sends a daily news digest at 6am CEST via Telegram
- Source: Google News (India locale) — top stories ranked by prominence
- Top 10 stories with headlines and links

## Stack
- Interface: Telegram Bot
- Hosting: Hetzner VPS (Ubuntu 26.04)
- News: Google News RSS (no AI for MVP)
- Language: Python 3

## Cost
- Hetzner VPS: ~€7/month
- API costs: €0 (MVP uses no AI)

## Setup
See DECISIONS.md for all architecture decisions.
Add your secrets to .env (never commit this file).

## How We Work
- Strategy & decisions: Claude.ai project chat
- Building & shipping: Claude Code
- Context files: CLAUDE.md, SOUL.md, DECISIONS.md
- CLAUDE.md is auto-read by Claude Code every session

## Roadmap
See DECISIONS.md for full use case roadmap.
