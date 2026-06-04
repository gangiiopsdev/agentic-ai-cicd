from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed", "output": subprocess.run(['ping', host], check=True, capture_output=True).stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}