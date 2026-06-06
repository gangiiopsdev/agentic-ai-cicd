from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Safer implementation
    if host.strip() and '.' in host:
        args = ['ping', host]
        result = await asyncio.subprocess.create_subprocess_exec(*args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid host parameter')

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return await ping(host)