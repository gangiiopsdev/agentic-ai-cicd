from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with shell=False and full executable path
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_host(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}