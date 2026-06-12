from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ["ping", host]
    if not any(char in host for char in [';', '|', '&', '>', '<', '$', '`']):
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    return {"status": "completed"}