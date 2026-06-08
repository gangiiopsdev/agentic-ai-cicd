from fastapi import FastAPI
import subprocess

app = FastAPI()

async def execute_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode()
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)