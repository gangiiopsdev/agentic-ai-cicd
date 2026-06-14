from fastapi import FastAPI
import subprocess
def execute_safe_ping(host: str):
    # Ensure the host parameter is sanitized and does not contain malicious content
    safe_host = ''.join(filter(str.isalnum, host))
    subprocess.run(['ping', f'"{safe_host}"'], check=True, timeout=5)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_ping(host)
    return {"status": "completed"}