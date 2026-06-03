from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.strip() or '&&' in host or ';' in host or '| ' in host:
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}