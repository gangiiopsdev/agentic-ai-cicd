from fastapi import FastAPI
import subprocess
global app = FastAPI()

async def ping(host: str):
    # Secure implementation using check_output instead of call
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await ping(host)