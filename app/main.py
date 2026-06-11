from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate the host to ensure it does not contain malicious content
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}