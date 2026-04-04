#!/usr/bin/env python3
"""MCP server for observability tools."""
import os, httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server

VLOGS = os.environ.get("VICTORIALOGS_URL", "http://victorialogs:9428")
VTRACES = os.environ.get("VICTORIATRACES_URL", "http://victoriatraces:10428")
app = Server("mcp-obs")

@app.tool()
async def logs_search(query: str, limit: int = 10) -> list:
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{VLOGS}/select/logsql/query", params={"query": query, "limit": limit}, timeout=30)
        r.raise_for_status()
        return r.json().get("data", [])

@app.tool()
async def logs_error_count(service: str, minutes: int = 60) -> dict:
    q = f'_time:{minutes}m service.name:"{service}" severity:ERROR'
    return {"count": len(await logs_search(q, 100)), "service": service, "window_minutes": minutes}

@app.tool()
async def traces_list(service: str, limit: int = 5) -> list:
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{VTRACES}/select/jaeger/api/traces", params={"service": service, "limit": limit}, timeout=30)
        r.raise_for_status()
        return [{"traceID": t.get("traceID"), "spans": len(t.get("spans", []))} for t in r.json().get("data", [])]

@app.tool()
async def traces_get(trace_id: str) -> dict:
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{VTRACES}/select/jaeger/api/traces/{trace_id}", timeout=30)
        r.raise_for_status()
        return r.json().get("data", [{}])[0]

async def main():
    async with stdio_server() as (r, w): await app.run(r, w)

if __name__ == "__main__": import asyncio; asyncio.run(main())
