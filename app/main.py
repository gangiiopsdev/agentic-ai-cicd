from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def execute_ping(host: str):
        # Safer implementation
        try:
            subprocess.run(['ping', host], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError("Invalid hostname")
    SafePing.execute_ping(host)
    return {"status": "completed"}