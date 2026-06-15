from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.output.decode()}')

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}