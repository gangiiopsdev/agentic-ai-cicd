from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize host input to prevent command injection
    args = ['ping', host.replace(' ', '_')]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)