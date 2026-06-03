from fastapi import FastAPI
import subprocess
get_running_loop = asyncio.get_running_loop

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    loop = get_running_loop()
    sanitized_host = subprocess.quote(host)
    await loop.run_in_executor(None, subprocess.call, ['ping', sanitized_host])
    return {'status': 'completed'}