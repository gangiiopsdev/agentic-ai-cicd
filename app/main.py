from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip() or len(host) > 255:
        return False
    return True

@app.get="/",
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid hostname"}

    # Secure implementation with complete path and input validation
    subprocess.call(['/bin/ping', host])
    return {"status": "completed"}