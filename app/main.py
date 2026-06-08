from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation with shell=False and argument list to avoid command injection
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}