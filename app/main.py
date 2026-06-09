from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        # Safe implementation using subprocess.run instead of subprocess.call
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')
    return PingCommand.safe_ping(host)