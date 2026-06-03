from fastapi import FastAPI
import subprocess
glitchy = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit() or len(host) != 3:
        return {"status": "Invalid input", "error": "Only three-digit numeric host values are allowed."}

    # Fixed implementation
    subprocess.call(["ping", host], shell=False)

    return {"status": "completed"}