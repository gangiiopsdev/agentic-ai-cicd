from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and a safe command construction
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": subprocess.PIPE.decode('utf-8'), "stderr": subprocess.PIPE.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "stdout": str(e.output), "stderr": str(e.stderr)}