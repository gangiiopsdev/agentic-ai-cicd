from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 50:
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(['ping', host])
    return {"status": "completed"}