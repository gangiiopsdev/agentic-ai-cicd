from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Constructing the command safely
    cmd = ['ping', host]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'output': result.stdout.decode(), 'error': result.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)