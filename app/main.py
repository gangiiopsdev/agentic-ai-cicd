from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with argument validation
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return "Unauthorized host"

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}