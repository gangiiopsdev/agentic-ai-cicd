from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Sanitize input by escaping special characters
        host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)