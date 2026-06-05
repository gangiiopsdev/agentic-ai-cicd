from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global host
    host = host.strip()
    if not host:
        raise ValueError('Host cannot be empty')
    safe_host = subprocess.list2cmdline([host])  # Sanitize the host input
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "host": host,
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "host": host,
            "error": str(e)
        }

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}