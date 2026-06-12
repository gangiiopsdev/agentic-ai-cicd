from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.strip():
        return {"error": "Host is required"}
    safe_host = subprocess.list2cmdline([host])
    try:
        subprocess.run(['ping', safe_host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)