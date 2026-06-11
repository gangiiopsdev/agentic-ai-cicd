from fastapi import FastAPI
import subprocess
import shlex

class SafeCommandRunner:
    @staticmethod
def safe_ping(host: str) -> dict:
        command = 'ping'
        args = shlex.split(f'{command} {host}')
        try:
            subprocess.run(args, check=True, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeCommandRunner.safe_ping(host)
    return result