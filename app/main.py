from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "output": e.output.decode()}
    return {"status": "completed"}