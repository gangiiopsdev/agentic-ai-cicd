from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}