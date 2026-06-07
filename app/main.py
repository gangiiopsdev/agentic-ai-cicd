from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host or len(host) > 255:
        return {"error": "Invalid host name"}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"error": e.output.decode('utf-8')}
    return {"status": "completed", "output": output.decode('utf-8')}