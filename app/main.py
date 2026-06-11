from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    try:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed", "host": host}
    except subprocess.CalledProcessError as e:
        return {"error": f'Ping failed for {host}: {e}'}