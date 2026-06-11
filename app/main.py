from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], timeout=5, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    return {"status": "completed", "output": output.decode('utf-8')}