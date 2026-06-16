from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Split the command and arguments into a list to avoid shell injection risks
        subprocess.call(['ping', host], timeout=5)
    except Exception as e:
        print(f'Error pinging {host}: {e}')
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}