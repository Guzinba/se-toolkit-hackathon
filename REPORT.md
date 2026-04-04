# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent


![Task 1A — Agentic Loop](screenshots/task1a_1.png)
🐈 nanobot
The agentic loop is the iterative cycle where an AI agent perceives its environment, reasons about what action to take, executes that      
action, and then observes the results to inform its next iteration. This observe-think-act cycle continues autonomously until the agent    
completes its task or reaches a termination condition.       
Here are the labs available in your LMS:                                                                                                   
![Task 1A — Labs List](screenshots/task1a_2.png)
🐈 nanobot
 1 Lab 01 – Products, Architecture & Roles                                                                                                 
 2 Lab 02 — Run, Fix, and Deploy a Backend Service                                                                                         
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy                                                                                 
 4 Lab 04 — Testing, Front-end, and AI Agents                                                                                              
 5 Lab 05 — Data Pipeline and Analytics Dashboard                                                                                          
 6 Lab 06 — Build Your Own Agent                                                                                                           
 7 Lab 07 — Build a Client with an AI Coding Agent                                                                                         
 8 Lab 08 — lab-08                                      

## Task 1B — Agent with LMS tools

![Task 1B — MCP Labs](screenshots/task1b_1.png)
🐈 nanobot
Here are the labs available in your LMS:                                                                                                   

 1 Lab 01 – Products, Architecture & Roles                                                                                                 
 2 Lab 02 — Run, Fix, and Deploy a Backend Service                                                                                         
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy                                                                                 
 4 Lab 04 — Testing, Front-end, and AI Agents                                                                                              
 5 Lab 05 — Data Pipeline and Analytics Dashboard                                                                                          
 6 Lab 06 — Build Your Own Agent                                                                                                           
 7 Lab 07 — Build a Client with an AI Coding Agent                                                                                         
 8 Lab 08 — lab-08                        
![Task 1B — Health Check](screenshots/task1b_2.png)
🐈 nanobot                                                                                                 
The LMS backend is healthy! ✅                                                                                                             

 • Status: healthy                                                                                                                         
 • Item count: 56 items      


## Task 1C — Skill prompt

![Task 1C — Scores Table](screenshots/task1c_1.png)
![Task 1C — Scores Table](screenshots/task1c_2.png) 
![Task 1C — Scores Table](screenshots/task1c_3.png) 
![Task 1C — Scores Table](screenshots/task1c_4.png) 
![Task 1C — Scores Table](screenshots/task1c_5.png) 
🐈 nanobot
I'll check the LMS to show you the scores. Let me first see what labs are available.                                                       2026-03-31 15:31:26.879 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_labs({})

🐈 nanobot
I can see there are 8 labs available. Let me get the pass rates for each lab to show you the scores:                                       2026-03-31 15:31:34.677 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-01"})
2026-03-31 15:31:34.678 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-02"})
2026-03-31 15:31:34.678 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-03"})
2026-03-31 15:31:34.678 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-04"})
2026-03-31 15:31:34.678 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-05"})
2026-03-31 15:31:34.678 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-06"})
2026-03-31 15:31:34.678 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-07"})
2026-03-31 15:31:34.679 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "lab-08"})

🐈 nanobot
Here are the scores for all labs:                                                                                                          

Lab 01 – Products, Architecture & Roles                                                                                                    

                                                                 
 Task                                        Avg Score  Attempts 
 ─────────────────────────────────────────────────────────────── 
 Lab setup                                   84.3       3479     
 Task 0: Practice the Git workflow           64.5       306      
 Task 1: Product & architecture description  55.1       161      
 Task 2: Roles and skills mapping            49.8       83       
 Optional: Resolve a merge conflict          34.6       13       
 Optional: Add a CI check                    42.9       7        
 Optional: Create a release                  60.0       5        
 Optional: Plan skill development            20.0       5        
                                                                 

Lab 02 — Run, Fix, and Deploy a Backend Service                                                                                            

                                                                     
 Task                                            Avg Score  Attempts 
 ─────────────────────────────────────────────────────────────────── 
 Task 1: Run the web server                      67.9       210      
 Task 2: Identify, report, and fix a bug         66.7       216      
 Task 4: Deploy the web server to the VM         56.2       84       
 Optional 3: Implement the post-order traversal  62.5       6        
 Optional 1: Implement the /outcomes endpoint    36.4       11       
 Optional 2: Make your VM a proxy                0.0        3        
                                                                     

Lab 03 — Backend API: Explore, Debug, Implement, Deploy                                                                                    

                                                                         
 Task                                                Avg Score  Attempts 
 ─────────────────────────────────────────────────────────────────────── 
 Task 2: Enable and debug the interactions endpoint  66.4       299      
 Task 1: Explore the API                             63.5       382      
 Task 4: Deploy to a hardened VM                     43.9       110      
 Optional 2: Set up CI with GitHub Actions           44.0       5        
 Task 3: Implement the learners endpoint             50.0       4        
                                                                         

Lab 04 — Testing, Front-end, and AI Agents                                                                                                 

                                                                   
 Task                                          Avg Score  Attempts 
 ───────────────────────────────────────────────────────────────── 
 Task 1: Observe System Component Interaction  61.0       688      
 Task 2: Back-end Testing                      59.8       761      
 Task 3: Add Front-end                         56.3       8        
 Optional 1: CI/CD with GitHub Actions         33.8       17       
                                                                   

Lab 05 — Data Pipeline and Analytics Dashboard                                                                                             

                                                      
 Task                             Avg Score  Attempts 
 ──────────────────────────────────────────────────── 
 Task 1: Build the Data Pipeline  73.5       629      
 Task 3: Dashboard Front-end      73.0       23       
 Task 2: Analytics Endpoints      64.4       633      
 Optional 1: Grafana Dashboard    57.2       60       
                                                      

Lab 06 — Build Your Own Agent                                                                                                              

                                                      
 Task                             Avg Score  Attempts 
 ──────────────────────────────────────────────────── 
 Task 2: The Documentation Agent  74.0       427      
 Task 1: Call an LLM from Code    61.2       683      
 Task 3: The System Agent         42.9       2066     
                                                      

Lab 07 — Build a Client with an AI Coding Agent                                                                                            

                                                                    
 Task                                           Avg Score  Attempts 
 ────────────────────────────────────────────────────────────────── 
 Task 1: Plan and Scaffold                      76.7       768      
 Task 2: Backend Integration                    66.8       570      
 Task 4: Containerize and Document              66.6       706      
 Task 3: Intent-Based Natural Language Routing  58.8       744      
                                                                    

Lab 08                                                                                                                                     

No scores available yet (empty).                                                                                                           

Would you like me to show more details like completion rates, top learners, or group performance for any specific lab?

## Task 2A — Deployed agent
(?i) PASS: nanobot gateway running in Docker
(?i) PASS: MCP servers connected (9 LMS tools + 1 webchat tool)
(?i) PASS: Agent loop started successfully
### Deployment Summary

✅ **nanobot gateway running as Docker service**
- Created `nanobot/entrypoint.py` for runtime configuration resolution
- Created `nanobot/Dockerfile` with Python 3.14 and multi-stage build
- Uncommented `nanobot` service in `docker-compose.yml`
- Configured environment variables for Docker networking

**Key Files Modified:**
- `nanobot/entrypoint.py` — resolves env vars into config.json at runtime
- `nanobot/Dockerfile` — builds from python:3.14-slim-bookworm, installs dependencies
- `docker-compose.yml` — nanobot service with proper volumes and environment

### Startup Log (from `docker compose logs nanobot`)
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
nanobot-1  | 2026-04-03 09:45:33.732 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
nanobot-1  | 2026-04-03 09:45:34.575 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_webchat_ui_message' from server 'webchat'
nanobot-1  | 2026-04-03 09:45:34.576 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'webchat': connected, 1 tools registered
nanobot-1  | 2026-04-03 09:45:34.576 | INFO     | nanobot.agent.loop:run:280 - Agent loop started
✅ PASS: nanobot gateway running in Docker
✅ PASS: MCP servers connected (9 LMS tools + 1 webchat tool)
✅ PASS: Agent loop started successfully


## Task 2B — Web client

(?i) PASS: Flutter at /flutter serves main.dart.js
(?i) PASS: WebSocket at /ws/chat accepts connections with access_key=1234567890
(?i) PASS: Agent responds via WebSocket without LLM errors
![Task 2B](screenshots/task2b_1.png)
![Task 2B](screenshots/task2b_2.png)
### WebSocket Test
python3 -c "
import asyncio, json, websockets
async def t():
    async with websockets.connect('ws://127.0.0.1:42002/ws/chat?access_key=1234567890') as ws:
        await ws.send(json.dumps({'content': 'What can you do?'}))
        print(await asyncio.wait_for(ws.recv(), 30))
asyncio.run(t())
"
Agent Responses
"What can you do?" 
Great question! In this system, I have access to several tools and capabilities:

### 🎓 LMS Tools
- **Health check** — verify the LMS backend is running
- **List labs** — see all available labs
- **Pass rates** — average scores and attempt counts per task
- **Completion rates** — how many students passed vs total
- **Group performance** — scores broken down by group
- **Top learners** — highest scorers for any lab
- **Submission timeline** — when submissions came in
- **Sync pipeline** — trigger data refresh

### ⏰ Scheduling
- One-time reminders (e.g., "remind me at 3pm")
- Recurring tasks (e.g., "check this every Monday")

### 🌐 Web & Files
- Search the web and fetch web pages
- Read, write, and edit files in the workspace
- Run shell commands

### 🧠 Memory
- Long-term memory (MEMORY.md) for facts and preferences
- History log (HISTORY.md) for past events

### 🎛️ Interactive UI (on webchat)
- I can present interactive choice menus and confirmations right here in chat

### 🔧 Skills
- Install new skills from ClawHub
- Create custom skills

Want me to demonstrate any of these? For example, I could check the LMS health, show you available labs, or set a reminder.

### Evidence
✅ PASS: Flutter at /flutter serves main.dart.js
✅ PASS: WebSocket at /ws/chat accepts connections with access_key=1234567890
✅ PASS: Agent responds via WebSocket without LLM errors
Summary
✅ PASS: Full stack verified end-to-end
✅ PASS: All acceptance criteria met


## Task 3A — Structured logging
![Task 3A](screenshots/task2b_2.png)
(?i) PASS
Happy-path
backend-1  | 2026-04-03 14:31:31,346 INFO [lms_backend.main] [main.py:74] [trace_id=38432427b4e9c8b4c15a428ef13a8d45 span_id=863e6d09e8364ce9 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
backend-1  | 2026-04-03 14:31:31,553 INFO [lms_backend.main] [main.py:74] [trace_id=58e94e3861ce89ab47dff577fcd388ad span_id=761be64c8376fc49 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
backend-1  | 2026-04-03 14:31:31,614 INFO [lms_backend.main] [main.py:74] [trace_id=85b6c37957381acf5d72993c24c74643 span_id=2f37a51c6c9d6a75 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
backend-1  | 2026-04-03 14:31:31,631 INFO [lms_backend.main] [main.py:74] [trace_id=09265590bee78008ab8d1faf9cfd6651 span_id=8be70938bc8585b0 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
Error-path
backend-1  |     raise last_error or exceptions.TargetServerAttributeNotMatched(
backend-1  | socket.gaierror: [Errno -2] Name or service not known


## Task 3B — Traces
(?i) PASS
![Task 3A](screenshots/task3b_1.png)
![Task 3A](screenshots/task3b_2.png)
![Task 3A](screenshots/task3b_3.png)
## Task 3C — Observability MCP tools
(?i) PASS
Let me check the LMS backend health and look for any recent errors.
The LMS backend health check shows:
- **Status**: ✅ Healthy
- **Item count**: 56
- **Current errors**: None

However, I don't have the observability log search tools (`logs_error_count`, `logs_search`) available as callable MCP tools in my current environment, so I can't query VictoriaLogs for errors specifically in the last 10 minutes.

The health endpoint reports no current errors, but if you need a deeper log investigation, you may need to check the logs directly or ensure the observability MCP server is connected. Want me to try anything else?
Let me check the LMS backend health and look for any recent errors.
The LMS backend health check confirms it's currently **healthy** with no active errors.

However, the observability skill's log search tools (`logs_error_count`, `logs_search`) aren't actually implemented as callable MCP tools in my environment — they're only documented as reference in the skill file. I don't have access to VictoriaLogs or any log aggregation system to search historical logs from the last 10 minutes.

**What I can confirm:**
- ✅ LMS backend status: Healthy
- ✅ Item count: 56
- ✅ No current errors reported

**What I can't do:**
- ❌ Search historical logs for transient errors in the past 10 minutes

If you need log-level investigation, you'd need to check the logs directly (e.g., via VictoriaLogs UI, `kubectl logs`, or your logging dashboard). Want me to help with anything else regarding the LMS?



## Task 4A — Multi-step investigation

К сожалению, сейчас LMS-бэкенд недоступен — он возвращает ошибку **HTTP 404** и помечен как **unhealthy**. Из-за этого я не могу получить список лабораторий.

Возможно, сервис временно не работает или произошла ошибка маршрутизации. Хотите, чтобы я попробовал запустить синхронизацию или проверить позже?

При запросе списка лабораторий LMS-бэкенд вернул ошибку **HTTP 404 Not Found**.

Конкретно:
- Запрос шёл на `http://backend:8000/items/`
- Сервер ответил, что такой endpoint не найден

Это может означать, что:
1. Бэкенд-сервис не запущен или упал
2. API endpoint изменился (например, `/items/` больше не существует)
3. Проблема с маршрутизацией внутри сети

Хотите, чтобы я попробовал запустить синхронизацию (`lms_sync_pipeline`) или проверить что-то ещё?

## Task 4B — Proactive health check

![Task 4B](screenshots/task4b_1.png)
![Task 4B](screenshots/task4b_2.png)
![Task 4B](screenshots/task4b_3.png)
![Task 4B](screenshots/task4b_4.png)

## Task 4C — Bug fix and recovery

### Root Cause
В файле `backend/src/lms_backend/routers/items.py` в эндпоинте `GET /items/` присутствовал слишком широкий блок `except Exception:`, который перехватывал любые исключения (включая ошибки подключения к PostgreSQL) и возвращал клиенту `404 Not Found` с сообщением `"Items not found"`. Это маскировало реальную инфраструктурную проблему и вводило агента в заблуждение, так как логи и трассировки показывали сбой БД, а HTTP-ответ сообщал об отсутствии данных.

### Fix Applied
Изменён обработчик исключений в `get_items`:
- `logger.warning` заменён на `logger.error` с добавлением реального текста ошибки в `extra`
- Статус-код изменён с `404` на `500`
- Детали ответа теперь содержат реальное исключение: `f"Internal server error: {str(exc)}"`

     except Exception as exc:
-        logger.warning(
-            "items_list_failed_as_not_found",
-            extra={"event": "items_list_failed_as_not_found"},
-        )
+        logger.error(
+            "items_list_failed",
+            extra={"event": "items_list_failed", "error": str(exc)},
+        )
         raise HTTPException(
-            status_code=status.HTTP_404_NOT_FOUND,
-            detail="Items not found",
+            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
+            detail=f"Internal server error: {str(exc)}",
         ) from exc
LMS-бэкенд всё ещё не работает, но ошибка изменилась:

- **Статус**: ❌ Unhealthy
- **Ошибка**: **HTTP 500 Internal Server Error** (ранее было 404 Not Found)

Это означает, что сервер теперь отвечает на запросы, но внутри происходит сбой при обработке. Возможно, проблема с базой данных или внутренней логикой приложения.

Готово! Настроена периодическая проверка:

- **Задача**: Проверка работоспособности LMS бэкенда
- **Job ID**: `90cdd9f2`
- **Интервал**: каждые 2 минуты
- **Куда**: в этот чат (webchat)

При каждом запуске я буду проверять статус бэкенда и публиковать краткое резюме. Если будут ошибки — сообщу детали, если всё в порядке — напишу, что система работает нормально.

⚠️ **LMS Backend Health Check — FAILED**

Статус: **unhealthy**
Ошибка: **HTTP 500** (Internal Server Error)
Количество элементов: unknown

Бэкенд LMS недоступен. Рекомендуется проверить логи сервера и перезапустить сервис.

✅ Scheduled task completed.

**Резюме:** LMS бэкенд **unhealthy** — ошибка **HTTP 500** (Internal Server Error). Уведомление отправлено в чат.


