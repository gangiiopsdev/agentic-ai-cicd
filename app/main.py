from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result

def ping(host: str):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(safe_ping(host))
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)