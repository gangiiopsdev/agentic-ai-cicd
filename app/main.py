from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
    except subprocess.TimeoutExpired:
        return 'Ping timed out'
    except Exception as e:
        return f'Ping failed: {e}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}