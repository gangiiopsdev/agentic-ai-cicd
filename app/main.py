from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def ping(host: str):
        if host.startswith('-') or '&&' in host or ';' in host or '|':
            raise ValueError('Invalid input')
        # Use subprocess.run instead of subprocess.call to avoid shell=True
        subprocess.run(['ping', host], check=True, capture_output=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    PingCommand.ping(host)
    return {"status": "completed"}