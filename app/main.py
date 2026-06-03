from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize input
    if host.strip() == '':
        return {'error': 'Invalid host'}
    return subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }