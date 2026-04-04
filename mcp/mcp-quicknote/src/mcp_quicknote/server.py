import os, httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("quicknote")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

@app.tool()
async def save_note(content: str) -> str:
    """Save a note and get auto-tags"""
    async with httpx.AsyncClient() as c:
        r = await c.post(f"{BACKEND_URL}/notes", params={"content": content}, timeout=10)
        return r.json().get("message", "Saved")

@app.tool()
async def query_notes(question: str) -> str:
    """Ask a question about saved notes"""
    async with httpx.AsyncClient() as c:
        r = await c.post(f"{BACKEND_URL}/notes/ask", params={"question": question}, timeout=15)
        return r.json().get("answer", "No notes found.")

async def main():
    async with stdio_server() as (r, w):
        await app.run(r, w)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
