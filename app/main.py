from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return 'Ping failed'