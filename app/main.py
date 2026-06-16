from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host is required'}
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)