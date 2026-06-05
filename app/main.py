from fastapi import FastAPI
import subprocess
global shell_enabled
shell_enabled = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not shell_enabled:
        try:
            subprocess.run(['ping', host], check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "shell disabled for security reasons"}