from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return ping(host)