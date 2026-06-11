from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize input
    if host.strip() in ['localhost', '127.0.0.1']:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)