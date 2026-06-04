from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit() or len(host) != 3:
        return {"error": "Invalid host format"}, 400
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {"status": "completed"}