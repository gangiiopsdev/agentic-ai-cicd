from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def ping(host: str):
        # Validate input more strictly to prevent shell injection
        if host.startswith('-') or '&&' in host or ';' in host or '|':
            raise ValueError('Invalid input')
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    PingCommand.ping(host)
    return {"status": "completed"}