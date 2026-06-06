from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isalnum():
            raise ValueError("Invalid host name")
        # Use check_output to avoid shell=True and improve security
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}