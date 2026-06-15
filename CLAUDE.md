# Vivian AI — Claude Code Context

## Read First
Before doing anything in this project, read:
- SOUL.md — Vivian's identity, personality, hard rules
- DECISIONS.md — every architecture decision and why
- README.md — project overview and stack

## What We're Building
Vivian is a personal AI chief of staff.
Interface: Telegram. Hosting: Hetzner VPS.
Language: Python. Database: deferred.

## Current Focus
MVP: daily news digest from Google News (India locale)
delivered to Telegram at 6am CEST. No AI used.

## Working Style
- One chunk at a time
- Wait for explicit approval before next chunk
- Never hardcode credentials
- Ask before spending money
- Stop and ask if anything is unclear

## Context Across Sessions
This file is auto-read by Claude Code every session.
DECISIONS.md is the source of truth for all choices.
