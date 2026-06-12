from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    safe_host = escape_host(host)
    args = ['ping', '--'] + [safe_host]  # Use -- to prevent injection
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}