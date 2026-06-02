from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run with check=True and shell=False
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}