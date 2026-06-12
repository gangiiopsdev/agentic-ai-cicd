from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run to avoid shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use the safe_ping function to avoid shell=True
    return {'status': 'completed', 'result': safe_ping(host)}