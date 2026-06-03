from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with check=True and capture_output
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": e.stderr.decode()}