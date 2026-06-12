from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent OS command injection
    if not host.isalnum():
        return {"error": "Invalid input"}, 400
    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}