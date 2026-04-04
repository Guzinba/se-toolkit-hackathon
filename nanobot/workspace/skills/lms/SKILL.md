---
name: lms
description: Use LMS MCP tools to work with real-time course data
always: true
---

## Available Tools
- `lms_health` — check if LMS backend is healthy
- `lms_labs` — list available labs
- `lms_pass_rates` — get pass rates for a lab
- `lms_learners` — get learner information
- `lms_timeline` — get submission timeline
- `lms_top_learners` — get top performers
- `lms_completion_rate` — get completion statistics
- `lms_groups` — get group performance
- `lms_sync_pipeline` — trigger data sync

## Strategy Rules
1. If user asks for scores/pass rates/completion without naming a lab:
   - First call `lms_labs` to get available labs
   - Ask user to choose one if multiple exist
2. Format numeric results nicely (percentages, counts)
3. Keep responses concise
4. If user asks "What can you do?", list available LMS tools

## Response Format
- Start with a one-sentence summary
- Use bullet points for lists
- End with a suggested next step if applicable
