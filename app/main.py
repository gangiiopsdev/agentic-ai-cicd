from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize and validate input
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        command = ["ping", host]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.stdout.strip()
    else:
        raise ValueError("Invalid host")

app = FastAPI()
@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"error": str(e)}