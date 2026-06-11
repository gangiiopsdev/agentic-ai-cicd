from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Splitting the command into a list avoids shell injection
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stderr}')
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": "Ping successful"}
    else:
        return {"status": "failed", "result": "Ping failed"}