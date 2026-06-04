from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Safe implementation using a list for args
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500