from fastapi import FastAPI, Depends, Body, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, create_engine, Session, select
from sqlalchemy import or_
from datetime import datetime
from typing import Optional, List
import httpx, json, os, re

app = FastAPI()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://quicknote:quicknote123@localhost:5432/quicknote_db")
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as s:
        yield s

class Note(SQLModel, table=True):
    __tablename__ = "notes"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default="")
    content: str = Field(max_length=5000)
    tags: str = Field(default="[]")
    insight: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)

@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)

ALL_TAGS = {
    "ru": ["учеба","планы","работа","идеи","личное","важно","лекция","семинар","лаба","экзамен","тест","домашка","встреча","дедлайн","проект","ментор","идея","креатив"],
    "en": ["study","plans","work","ideas","personal","important","lecture","seminar","lab","exam","test","homework","meeting","deadline","project","mentor","idea","creative"]
}

TRANSLATIONS = {
    "en": {"title":"✨ QuickNote AI","placeholder":"Enter your note...","save":"💾 Save","tags":"🏷️ Tags:","add":"Add:","insight":"💡 Insight:","confirm":"✅ Confirm","search_title":"🔍 Search","search_placeholder":"Search query or #tag...","search_btn":"🔎 Search","history":"📚 History","empty":"Empty","error":"Error","delete_confirm":"Delete this note?","no_tags":"No tags","saved":"Note saved","found":"Found","notes":"notes"},
    "ru": {"title":"✨ QuickNote AI","placeholder":"Введите заметку...","save":"💾 Сохранить","tags":"🏷️ Теги:","add":"Добавить:","insight":"💡 Инсайт:","confirm":"✅ Подтвердить","search_title":"🔍 Поиск","search_placeholder":"Поиск или #тег...","search_btn":"🔎 Найти","history":"📚 История","empty":"Пусто","error":"Ошибка","delete_confirm":"Удалить заметку?","no_tags":"Нет тегов","saved":"Заметка сохранена","found":"Найдено","notes":"записей"}
}

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/v1/chat/completions")

def detect_lang(text: str) -> str:
    return "ru" if re.search(r'[\u0400-\u04FF]', text) else "en"

async def llm_call(prompt: str, timeout: int = 5) -> str:
    try:
        async with httpx.AsyncClient(timeout=timeout) as c:
            r = await c.post(OLLAMA_URL, json={"model":"qwen2.5:1.5b","messages":[{"role":"user","content":prompt}],"max_tokens":80})
            return r.json()["choices"][0]["message"]["content"].strip()
    except:
        return ""

EN_MORPHOLOGY = {
    "meeting": ["meeting","meetings","meet","met","schedule","appointment","conference","call"],
    "meet": ["meet","meeting","meetings","met"],
    "database": ["database","databases","db","data","sql","postgres"],
    "note": ["note","notes","noted"],
    "task": ["task","tasks","todo","assignment"],
    "work": ["work","works","working","worked","job"],
    "project": ["project","projects","proj"],
    "deadline": ["deadline","deadlines","due"],
    "test": ["test","tests","testing","tested"],
    "lab": ["lab","labs","laboratory"],
    "exam": ["exam","exams","examination"],
    "lecture": ["lecture","lectures"],
    "study": ["study","studies","studying","studied"],
    "idea": ["idea","ideas"],
    "plan": ["plan","plans","planning","planned"],
    "time": ["time","times","timing"],
}

RU_MORPHOLOGY = {
    "встреч": ["встреча","встречи","встречу","встречей","встрече","встречам","встречами","встречах","собрани","совещани"],
    "баз": ["база","базы","базе","базу","базой","базам","базами","базах","баз","данных","данные"],
    "данн": ["данные","данных","данным","данными","данную","данной"],
    "лекц": ["лекция","лекции","лекцию","лекцией","лекциях"],
    "лаб": ["лаба","лабы","лабе","лабу","лабой","лабам","лабами","лабах","лаб","лабораторн"],
    "работ": ["работа","работы","работе","работу","работой","работам","работами","работах","работ"],
    "проект": ["проект","проекта","проекту","проектом","проекте","проекты","проектов","проектах"],
    "дедлайн": ["дедлайн","дедлайна","дедлайну","дедлайном","дедлайне","дедлайны","дедлайнов"],
    "экзамен": ["экзамен","экзамена","экзамену","экзаменом","экзамене","экзамены","экзаменов"],
    "семин": ["семинар","семинара","семинару","семинаром","семинаре","семинары","семинарах"],
    "домашк": ["домашка","домашки","домашке","домашку","домашкой"],
    "план": ["план","плана","плану","планом","плане","планы","планов","планах"],
    "времен": ["время","времени","временем","времена","времен"],
    "задач": ["задача","задачи","задаче","задачу","задачей","задачам","задачами","задачах"],
    "иде": ["идея","идеи","идее","идею","идеей","идей","идеях"],
}

def expand_word_morphology(word: str, lang: str) -> List[str]:
    word = word.lower()
    results = [word]
    morphology = EN_MORPHOLOGY if lang == "en" else RU_MORPHOLOGY
    for root, forms in morphology.items():
        if root in word or word in forms or any(word.startswith(r) for r in morphology.keys()):
            results.extend(forms)
            break
    if lang == "en" and len(word) > 3:
        if word.endswith('s'): results.append(word[:-1])
        if word.endswith('ing'): results.append(word[:-3]); results.append(word[:-3]+'s')
        if word.endswith('ed'): results.append(word[:-2])
    return list(set(results))

async def expand_query_with_llm(query: str, lang: str) -> List[str]:
    if lang == "ru":
        prompt = f"Search: '{query}'. Return Russian words ONLY, comma-separated: original words, synonyms, word forms. Example: 'встречам' → встреча,встречам,встречи,собрания. Just words:"
    else:
        prompt = f"Search: '{query}'. Return English words ONLY, comma-separated: original words, synonyms, word forms. Example: 'meetings' → meeting,meetings,meet,schedule. Just words:"
    result = await llm_call(prompt, timeout=5)
    if result:
        return [w.strip().lower() for w in result.split(',') if len(w.strip()) >= 2][:15]
    return []

def auto_tags(text: str, lang: str = "ru") -> List[str]:
    t = text.lower(); tags = []
    if lang == "ru":
        if any(w in t for w in ["лаба","тест","экзамен","лекция","семинар","домашка","sql","баз","данны","задач"]): tags.append("учеба")
        if any(w in t for w in ["встреч","дедлайн","срок","план","завтра","врем"]): tags.append("планы")
        if any(w in t for w in ["проект","ментор","работ"]): tags.append("работа")
        if any(w in t for w in ["иде","креатив"]): tags.append("идеи")
    else:
        if any(w in t for w in ["lab","test","exam","lecture","seminar","homework","sql","database"]): tags.append("study")
        if any(w in t for w in ["meeting","deadline","plan","tomorrow","time"]): tags.append("plans")
        if any(w in t for w in ["project","mentor","work"]): tags.append("work")
        if any(w in t for w in ["idea","creative"]): tags.append("ideas")
    if not tags: tags.append("personal" if lang == "en" else "личное")
    return tags[:3]

class NoteIn(BaseModel): content: str
class TagUpdate(BaseModel): note_id: int; tags: List[str]

@app.get("/api/tags")
def get_tags(lang: str = Query(default="ru")):
    return {"tags": ALL_TAGS.get(lang, ALL_TAGS["ru"])}

@app.post("/api/process")
async def process_note(data: NoteIn, lang: str = Query(default="ru"), session: Session = Depends(get_session)):
    detected_lang = detect_lang(data.content)
    title = " ".join(data.content.split()[:7])[:100] or ("Note" if detected_lang == "en" else "Заметка")
    tags = auto_tags(data.content, detected_lang)
    content_lower = data.content.lower()
    if detected_lang == "ru":
        if any(w in content_lower for w in ["лаба","экзамен","тест"]): insight = "💡 Подготовьте материалы заранее"
        elif any(w in content_lower for w in ["встреч","дедлайн"]): insight = "💡 Поставьте напоминание"
        elif any(w in content_lower for w in ["баз","sql","postgres"]): insight = "💡 Проверьте подключение к БД"
        else: insight = "💡 Заметка сохранена"
    else:
        if any(w in content_lower for w in ["lab","exam","test"]): insight = "💡 Prepare materials in advance"
        elif any(w in content_lower for w in ["meeting","deadline"]): insight = "💡 Set a reminder"
        elif any(w in content_lower for w in ["database","sql"]): insight = "💡 Check DB connection"
        else: insight = "💡 Note saved"
    note = Note(title=title, content=data.content, tags=json.dumps(tags), insight=insight)
    session.add(note); session.commit(); session.refresh(note)
    return {"success": True, "id": note.id, "title": title, "content": data.content, "tags": tags, "insight": insight}

@app.post("/api/update-tags")
def update_tags(data: TagUpdate, session: Session = Depends(get_session)):
    note = session.get(Note, data.note_id)
    if not note: raise HTTPException(404, "Not found")
    note.tags = json.dumps(data.tags[:5]); session.commit()
    return {"success": True}

@app.get("/api/notes/{nid}")
def get_note(nid: int, session: Session = Depends(get_session)):
    note = session.get(Note, nid)
    if not note: raise HTTPException(404, "Not found")
    return {"id": note.id, "title": note.title, "content": note.content, "tags": json.loads(note.tags), "insight": note.insight, "created_at": note.created_at.isoformat()}

@app.delete("/api/notes/{nid}")
def delete_note(nid: int, session: Session = Depends(get_session)):
    note = session.get(Note, nid)
    if not note: raise HTTPException(404, "Note not found")
    session.delete(note); session.commit()
    return {"success": True, "message": "Note deleted"}

@app.get("/api/notes")
def list_notes(limit: int = 50, session: Session = Depends(get_session)):
    notes = session.exec(select(Note).order_by(Note.created_at.desc()).limit(limit)).all()
    return [{"id": n.id, "title": n.title, "content": n.content, "tags": json.loads(n.tags), "insight": n.insight, "created_at": n.created_at.isoformat()} for n in notes]

@app.post("/api/search")
async def search_notes(query_data: dict = Body(), lang: str = Query(default="ru"), session: Session = Depends(get_session)):
    q = query_data.get("query", "").strip()
    if len(q) < 1:
        return {"success": False, "message": "Minimum 1 character" if lang == "en" else "Минимум 1 символ"}
    detected_lang = detect_lang(q)
    t = TRANSLATIONS.get(detected_lang, TRANSLATIONS["ru"])
    all_tags = ALL_TAGS.get(detected_lang, ALL_TAGS["ru"])
    tag_keywords, text_keywords = [], []
    words = [w.lower() for w in re.findall(r'\w+', q) if len(w) >= 1]
    for word in words:
        word_clean = word.lstrip('#')
        if word_clean in all_tags or word in all_tags: tag_keywords.append(word_clean)
        elif len(word) >= 2: text_keywords.append(word)
    keywords = text_keywords[:]
    for word in text_keywords:
        keywords.extend(expand_word_morphology(word, detected_lang))
    if len(' '.join(text_keywords)) > 5:
        keywords.extend(await expand_query_with_llm(' '.join(text_keywords), detected_lang))
    keywords = list(set(keywords))[:30]
    conds = []
    if keywords:
        for k in keywords:
            conds.append(Note.content.ilike(f"%{k}%")); conds.append(Note.title.ilike(f"%{k}%"))
    if tag_keywords:
        for tag in tag_keywords: conds.append(Note.tags.ilike(f'%"{tag}"%'))
    if not conds: return {"success": False, "message": "Nothing found" if lang == "en" else "Ничего не найдено"}
    notes = session.exec(select(Note).where(or_(*conds)).order_by(Note.created_at.desc()).limit(10)).all()
    if not notes: return {"success": False, "message": "Nothing found" if lang == "en" else "Ничего не найдено"}
    search_info = f" (tags: {', '.join(tag_keywords)})" if tag_keywords else ""
    answer = f"🔍 {t['found']} {len(notes)} {t['notes']}{search_info}"
    return {"success": True, "answer": answer, "notes": [{"id": n.id, "title": n.title, "content": n.content, "tags": json.loads(n.tags), "created_at": n.created_at.isoformat()} for n in notes]}

@app.get("/health")
def health(): return {"status": "ok", "db": "postgresql", "llm": "ollama"}

def get_html(lang: str = "ru") -> str:
    t = TRANSLATIONS.get(lang, TRANSLATIONS["ru"]); tags_list = ALL_TAGS.get(lang, ALL_TAGS["ru"])
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>QuickNote AI</title>
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui,sans-serif;max-width:800px;margin:0 auto;padding:20px;background:#f8f9fa;color:#1f2937}}.card{{background:#fff;padding:20px;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);margin-bottom:16px}}h1,h2{{margin-bottom:12px}}textarea,input{{width:100%;padding:12px;border:2px solid #e5e7eb;border-radius:8px;font-size:16px;margin-bottom:8px}}textarea{{min-height:100px;resize:vertical}}button{{background:#4f46e5;color:#fff;border:none;padding:12px 20px;border-radius:8px;font-size:16px;cursor:pointer}}button:hover{{background:#4338ca}}button:disabled{{background:#9ca3af;cursor:not-allowed}}.result{{margin-top:12px;padding:16px;background:#f0f9ff;border-radius:8px;display:none}}.result.show{{display:block}}.tag{{display:inline-block;background:#e0e7ff;color:#3730a3;padding:4px 12px;border-radius:20px;font-size:14px;margin:4px 4px 4px 0;cursor:pointer}}.tag.rem:hover{{background:#fecaca}}.note{{position:relative;padding:12px;border:1px solid #e5e7eb;border-radius:8px;margin-bottom:8px;cursor:pointer}}.note:hover{{background:#f9fafb}}.note.exp{{background:#f9fafb}}.note-title{{font-weight:600;margin-bottom:4px}}.note-date{{color:#6b7280;font-size:12px}}.note-preview{{color:#4b5563;font-size:14px}}.note-full{{background:#fff;padding:12px;border-radius:6px;margin-top:8px;border-left:3px solid #4f46e5}}.tag-cloud{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}}.tag-opt{{padding:6px 12px;border:2px solid #e5e7eb;border-radius:20px;cursor:pointer;font-size:13px}}.tag-opt:hover{{border-color:#4f46e5}}.tag-opt.active{{background:#4f46e5;color:#fff;border-color:#4f46e5}}.error{{color:#dc2626;margin-top:8px}}.success{{color:#059669;margin-top:8px}}.delete-btn{{position:absolute;right:10px;top:10px;background:#fee2e2;border:none;border-radius:4px;padding:4px 8px;cursor:pointer;font-size:14px}}.delete-btn:hover{{background:#fecaca}}.lang-switch{{position:fixed;top:20px;right:20px;background:#fff;padding:8px 16px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1);cursor:pointer;border:2px solid #e5e7eb}}.lang-switch:hover{{border-color:#4f46e5}}.tag-search-hint{{color:#6b7280;font-size:12px;margin-top:4px}}</style></head><body>
<button class="lang-switch" onclick="toggleLang()">🌍 {'English' if lang == 'ru' else 'Русский'}</button>
<div class="card"><h1>{t['title']}</h1><textarea id="content" placeholder="{t['placeholder']}"></textarea><button id="saveBtn" onclick="saveNote()">{t['save']}</button><div id="saveErr" class="error"></div><div class="result" id="saveRes"><div style="background:#fff;padding:12px;border-radius:6px;margin-bottom:12px;border-left:3px solid #4f46e5"><strong id="savedTitle"></strong><br><span id="savedContent" style="color:#4b5563"></span></div><div><strong>{t['tags']}</strong><div id="tagList"></div></div><div style="margin-top:8px"><strong>{t['add']}</strong><div class="tag-cloud" id="tagCloud"></div></div><div style="margin-top:12px"><strong>{t['insight']}</strong><p id="savedInsight"></p></div><button onclick="confirmTags()" style="margin-top:12px;width:100%">{t['confirm']}</button></div></div>
<div class="card"><h2>{t['search_title']}</h2><input type="text" id="searchQ" placeholder="{t['search_placeholder']}"><button onclick="doSearch()">{t['search_btn']}</button><div class="tag-search-hint">💡 Try: #study or meeting or "team schedule"</div><div id="searchErr" class="error"></div><div class="result" id="searchRes"></div><div id="searchList"></div></div>
<div class="card"><h2>{t['history']}</h2><div id="history"></div></div>
<script>
let curId=null,curTags=[],allTags={json.dumps(tags_list)},currentLang='{lang}';
async function saveNote(){{const c=document.getElementById("content").value.trim();const btn=document.getElementById("saveBtn");const err=document.getElementById("saveErr");if(!c){{err.textContent="{t['error']}";return}}err.textContent="";btn.disabled=true;btn.textContent="⏳";try{{const r=await fetch("/api/process?lang="+currentLang,{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{content:c}})}});const d=await r.json();if(!d.success){{err.textContent=d.detail||"{t['error']}";return}}curId=d.id;curTags=d.tags||[];document.getElementById("savedTitle").textContent=d.title;document.getElementById("savedContent").textContent=d.content.length>150?d.content.substring(0,150)+"...":d.content;document.getElementById("savedInsight").textContent=d.insight;renderTags();renderCloud();document.getElementById("saveRes").classList.add("show");document.getElementById("content").value="";loadHist();}}catch(e){{err.textContent="{t['error']}: "+e.message}}finally{{btn.disabled=false;btn.textContent="{t['save']}"}}}}
function renderTags(){{const div=document.getElementById("tagList");div.innerHTML="";if(!curTags.length){{div.innerHTML="<span style='color:#6b7280'>{t['no_tags']}</span>";return}}curTags.forEach(t=>{{const s=document.createElement("span");s.className="tag rem";s.textContent="#"+t+" ×";s.onclick=()=>{{curTags=curTags.filter(x=>x!==t);renderTags();renderCloud()}};div.appendChild(s);}});}}
function renderCloud(){{const div=document.getElementById("tagCloud");div.innerHTML="";allTags.forEach(t=>{{const b=document.createElement("span");b.className="tag-opt"+(curTags.includes(t)?" active":"");b.textContent=t;b.onclick=()=>{{if(curTags.includes(t)){{curTags=curTags.filter(x=>x!==t)}}else if(curTags.length<5){{curTags.push(t)}};renderTags();renderCloud()}};div.appendChild(b);}});}}
async function confirmTags(){{if(!curId)return;try{{const r=await fetch("/api/update-tags",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{note_id:curId,tags:curTags}})}});const d=await r.json();if(d.success){{document.getElementById("saveErr").className="success";document.getElementById("saveErr").textContent="✅ {t['saved']}";setTimeout(()=>{{document.getElementById("saveRes").classList.remove("show");document.getElementById("saveErr").className="error";document.getElementById("saveErr").textContent=""}},2000);loadHist()}}}}catch(e){{alert("{t['error']}: "+e.message)}}}}
async function doSearch(){{const q=document.getElementById("searchQ").value.trim();const btn=document.querySelector("#searchQ+button");const err=document.getElementById("searchErr");const resDiv=document.getElementById("searchRes");const listDiv=document.getElementById("searchList");if(!q){{err.textContent="{t['error']}";return}}err.textContent="";resDiv.textContent="";resDiv.classList.remove("show");listDiv.innerHTML="";btn.disabled=true;btn.textContent="⏳";try{{const r=await fetch("/api/search?lang="+currentLang,{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{query:q}})}});const d=await r.json();if(!d.success){{resDiv.textContent="🔍 "+d.message;resDiv.classList.add("show");return}}resDiv.textContent=d.answer;resDiv.classList.add("show");let h="";(d.notes||[]).forEach(n=>{{h+="<div class='note' onclick='toggleNote("+n.id+")'><button class='delete-btn' onclick='deleteNote("+n.id+",event)'>🗑️</button><div class='note-title'>"+(n.title||"")+"</div><div class='note-date'>"+(n.created_at||"").substring(0,10)+"</div><div class='note-preview'>"+(n.content||"").substring(0,120)+"...</div></div>"}});listDiv.innerHTML=h;}}catch(e){{err.textContent="{t['error']}: "+e.message}}finally{{btn.disabled=false;btn.textContent="{t['search_btn']}"}}}}
async function toggleNote(id){{const el=event.currentTarget;if(el.classList.contains("expanded")){{el.classList.remove("expanded");el.innerHTML=el.dataset.collapsed;return}}try{{const r=await fetch("/api/notes/"+id);const n=await r.json();el.dataset.collapsed=el.innerHTML;el.classList.add("expanded");el.innerHTML="<button class='delete-btn' onclick='deleteNote("+n.id+",event)'>🗑️</button><div class='note-title'>"+(n.title||"")+"</div><div class='note-date'>"+(n.created_at||"").substring(0,10)+"</div><div class='note-full'>"+n.content+"</div><div style='margin-top:8px'><span style='color:#6b7280;font-size:12px'>🏷️ "+((n.tags||[]).join(", ")||"{t['no_tags']}")+"</span></div>"+(n.insight?"<div style='margin-top:8px;color:#059669;font-size:13px'>"+n.insight+"</div>":"");}}catch(e){{alert("{t['error']}")}}}}
async function deleteNote(id,event){{event.stopPropagation();if(!confirm("{t['delete_confirm']}"))return;try{{const r=await fetch("/api/notes/"+id,{{method:"DELETE"}});const d=await r.json();if(d.success){{loadHist();doSearch();}}}}catch(e){{alert("{t['error']}: "+e.message)}}}}
async function loadHist(){{const div=document.getElementById("history");try{{const r=await fetch("/api/notes");const d=await r.json();if(!d||!d.length){{div.innerHTML="<span style='color:#6b7280'>{t['empty']}</span>";return}}let h="";d.forEach(n=>{{h+="<div class='note' onclick='toggleNote("+n.id+")'><button class='delete-btn' onclick='deleteNote("+n.id+",event)'>🗑️</button><div class='note-title'>"+(n.title||"")+"</div><div class='note-date'>"+(n.created_at||"").substring(0,10)+"</div><div class='note-preview'>"+(n.content||"").substring(0,120)+"...</div></div>"}});div.innerHTML=h;}}catch(e){{div.innerHTML="<span style='color:#6b7280'>{t['error']}</span>"}}}}
function toggleLang(){{currentLang=currentLang==='ru'?'en':'ru';window.location.href='/?lang='+currentLang;}}
loadHist();
</script></body></html>"""

@app.get("/", response_class=HTMLResponse)
def home(lang: str = Query(default="ru")): return get_html(lang)
