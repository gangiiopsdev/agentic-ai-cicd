from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '._')
    result = safe_ping(sanitized_host)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr if result.returncode != 0 else None
    }