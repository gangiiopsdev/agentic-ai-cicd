from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.isnumeric():
        args = ['ping', host]
        subprocess.run(args, check=True)
    else:
        return {"error": "Invalid input"}

    return {"status": "completed"}