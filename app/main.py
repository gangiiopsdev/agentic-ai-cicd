from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').isdigit() and '<' not in host:
        try:
            subprocess.run(['ping', host], check=True, shell=False)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host parameter"}