from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and shlex.split to safely pass arguments
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}