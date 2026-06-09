from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isdigit():
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError("Invalid input for host")

    return {"status": "completed"}