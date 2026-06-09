from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        # Use subprocess.run with shell=False and arguments split for security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}, 500

@app.get("/ping")
def ping(host: str):
    return run_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}