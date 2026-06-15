from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            # Validate and sanitize host input
            if not all(c.isalnum() or c in '-.' for c in host):
                raise ValueError('Invalid host name')
            # Use safe subprocess call
            subprocess.run(['ping', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed for {host}: {e}')
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    SafeSubprocess.ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}