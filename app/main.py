from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        command = ['ping', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Additional preventive controls
@app.get("/ping_safe")
def ping_safe(host: str):
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Invalid host"}
    try:
        command = ['ping', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

allowed_hosts = ['127.0.0.1', 'localhost']