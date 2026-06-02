from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and args parameter
        result = await asyncio.to_thread(subprocess.run, ['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)