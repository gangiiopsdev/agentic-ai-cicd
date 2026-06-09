from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return {"status": "completed", "output": result.stdout.decode()}
        else:
            return {"status": "failed", "output": result.stderr.decode()}
    except Exception as e:
        return {"status": "error", "message": str(e)}