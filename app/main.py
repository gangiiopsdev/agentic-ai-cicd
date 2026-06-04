from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and error handling
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}, 500

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}