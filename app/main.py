from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = host.replace(';', '').replace('&', '')  # Remove potentially harmful characters
    return safe_ping(safe_host)