from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    try:
        # Use subprocess.run instead of subprocess.check_output for better control
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return {"status": "error", "message": result.stderr}
        else:
            return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}