from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(char.isalnum() or char in ['-', '.', ':'] for char in host):
        return {"error": "Invalid hostname"}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}