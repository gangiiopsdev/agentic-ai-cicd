from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError("Invalid characters in host")
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)