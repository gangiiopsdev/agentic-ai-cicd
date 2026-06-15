from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input to avoid command injection
        sanitized_host = subprocess.quote(host)
        result = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT)
        return {"status": "completed", "result": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}