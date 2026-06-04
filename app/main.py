from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with input validation
        if not host.strip() or '&&' in host or ';' in host:
            raise ValueError('Invalid host parameter')
        args = ['ping', '-c', '4', host]
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'output': process.stdout, 'error': process.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return SafePing.ping(host)