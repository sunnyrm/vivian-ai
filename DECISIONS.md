# Vivian — Architecture Decisions Log

## Project Overview
Personal AI chief of staff. Built incrementally.
Uses Lyra AI as reference
architecture but makes independent decisions.

## Decision Log

### Interface: Telegram
- Chosen because: already used daily
- Rejected: WhatsApp (cost, complexity),
  custom app (overkill)
- Revisit: when onboarding wife as second user

### Hosting: Hetzner VPS
- Chosen because: always-on, cheap (€4-6/mo),
  full control, same as Lyra
- Rejected: Mac local (not always on),
  GitHub Actions (deferred for later),
  Railway/Render (less control)
- Revisit: never — right call for production

### Database: Deferred
- Not needed for MVP (news feed only)
- Revisit: before building use case 2 (email)
- Leading candidate: Notion

### Model Routing: Deferred
- Not needed for MVP (no AI used)
- Revisit: when summarisation is added post-MVP

### News Source: Google News RSS (India locale)
- Feed: https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en
- Chosen because: editorially ranked by Google (prominence + recency),
  covers India + world mix in one feed, closer to homepage curation
- Rejected: HT RSS feeds — chronological only, no editorial ranking;
  HT has no homepage-curation RSS feed
- Stories: top 10 by Google's ranking (not chronological)
- Sources: multi-source (Hindu, TOI, NDTV, HT, Al Jazeera etc.)
- URLs: shortened via TinyURL (Google News URLs are ~300 chars,
  exceed Telegram's 4096 char limit at 10 stories)
- Revisit: post-MVP — add AI filtering to remove noise if needed

### No AI for MVP
- RSS fetch + Telegram delivery needs no AI
- Cost: €0 API spend for MVP
- Revisit: post-MVP for summarisation (likely Haiku)

### Delivery Schedule
- Cron: 0 4 * * * (4am UTC = 6am CEST)
- Revisit: October when clocks change (CET = UTC+1, adjust to 0 5 * * *)

### Chunked Build Approach
- Build and verify one chunk at a time
- Never proceed to next chunk without confirmation
- Each chunk has a clear done check

### Context Preservation
- CLAUDE.md auto-read by Claude Code every session
- SOUL.md, DECISIONS.md, README.md are the
  source of truth across all sessions
- This chat (Claude.ai project) holds the
  strategic discussion history

## Post-MVP Backlog
1. AI summarisation (1-2 lines per story)
2. Additional news sources
3. Story ranking by relevance
4. Digest logging to Notion
5. WhatsApp migration option
6. Filtering layer if feeds have noise
7. Email scanning (use case 2)
8. Wife coordination (use case 3)

## Use Cases Roadmap
1. ✅ News digest (MVP — complete)
2. ⏳ Email scanning + reply drafting
3. ⏳ Household coordination with wife
4. ⏳ Diet organiser
5. ⏳ Financial organiser
6. ⏳ Idea capture
7. ⏳ Content generation
8. ⏳ Reservations
9. ⏳ Trip planning
10. ⏳ Calendar management
