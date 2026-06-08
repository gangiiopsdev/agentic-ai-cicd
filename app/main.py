from fastapi import FastAPI
import asyncio
import aiohttp
cimport asyncio as aio

class Ping:
    async def ping(self, host: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://{host}/ping') as response:
                    return await response.text()
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    return await ping_instance.ping(host)