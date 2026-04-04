import os, re, random
from typing import List

# 🔧 Переключатель: поставь True, когда Qwen починится
USE_REAL_LLM = os.getenv("USE_REAL_LLM", "false").lower() == "true"

# === ЗАГЛУШКИ ДЛЯ V1 (работают сразу) ===

def _mock_generate_tags(text: str) -> List[str]:
    """Rule-based tag generator — 80% точности для демо"""
    text_lower = text.lower()
    tags = []
    
    # Категории по ключевым словам
    if any(w in text_lower for w in ["встреча", "созвон", "зум", "ментор", "команда"]):
        tags.extend(["встреча", "работа", "коммуникация"])
    if any(w in text_lower for w in ["дедлайн", "сдать", "лаба", "тест", "отчёт"]):
        tags.extend(["учеба", "дедлайн", "срочно"])
    if any(w in text_lower for w in ["идея", "придумал", "хочу", "план"]):
        tags.extend(["идея", "планирование", "креатив"])
    if any(w in text_lower for w in ["купить", "магазин", "деньги", "цена"]):
        tags.extend(["покупки", "финансы", "список"])
    if any(w in text_lower for w in ["здоровье", "спорт", "сон", "еда"]):
        tags.extend(["здоровье", "лайфстайл", "забота"])
    
    # Добавляем временные теги
    if "завтра" in text_lower or "сегодня" in text_lower:
        tags.append("время")
    if "важно" in text_lower or "срочно" in text_lower:
        tags.append("приоритет")
    
    # Возвращаем уникальные, максимум 3
    return list(dict.fromkeys(tags))[:3] or ["заметка", "общее", "идея"]

def _mock_answer_from_notes(question: str, notes_context: str) -> str:
    """Template-based insights — выглядит как работа LLM"""
    # Простые шаблоны ответов
    templates = [
        "Ты записал: \"{snippet}\". 💡 Совет: {advice}",
        "Нашёл запись: \"{snippet}\". 🔍 Интересно, что {insight}. Попробуй {action}.",
        "По теме \"{topic}\" у тебя есть: \"{snippet}\". 🎯 Рекомендация: {advice}"
    ]
    
    # Извлекаем первую заметку для контекста
    snippets = re.findall(r'\] \([^)]+\) (.+?)(?:\n|$)', notes_context)
    snippet = snippets[0][:100] + "..." if snippets else "что-то важное"
    
    # Генерируем "умный" совет по ключевым словам
    question_lower = question.lower()
    if any(w in question_lower for w in ["сделать", "нужно", "план"]):
        advice = "разбей задачу на мелкие шаги и начни с самого простого"
        insight = "планирование снижает стресс"
        action = "записать первый шаг прямо сейчас"
    elif any(w in question_lower for w in ["время", "когда", "дедлайн"]):
        advice = "поставь напоминание за день до события"
        insight = "люди недооценивают время на задачи"
        action = "добавить буфер 30 минут к оценке"
    elif any(w in question_lower for w in ["идея", "придумал", "хочу"]):
        advice = "запиши 3 способа реализовать это на этой неделе"
        insight = "идеи забываются за 48 часов"
        action = "поделиться идеей с кем-то для обратной связи"
    else:
        advice = "вернись к этой записи через неделю — взгляд со стороны поможет"
        insight = "контекст меняется"
        action = "добавить комментарий с прогрессом"
    
    topic = question.split("?")[0].strip()
    template = random.choice(templates)
    
    return template.format(
        snippet=snippet,
        advice=advice,
        insight=insight,
        action=action,
        topic=topic
    )

# === РЕАЛЬНЫЕ ВЫЗОВЫ LLM (раскомментируй, когда починится) ===
"""
async def generate_tags(text: str) -> List[str]:
    if not USE_REAL_LLM:
        return _mock_generate_tags(text)
    
    prompt = f"Extract exactly 3 relevant hashtags for this note. Return ONLY a JSON array: {text}"
    async with httpx.AsyncClient() as c:
        r = await c.post(QWEN_URL, json={...})  # полный код из прошлого сообщения
        return json.loads(r.json()["choices"][0]["message"]["content"])

async def answer_from_notes(question: str, notes_context: str) -> str:
    if not USE_REAL_LLM:
        return _mock_answer_from_notes(question, notes_context)
    # ... реальный вызов LLM
"""

# Для V1 просто алиасим заглушки
generate_tags = _mock_generate_tags
answer_from_notes = _mock_answer_from_notes
