from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        try:
            # Safer implementation
            subprocess.run(['ping', host], check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return PingCommand.ping(host)