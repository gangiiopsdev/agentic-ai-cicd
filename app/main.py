from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    else:
        return {
            "status": "denied",
            "message": "Host not allowed"
        }

class SafePingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ['example.com', 'localhost']:
        return {
            "status": "denied",
            "message": "Host not allowed"
        }
    try:
        result = SafePingCommand(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }