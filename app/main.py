from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Sanitize the input to prevent command injection
    try:
        sanitized_host = shlex.quote(host)
        return subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    except Exception as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}