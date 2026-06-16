from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.replace('.', '').isalnum() and '.' not in host:
        return {"status": "error", "message": "Invalid host parameter"}
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}