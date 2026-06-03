from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use check_output to avoid shell=True and potential command injection
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', result.stderr)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    return {"status": "completed"}