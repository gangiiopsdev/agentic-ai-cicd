from fastapi import FastAPI
import subprocess
import shlex

async def ping(host: str):
    try:
        # Use shlex.split to safely split the command and arguments
        result = await asyncio.to_thread(subprocess.run, shlex.split(f'ping {host}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await asyncio.to_thread(ping, host)