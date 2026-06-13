from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the host input
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)