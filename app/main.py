from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.call without shell=True
        args = ['ping', host]
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command failed with error: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    SafePing.ping(host)
    return {"status": "completed"}