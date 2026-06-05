from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if '.' not in host:
        return {"error": "Invalid hostname"}
    return {"status": await safe_ping(host)}