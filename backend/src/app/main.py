from fastapi import FastAPI, Depends, Query
from sqlmodel import Session, select, or_
from .models import Note
from .llm import generate_tags, answer_from_notes
from .database import get_session, create_db_and_tables

app = FastAPI(title="QuickNote AI")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/notes")
async def save_note(content: str, session: Session = Depends(get_session)):
    tags = await generate_tags(content)  # работает с заглушкой или LLM
    note = Note(content=content, tags=tags)
    session.add(note)
    session.commit()
    session.refresh(note)
    return {
        "id": note.id, 
        "tags": tags, 
        "message": f"✅ Сохранено! Теги: #{' #'.join(tags)}"
    }

@app.post("/notes/ask")
async def ask_notes(question: str, session: Session = Depends(get_session)):
    # Простой поиск по ключевым словам (V1)
    words = [w for w in question.lower().split() if len(w) > 3][:3]
    stmt = select(Note).where(or_(*[Note.content.ilike(f"%{w}%") for w in words])).limit(4)
    notes = session.exec(stmt).all()
    
    if not notes:
        return {"answer": "📝 Пока нет записей по этой теме. Сохрани что-нибудь!"}
    
    # Формируем контекст для "инсайта"
    context = "\n".join([
        f"[{n.created_at.strftime('%d.%m')}] ({', '.join(n.tags)}) {n.content}" 
        for n in notes
    ])
    
    answer = await answer_from_notes(question, context)  # заглушка или LLM
    return {"answer": answer, "notes_used": len(notes)}

@app.get("/health")
def health():
    return {"status": "ok", "service": "quicknote-backend"}
