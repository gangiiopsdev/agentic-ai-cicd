from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run and shell=False to avoid command injection
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}