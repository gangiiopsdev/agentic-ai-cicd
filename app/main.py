from fastapi import FastAPI
import subprocess
global ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')

    return {"status": "completed"}