from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str) -> None:
        # Safe implementation using list instead of string for the command and validating input
        if not host.strip().replace('.', '').isdigit():
            raise ValueError('Invalid hostname or IP address')
        subprocess.call(['ping', '-c', '4', host])  # Limiting number of pings to mitigate DDoS risk

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.safe_ping(host)
    return {"status": "completed"}