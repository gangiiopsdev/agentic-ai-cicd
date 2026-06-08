from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Validate and sanitize the host parameter
        if not host.isalnum() or len(host) > 63:
            raise ValueError('Invalid host name')
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)