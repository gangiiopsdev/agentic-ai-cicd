from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": "completed", "output": safe_ping(host)}