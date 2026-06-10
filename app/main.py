from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the host input
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}
def is_valid_host(host: str) -> bool:
    # Implement validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts