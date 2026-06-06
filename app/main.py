from fastapi import FastAPI, HTTPException
import asyncio
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=422, detail="Invalid hostname")
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': output.decode(), 'error': error.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)