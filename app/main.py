from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            subprocess.run(['ping', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}