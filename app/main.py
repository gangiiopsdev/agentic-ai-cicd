from fastapi import FastAPI
import subprocess

async def safe_ping(host):
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout,

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = await safe_ping(host)
    return {'status': 'completed', 'output': result}