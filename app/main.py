from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.isnumeric():
        args = ['ping', host]
        subprocess.call(args)
    else:
        return {"error": "Invalid input"}

    return {"status": "completed"}