from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping/{host}")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
        return {"status": "completed", "message": f'Ping to {host} successful'}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}