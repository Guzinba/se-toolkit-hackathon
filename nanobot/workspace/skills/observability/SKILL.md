# Observability Skill

## Purpose
Help users investigate errors using logs and traces.

## Tools
- `logs_search(query, limit)` — search VictoriaLogs by LogsQL
- `logs_error_count(service, minutes)` — count errors for a service
- `traces_list(service, limit)` — list recent traces
- `traces_get(trace_id)` — fetch full trace by ID

## Investigation Flow (when user asks "What went wrong?" or "Check system health")
1. Call `logs_error_count(service="Learning Management Service", minutes=10)`
2. If errors > 0:
   a. Call `logs_search(query='_time:10m service.name:"Learning Management Service" severity:ERROR', limit=5)`
   b. Extract `trace_id` from the most recent error log
   c. Call `traces_get(trace_id="<extracted_id>")`
3. Summarize findings in 2-3 sentences:
   - Which service failed
   - What operation caused it
   - Reference both log entry and trace

## Response Rules
- Never dump raw JSON — always summarize
- If no recent errors: "System healthy, no errors in last 10 minutes"
- If user asks "What can you do?", list observability tools briefly
