from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)